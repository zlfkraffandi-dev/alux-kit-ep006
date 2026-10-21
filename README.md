# SOP & Panduan Editor: Sourcing & Penempatan Aset (EP006 Part 1)

Panduan kerja untuk editor (**Repi, Sultan, Agil**) dalam mencari footage, mengunduh aset, hingga menempatkannya di timeline Adobe Premiere Pro sesuai file cue sheet `EP006_Part1_BROLL_EDITOR.html`.

---

## 1. Pembagian Tugas & Cakupan File (Part 1)

Buka file **`EP006_Part1_BROLL_EDITOR.html`** di browser Chrome / Edge. Klik tombol nama kalian di toolbar atas:

| Editor | Scene / Chapter | Cakupan |
|---|---|---|
| **REPI** | `S01` Cold Open, `S02` Ch 1, `S03` Ch 2 | 67 slot (34 Footage, 30 Graphic, 3 Archive) |
| **SULTAN** | `S04` Ch 3, `S05` Ch 4, `S06` Ch 5 | 103 slot (61 Footage, 40 Graphic, 2 Archive) |
| **AGIL** | `S07` Ch 6 *(sisa Ch 7–9 di Part 2)* | 19 slot (11 Footage, 7 Graphic, 1 Archive) |

*Catatan: Zulfikar akan mulai di Batch Part 2 (Chapter 9–11).*

---

## 2. Mengenal 3 Kategori Isian (Marking Timeline)

Setiap baris di HTML dan timeline Premiere ditandai dengan garis warna & badge:

1. <span style="color:#10b981;font-weight:bold;">[FOOTAGE]</span> (Kode `B001` s/d `B100` | Garis Hijau)
   * **Sumber:** Stock video komersial dari **Envato Elements**.
   * **Tujuan Timeline:** Masuk ke track **`V1`** (di bawah marking `V4`).
   * **Cara:** Klik tombol **Cari** di HTML untuk langsung membuka hasil pencarian Envato, atau klik **Copy** untuk menyalin keyword.

2. <span style="color:#6366f1;font-weight:bold;">[GRAPHIC]</span> (Kode `EP006-001` s/d `083` | Garis Ungu)
   * **Sumber:** Desain dari **Figma**, render **MOGRT**, atau animasi peta **GeoLayers 3** (After Effects).
   * **Tujuan Timeline:** Masuk ke track **`V3`** (di bawah marking `V6`).
   * **Cara:** Cek kolom *Konteks & arahan visual*. Jika bertanda `GeoLayers 3`, siapkan animasi peta sesuai koordinat GPS yang tertera. Jika ada link artikel berita (BBC/CNN), klik link untuk referensi screenshot koran/web.

3. <span style="color:#f59e0b;font-weight:bold;">[ARCHIVE]</span> (Kode `A001` s/d `A006` | Garis Kuning)
   * **Sumber:** Dokumen sejarah, foto arsip, cuplikan berita lama, atau Wikimedia Commons.
   * **Tujuan Timeline:** Masuk ke track **`V2`** (di bawah marking `V5`).
   * **Cara:** Lihat keterangan di kolom *Sumber/Aset* (misal: *National Geographic*, *History.com*, *USDA History*), cari footage/foto arsip yang relevan.

---

## 3. Standar Unduh (Download Rules)

* **Resolusi Utama:** Pilih resolusi **Full HD (1080p)** saat download dari Envato untuk efisiensi penyimpanan.
* **Frame Rate:** Utamakan **24 fps** (sesuai sequence Premiere 24.0 fps). Jika dapat 25/30/60 fps, sesuaikan di Interpret Footage bila perlu.
* **Format Penamaan File:** Wajib sertakan KODE di depan nama file agar mudah dicari:
  * Contoh: `B001_refrigerated_truck_dock.mp4`
  * Contoh: `A001_chicken_of_tomorrow_1948.mp4`

---

## 4. Aturan Penempatan di Adobe Premiere Pro

Susunan Track di Sequence:
```text
[V8] CHAPTER                <- Penanda nama babak (jangan digeser)
[V6] ADJUSTMENT GRAPHIC     <- Marking durasi grafis
[V5] ADJUSTMENT ARCHIVE     <- Marking durasi arsip
[V4] ADJUSTMENT ENVATO      <- Marking durasi footage stock
-------------------------------------------------------------------
[V3] (Tempat Aset Grafis)   <- Letakkan render grafis / MOGRT di sini
[V2] (Tempat Arsip)         <- Letakkan video / foto arsip di sini
[V1] (Tempat Footage)       <- Letakkan stock video Envato di sini
-------------------------------------------------------------------
[A1 / A2] VOICE OVER        <- TERKUNCI (LOCKED) - JANGAN DIUBAH
```

### Aturan Wajib Editing:
1. **Snap Sesuai Marking:**
   * Aktifkan tombol **Snap (`S`)** di timeline Premiere.
   * Panjang klip di `V1` atau `V2` harus pas dari awal sampai akhir batas adjustment layer di atasnya (`V4` atau `V5`). Jangan ada gap / lubang hitam.
2. **Zero Vertical Stacking (Dilarang Menumpuk):**
   * Di titik waktu yang ada `GRAPHIC` (`V6`), di bawahnya (`V1`/`V2`) **TIDAK BOLEH** ada footage atau arsip, KECUALI jika arahan grafisnya transparan dan meminta latar gelap/subtle background.
   * Begitu pula antara `V1` dan `V2`: jika slot arsip aktif, track footage kosong.
3. **Scale to Frame:**
   * Sequence berukuran **3840×2160 (4K UHD)**.
   * Footage 1080p wajib di-scale **200%** (atau klik kanan -> *Set to Frame Size*) agar menutupi frame penuh (tidak ada border hitam).
   * Footage 4K biarkan pada scale **100%**.

---

## 5. Pelacakan Progres (Done Checkbox)

1. Setelah satu shot selesai diimpor dan dipasang rapi di timeline, kembali ke browser.
2. Centang kotak **Done** di kolom paling kanan baris tersebut.
3. Progres akan otomatis tersimpan di browser kalian masing-masing melalui *localStorage* (tidak akan hilang saat browser direfresh).
4. Angka indikator di pojok kanan atas (`Selesai: X / 189`) akan bertambah otomatis.

---

## 6. Prompting Eksekusi (Untuk ChatGPT / Claude / AI Assistant)

Jika kalian kesulitan menemukan stock video yang pas, butuh arsip sejarah, atau ingin menerjemahkan narasi abstrak menjadi shot konkret, gunakan template prompt di bawah ini ke AI (ChatGPT / Claude). Tinggal copy-paste dan isi data dari tabel HTML.

### Prompt A: Mencari Alternatif Keyword Envato (Bila Hasil Default Nihil / Kurang Pas)
Gunakan prompt ini jika tombol "Cari" di HTML tidak memberikan video yang memuaskan:
```text
Bertindaklah sebagai Senior B-Roll Visual Researcher untuk dokumenter video esai Alux.
Saya sedang mengedit slot footage berikut:
- Kode Slot: [Isi Kode, misal: B015]
- Konteks & Arahan Visual: [Copy dari kolom Konteks di tabel HTML]
- Kalimat Voice Over (VO): [Copy kalimat VO di tabel HTML]
- Durasi: [Isi durasi detik]

Masalah: Keyword default di tabel tidak menghasilkan klip yang bagus di Envato Elements.
Aturan:
1. Berikan 5 alternatif query pencarian bahasa Inggris (terdiri dari 2–4 kata per query).
2. Fokus pada SUBJEK KONKRET + AKSI NYATA (misal: "poultry conveyor inspection", "refrigerated warehouse forklift").
3. DILARANG menggunakan kata filler sampah: "cinematic", "dramatic", "4k", "moody", "slow motion".
4. Tentukan era (modern vs vintage) sesuai konteks cerita.
5. Berikan penjelasan singkat (1 kalimat) untuk tiap query mengapa shot itu tepat untuk mendukung kalimat VO tersebut.
```

---

### Prompt B: Riset Sumber Arsip Sejarah & Dokumen Publik (Track V5 - Archive)
Gunakan prompt ini khusus untuk baris bertanda **`[ARCHIVE]`** (`A001` s/d `A006`):
```text
Bertindaklah sebagai Archival Researcher dokumenter sejarah.
Saya membutuhkan footage / foto resolusi tinggi / scan dokumen publik autentik untuk slot arsip:
- Kode Slot: [Isi Kode, misal: A001]
- Referensi Naskah: [Copy dari kolom Sumber/Aset, misal: Chicken of Tomorrow Contest 1948, USDA History]
- Kalimat Narasi (VO): [Copy kalimat VO di tabel HTML]

Tolong berikan:
1. Nama arsip publik atau database open-access tempat aset ini tersimpan (misal: Library of Congress, US National Archives / NARA, Wikimedia Commons, Prelinger Archives).
2. Kata kunci pencarian spesifik untuk dicari di Google / YouTube / Archive.org.
3. Rekomendasi apakah aset ini lebih cocok berupa video arsip bergerak (film hitam-putih) atau scan foto dokumen koran/foto arsip statis dengan camera push-in.
```

---

### Prompt C: Menerjemahkan Kalimat VO Abstrak Menjadi B-Roll Nyata
Gunakan prompt ini jika kalimat narator sangat abstrak atau berupa filosofi bisnis:
```text
Sebagai visual director video esai, bantu saya memvisualisasikan kalimat narasi abstrak ini:
- Kalimat Narator: "[Isi kalimat narasi, contoh: 'The system decided this years before you walked into the store.']"
- Topik Video: Industri peternakan ayam & rantai pasok makanan cepat saji AS.
- Target Platform B-Roll: Envato Elements (Stock footage).

Berikan 3 konsep visual konkret yang metaforis namun tetap grounded (masuk akal di mata penonton), lengkap dengan:
1. Deskripsi Shot (Angle, subjek, dan pergerakan kamera).
2. Keyword pencarian Envato (2–3 kata bahasa Inggris).
3. Makna psikologis / subteks yang ingin disampaikan ke penonton.
```

---

### Prompt D: Skrip Otomatisasi Rename File Footage Massal (Python / Batch)
Jika kalian mengunduh 20–30 file sekaligus dari Envato dan ingin otomatis me-rename sesuai kode slot tabel HTML, paste prompt ini ke AI:
```text
Saya punya daftar file video stock yang baru diunduh di folder 'C:/Downloads/EP006_BROLL/'.
Daftar pasangan kode slot dan deskripsinya adalah:
- B001: refrigerated truck loading dock
- B002: close up wings sauce sports bar
- B003: chicken broiler farm conveyor
[dst...]

Tolong buatkan skrip Python sederhana (atau batch script Windows) untuk me-rename file-file tersebut agar format namanya menjadi '[KODE]_[deskripsi_singkat].mp4' secara rapi.
```

