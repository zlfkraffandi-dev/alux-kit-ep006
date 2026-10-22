"""
Automasi Download Envato Elements untuk Proyek ALUX EP006 Part 1
Mengambil data slot langsung dari GitHub Pages / HTML cue sheet,
mencari di Envato dengan filter 1080p & Horizontal, mengunduh,
dan otomatis me-rename file sesuai format: [CODE]_[slug].[ext]
"""

import argparse
import asyncio
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import zipfile

try:
    import websockets
except ImportError:
    print("ERR: Library 'websockets' belum terinstall.")
    print("Jalankan: pip install websockets")
    sys.exit(1)

CUE_SHEET_URL = "https://zlfkraffandi-dev.github.io/alux-kit-ep006/"
BAD_WORDS = re.compile(
    r'3D|animat|cgi|render|cartoon|vector|silhouette|motion graphic|loop|background|abstract|futuristic|flat design|alpha',
    re.I
)

def fetch_cue_sheet():
    """Mengambil cue sheet dari GitHub Pages atau file lokal index.html"""
    if os.path.exists("index.html"):
        print("Membaca cue sheet dari file lokal 'index.html'...")
        content = open("index.html", encoding="utf-8").read()
    else:
        print(f"Mengunduh cue sheet online dari {CUE_SHEET_URL}...")
        req = urllib.request.Request(CUE_SHEET_URL, headers={"User-Agent": "ALUX-Envato-Downloader/1.0"})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode("utf-8")
    
    m = re.search(r'const D=(\[.*?\]);\s*\n', content, re.S)
    if not m:
        raise ValueError("Data cue sheet 'const D' tidak ditemukan dalam HTML!")
    return json.loads(m.group(1))

async def run_automation(editor, port, out_dir, scratch_dir, limit=None):
    editor = editor.upper()
    data = fetch_cue_sheet()
    
    # Filter footage Envato
    slots = [r for r in data if r.get('type') == 'ENVATO']
    if editor != "ALL":
        slots = [r for r in slots if r.get('ed') == editor]
    
    if limit:
        slots = slots[:limit]
        
    print(f"\nTotal slot FOOTAGE untuk editor '{editor}': {len(slots)} slot")
    if not slots:
        print("Tidak ada slot footage yang perlu diunduh.")
        return

    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(scratch_dir, exist_ok=True)
    progress_file = os.path.join(out_dir, f"progress_{editor.lower()}.json")
    
    progress = {}
    if os.path.exists(progress_file):
        try:
            progress = json.load(open(progress_file, encoding="utf-8"))
        except Exception:
            progress = {}

    # Scan file yang sudah ada di folder
    existing_files = os.listdir(out_dir)
    for s in slots:
        c = s['code']
        matched = [f for f in existing_files if f.startswith(f"{c}_")]
        if matched and c not in progress:
            progress[c] = {
                "file": matched[0],
                "path": os.path.join(out_dir, matched[0]),
                "status": "existing"
            }

    # Cek koneksi ke Chrome CDP
    cdp_json_url = f"http://127.0.0.1:{port}/json"
    try:
        tabs = json.load(urllib.request.urlopen(cdp_json_url, timeout=5))
    except Exception as e:
        print(f"\n[ERROR] Tidak dapat terhubung ke Chrome di port {port}!")
        print("Pastikan Chrome sudah dibuka dengan remote debugging:")
        print(f'chrome.exe --remote-debugging-port={port} --user-data-dir="<path_profile>"')
        print(f"Detail error: {e}")
        return

    page_tabs = [t for t in tabs if t.get('type') == 'page']
    if not page_tabs:
        print("[ERROR] Tidak ada tab browser yang terbuka di Chrome.")
        return
        
    ws_url = page_tabs[0]['webSocketDebuggerUrl']
    print(f"Terhubung ke Chrome via CDP (Tab: {page_tabs[0].get('title', '')[:40]}...)")

    async with websockets.connect(ws_url, max_size=None) as ws:
        msg_id = 0
        async def call(method, **params):
            nonlocal msg_id
            msg_id += 1
            i = msg_id
            await ws.send(json.dumps({'id': i, 'method': method, 'params': params}))
            while True:
                d = json.loads(await ws.recv())
                if d.get('id') == i:
                    return d.get('result', {})

        # Setup lokasi download otomatis
        abs_scratch = os.path.abspath(scratch_dir)
        await call('Browser.setDownloadBehavior', behavior='allow', downloadPath=abs_scratch, eventsEnabled=True)
        await call('Page.setDownloadBehavior', behavior='allow', downloadPath=abs_scratch)

        for idx, s in enumerate(slots, 1):
            code = s['code']
            # Nama file target
            first_q = s['q'][0] if s.get('q') else code
            slug = re.sub(r'[^a-zA-Z0-9]+', '_', first_q).strip('_').lower()
            fn_base = f"{code}_{slug}"
            
            if code in progress and os.path.exists(progress[code].get('path', '')):
                print(f"[{idx}/{len(slots)}] SKIP {code} (Sudah ada: {progress[code]['file']})")
                continue

            dur = round(s['et'] - s['st'], 1)
            print(f"\n=======================================================")
            print(f"[{idx}/{len(slots)}] MENGUNDUH {code} (Target durasi: {dur}s)")
            print(f"Arah Visual: {s.get('ctx', '')[:80]}...")

            # Bersihkan scratch folder
            for f in os.listdir(abs_scratch):
                try: os.remove(os.path.join(abs_scratch, f))
                except Exception: pass

            # 1. Cari di Envato
            queries = s.get('q', [first_q])
            cards = []
            chosen_q = queries[0]
            
            for q in queries:
                search_url = (
                    f"https://app.envato.com/search?itemType=stock-video&term={urllib.parse.quote_plus(q)}"
                    f"&filter.video_resolutions=1080p+%28Full+HD%29&filter.orientation=Horizontal"
                )
                print(f" -> Mencari di Envato: '{q}' (1080p, Horizontal)...")
                await call('Page.navigate', url=search_url)
                await asyncio.sleep(3.5)

                js_get_cards = """
                (() => {
                    const items = [...document.querySelectorAll('[data-cy=item-card]')];
                    const res = [];
                    for (const c of items.slice(0, 15)) {
                        const a = c.querySelector('[data-analytics-item_title]');
                        const title = a ? a.getAttribute('data-analytics-item_title') : '';
                        const link = c.querySelector('a[href*="/search/stock-video/"]')?.href || c.querySelector('a')?.href;
                        if (title && link) res.push({title, link});
                    }
                    return res;
                })()
                """
                r = await call('Runtime.evaluate', expression=js_get_cards, returnByValue=True)
                res = r.get('result', {}).get('value') or []
                valid = [c for c in res if not BAD_WORDS.search(c['title'])]
                if valid:
                    cards = valid
                    chosen_q = q
                    break

            if not cards:
                print(f"[LEWAT] Tidak ditemukan video live-action yang cocok untuk {code}")
                continue

            # Skor kecocokan kata kunci
            best = cards[0]
            ctx_words = set(re.findall(r'[a-zA-Z]{4,}', (s.get('ctx', '') + ' ' + chosen_q).lower()))
            best_score = -1
            for c in cards:
                score = sum(1 for w in ctx_words if w in c['title'].lower())
                if score > best_score:
                    best_score = score
                    best = c

            print(f" -> Kartu Terpilih: '{best['title']}'")
            print(f"    URL: {best['link']}")

            # 2. Buka halaman detail item
            await call('Page.navigate', url=best['link'])
            await asyncio.sleep(3.5)

            # 3. Pastikan format 1080P terpilih
            js_fmt = """
            (() => {
                const btn = document.querySelector('[data-cy="idp-download-button"]');
                if (btn && btn.innerText.includes('1080P')) return {ready: true};
                const trigger = document.querySelector('[data-cy="idp-format-dropdown-trigger"]');
                if (trigger) {
                    const expanded = trigger.getAttribute('aria-expanded') === 'true';
                    if (!expanded) trigger.click();
                    return {ready: false, opened: true};
                }
                return {ready: false, opened: false};
            })()
            """
            r_fmt = await call('Runtime.evaluate', expression=js_fmt, returnByValue=True)
            fmt_res = r_fmt.get('result', {}).get('value') or {}
            if not fmt_res.get('ready'):
                await asyncio.sleep(0.6)
                js_opt = """
                (() => {
                    const btns = [...document.querySelectorAll('button, [role="menuitem"], [role="option"]')];
                    const opt = btns.find(b => b.innerText.includes('1080P'));
                    if (opt) { opt.click(); return true; }
                    return false;
                })()
                """
                await call('Runtime.evaluate', expression=js_opt, returnByValue=True)
                await asyncio.sleep(0.8)

            # 4. Klik Download
            before = set(os.listdir(abs_scratch))
            js_dl = """
            (() => {
                const btn = document.querySelector('[data-cy="idp-download-button"]');
                if (btn) { btn.click(); return true; }
                const btns = [...document.querySelectorAll('button')];
                const b2 = btns.find(x => (x.innerText||'').toLowerCase().includes('download'));
                if (b2) { b2.click(); return true; }
                return false;
            })()
            """
            await call('Runtime.evaluate', expression=js_dl, returnByValue=True)
            print(" -> Menunggu unduhan selesai...")

            dl_file = None
            for _ in range(45):
                await asyncio.sleep(1)
                files = [f for f in os.listdir(abs_scratch) if f not in before]
                if files and not any(f.endswith('.crdownload') for f in files):
                    dl_file = os.path.join(abs_scratch, files[0])
                    break

            if not dl_file or not os.path.exists(dl_file):
                print(f"[GAGAL] Timeout saat mengunduh {code}")
                continue

            sz_mb = os.path.getsize(dl_file) / 1024 / 1024
            print(f" -> Selesai diunduh: {os.path.basename(dl_file)} ({sz_mb:.1f} MB)")

            # Ekstrak jika format ZIP
            if dl_file.endswith('.zip'):
                with zipfile.ZipFile(dl_file) as z:
                    vids = [n for n in z.namelist() if n.lower().endswith(('.mp4', '.mov'))]
                    if vids:
                        z.extract(vids[0], abs_scratch)
                        extracted = os.path.join(abs_scratch, vids[0])
                        try: os.remove(dl_file)
                        except Exception: pass
                        dl_file = extracted

            ext = os.path.splitext(dl_file)[1].lower()
            target_fn = f"{fn_base}{ext}"
            target_path = os.path.join(out_dir, target_fn)
            shutil.move(dl_file, target_path)

            progress[code] = {
                "file": target_fn,
                "path": target_path,
                "title": best['title'],
                "url": best['link'],
                "size_mb": round(sz_mb, 1),
                "status": "downloaded"
            }
            json.dump(progress, open(progress_file, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
            print(f" -> Berhasil disimpan sebagai: {target_fn}")
            await asyncio.sleep(1.5)

    print(f"\n[SELESAI] Semua footage untuk editor '{editor}' selesai diproses di {out_dir}!")

def main():
    parser = argparse.ArgumentParser(description="Automasi Unduh Footage Envato Elements ALUX EP006")
    parser.add_argument("--editor", "-e", choices=["REPI", "SULTAN", "AGIL", "ALL"], default="REPI",
                        help="Filter nama editor (default: REPI)")
    parser.add_argument("--port", "-p", type=int, default=9222,
                        help="Port Chrome remote debugging (default: 9222)")
    parser.add_argument("--out-dir", "-o", default=None,
                        help="Folder tujuan penyimpanan footage (default: FOOTAGE/<EDITOR>)")
    parser.add_argument("--scratch-dir", default=None,
                        help="Folder sementara unduhan")
    parser.add_argument("--limit", "-l", type=int, default=None,
                        help="Batasi jumlah slot yang diunduh")
    args = parser.parse_args()

    out_dir = args.out_dir or os.path.join("FOOTAGE", args.editor)
    scratch_dir = args.scratch_dir or os.path.join(os.path.expanduser("~"), "AppData", "Local", "hermes", "cache", "scratch", "envato_dl")

    asyncio.run(run_automation(args.editor, args.port, out_dir, scratch_dir, args.limit))

if __name__ == "__main__":
    main()
