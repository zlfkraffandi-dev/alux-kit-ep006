# SOP & Panduan Automasi Download Footage Envato Elements (EP006 Part 1)

Panduan ini menjelaskan cara mengunduh seluruh footage stock video dari **Envato Elements** secara otomatis menggunakan skrip Python (`download_envato.py`) atau melalui perintah langsung di **Hermes Chat** (Premiere Pro CEP Panel).

---

## 1. Kebutuhan & Prasyarat Sistem

Sebelum menjalankan automasi, pastikan hal-hal berikut sudah siap di komputer:

1. **Python 3.9+ & Library `websockets`:**
   ```bash
   pip install websockets
   ```
2. **Google Chrome dalam Mode Remote Debugging (Port 9222):**
   Automasi membutuhkan browser Chrome yang sudah **login ke akun Envato Elements** (langganan aktif) dan dijalankan dengan remote port.
   
   *Cara buka Chrome remote debugging di Windows:*
   * Tutup seluruh jendela Chrome terlebih dahulu, lalu jalankan di terminal / Command Prompt:
     ```bash
     "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="%LOCALAPPDATA%\Google\Chrome\AutomationProfile"
     ```
   * Pastikan tab Chrome terbuka dan buka https://elements.envato.com (login akunmu).
3. **Repo Kerja Terkini:**
   ```bash
   cd "%USERPROFILE%\alux-kit-ep006" && git pull
   ```

---

## 2. Cara 1: Menjalankan Skrip Otomasi Python (CLI)

Di folder repo `alux-kit-ep006`, kalian bisa langsung menjalankan perintah sesuai nama editor masing-masing:

### Untuk REPI (31 Footage | `B001` s/d `B031`):
```bash
python download_envato.py --editor REPI
```

### Untuk SULTAN (58 Footage | `B032` s/d `B089`):
```bash
python download_envato.py --editor SULTAN
```

### Untuk AGIL (11 Footage | `B090` s/d `B100`):
```bash
python download_envato.py --editor AGIL
```

### Opsi Parameter Tambahan:
* Mengunduh semua footage sekaligus:
  ```bash
  python download_envato.py --editor ALL
  ```
* Menentukan folder penyimpanan kustom:
  ```bash
  python download_envato.py --editor SULTAN --out-dir "D:/ALUX/FOOTAGE/SULTAN"
  ```
* Uji coba download 3 slot pertama saja:
  ```bash
  python download_envato.py --editor SULTAN --limit 3
  ```

---

## 3. Fitur Cerdas Skrip Automasi

* **Filter Otomatis:** Menambahkan parameter `filter.video_resolutions=1080p+(Full+HD)` dan `filter.orientation=Horizontal` ke Envato.
* **Anti-CGI / Anti-3D:** Secara otomatis menyaring hasil animasi 3D, kartun, renderan loop, atau motion graphic, dan hanya memilih footage *live-action riil*.
* **Format Penamaan Standar ALUX:** File hasil unduh langsung di-rename rapi sesuai format cue sheet:
  * Format: `[KODE]_[slug_deskripsi].[ext]`
  * Contoh: `B032_poultry_processing_plant_workers.mp4`
* **Resume Otomatis (Progress Tracker):** Jika koneksi terputus atau proses dihentikan, skrip mencatat file yang sudah selesai di `progress_<editor>.json`. Saat dijalankan ulang, slot yang sudah terunduh akan otomatis di-**SKIP**.
* **Ekstraksi Otomatis:** Jika Envato mengunduh dalam bentuk file ZIP, skrip otomatis mengekstrak file video di dalamnya (`.mp4` / `.mov`).

---

## 4. Cara 2: Menjalankan via Hermes Chat (Panel Premiere Pro / Terminal)

Jika menggunakan Hermes Agent di aplikasi desktop atau panel **Hermes Chat** di Premiere Pro:

### Prompt Eksekusi Siap Pakai di Hermes Chat:
```text
Tolong unduh otomatis seluruh footage Envato untuk bagian <REPI/SULTAN/AGIL> dari cue sheet online https://zlfkraffandi-dev.github.io/alux-kit-ep006/:
1. Buka Chrome CDP port 9222 (yang sudah login Envato).
2. Filter hanya footage 1080p Full HD dan Landscape (Horizontal).
3. Skip footage jika terdeteksi 3D/CGI/animasi.
4. Simpan ke folder 'FOOTAGE/<NAMA>/' dengan format '[KODE]_[slug].mp4'.
5. Laporkan total file yang berhasil diunduh dan durasinya!
```

---

## 5. Cara 3: Alur Manual Terpandu (Bila Tanpa Remote Debugging)

Jika editor tidak ingin memakai remote port Chrome, mereka tetap bisa mengunduh manual melalui dashboard online:

1. Buka dashboard cue sheet: https://zlfkraffandi-dev.github.io/alux-kit-ep006/
2. Klik tombol nama kalian (**REPI** / **SULTAN** / **AGIL**).
3. Klik tombol **Cari** pada slot footage:
   * Tombol ini langsung membuka pencarian Envato yang sudah difilter 1080p.
4. Klik **Download (1080P)** pada kartu video live-action pilihan.
5. Gunakan script rename batch atau AI Assistant untuk merapikan nama file ke folder kerja.
