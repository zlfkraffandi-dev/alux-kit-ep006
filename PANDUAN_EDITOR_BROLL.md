# SOP & Panduan Editor: Sourcing & Penempatan Aset (EP006 Part 1)

Panduan kerja untuk editor (**Repi, Sultan, Agil**) dalam mencari footage, mengunduh aset, hingga menempatkannya di timeline Adobe Premiere Pro sesuai file cue sheet `EP006_Part1_BROLL_EDITOR.html`.

---

## 1. Pembagian Tugas & Cakupan File (Part 1)

Buka file **`EP006_Part1_BROLL_EDITOR.html`** di browser Chrome / Edge. Klik tombol nama kalian di toolbar atas:

| Editor | Scene / Chapter | Cakupan |
|---|---|---|
| **REPI** | `S01` Cold Open, `S02` Ch 1, `S03` Ch 2 | 72 baris (31 Footage, 3 Archive, 33 Graphic, 5 GeoLayer) |
| **SULTAN** | `S04` Ch 3, `S05` Ch 4, `S06` Ch 5 | 107 baris (58 Footage, 3 Archive, 42 Graphic, 4 GeoLayer) |
| **AGIL** | `S07` Ch 6 *(S08–S09 menyusul di Part 2)* | 19 baris (11 Footage, 0 Archive, 8 Graphic, 0 GeoLayer) |

*Catatan: Part 2 (S08–S13) menyusul setelah audio dan SRT-nya jadi, dengan file HTML terpisah. Total Part 1: 198 baris = 100 Footage (V5) + 6 Archive (V6) + 83 Graphic (V7) + 9 GeoLayer (V8).*

---

## 2. Mengenal 3 Kategori Isian (Marking Timeline)

Setiap baris di HTML dan timeline Premiere ditandai dengan garis warna & badge:

1. <span style="color:#10b981;font-weight:bold;">[FOOTAGE]</span> (Kode `B001` s/d `B100` | Garis Hijau)
   * **Sumber:** Stock video komersial dari **Envato Elements**.
   * **Tujuan Timeline:** Marking di track **`V5`** (Konten diletakkan di track **`V1` B-ROLL**). Letakkan klip hasil download tepat di bawah marking (lihat Bagian 4).
   * **Cara:** Klik tombol **Cari** di HTML untuk langsung membuka hasil pencarian Envato, atau klik **Copy** untuk menyalin keyword.

2. <span style="color:#6366f1;font-weight:bold;">[GRAPHIC]</span> (Kode `EP006-001` s/d `083` | Garis Ungu)
   * **Sumber:** Desain dari **Figma**, render **MOGRT** (After Effects).
   * **Tujuan Timeline:** Marking di track **`V7`** (Konten diletakkan di track **`V3` GRAPHIC**). Grafis dirender dari Figma/GeoLayers, bukan dicari di stock.
   * **Cara:** Cek kolom *Konteks & arahan visual*. Jika bertanda `GeoLayers 3`, siapkan animasi peta sesuai koordinat GPS yang tertera. Jika ada link artikel berita (BBC/CNN), klik link untuk referensi screenshot koran/web.

3. <span style="color:#f59e0b;font-weight:bold;">[ARCHIVE]</span> (Kode `A001` s/d `A006` | Garis Kuning)
   * **Sumber:** Dokumen sejarah, foto arsip, cuplikan berita lama, atau Wikimedia Commons.
   * **Tujuan Timeline:** Marking di track **`V6`** (Konten diletakkan di track **`V2` ARCHIEVE**). Letakkan arsip tepat di bawah marking (lihat Bagian 4).
   * **Cara:** Lihat keterangan di kolom *Sumber/Aset* (misal: *National Geographic*, *History.com*, *USDA History*), cari footage/foto arsip yang relevan.

4. <span style="color:#06b6d4;font-weight:bold;">[GEOLAYER]</span> (Track **`V8`**)
   * **Sumber:** Animasi peta 3D After Effects via plugin **GeoLayers 3**.
   * **Tujuan Timeline:** Marking penanda durasi di track **`V8`** (Konten diletakkan di track **`V4` GEOLAYER**).
   * **Cara:** Cek arahan di kolom *Konteks & arahan visual* file HTML. Wajib input koordinat Latitude & Longitude (bukan nama kota) serta ikuti setup zoom & pitch kamera AE yang tertera.

---

## 3. Standar Unduh (Download Rules)

* **Resolusi Utama:** Pilih resolusi **Full HD (1080p)** saat download dari Envato untuk efisiensi penyimpanan.
* **Frame Rate:** Utamakan **24 fps** (sesuai sequence Premiere 24.0 fps). Jika dapat 25/30/60 fps, sesuaikan di Interpret Footage bila perlu.
* **Format Penamaan File:** Wajib sertakan KODE di depan nama file agar mudah dicari:
  * Contoh: `B001_refrigerated_truck_dock.mp4`
  * Contoh: `A001_chicken_of_tomorrow_1948.mp4`

---

## 4. Aturan Penempatan di Adobe Premiere Pro

Marking sudah terpasang di sequence (A1/A2 voice over terkunci, jangan diubah):
Struktur Track Sequence Premiere Pro (Update Master 12 Track):
```text
[V12] Video 12                 <- LOGO PLACEMENT VIDEO.png (Watermark branding)
[V10] SOURCE                   <- Master footage / talking head
[V9]  CHAPTER                  <- Penanda babak (jangan digeser)
[V8]  MARKING GEOLAYER         <- Penanda durasi animasi peta GeoLayers 3 (After Effects)
[V7]  MARKING GRAPHIC          <- Penanda durasi motion graphic Figma / MOGRT
[V6]  MARKING ARCHIEVE         <- Penanda durasi foto / dokumen arsip sejarah
[V5]  MARKING ENVATO           <- Penanda durasi stock video Envato Elements
-------------------------------------------------------------------
[V4]  GEOLAYER                 <- Tempat meletakkan render animasi peta GeoLayers 3
[V3]  GRAPHIC                  <- Tempat meletakkan render motion graphic Figma / MOGRT
[V2]  ARCHIEVE                 <- Tempat meletakkan foto / video arsip sejarah
[V1]  B-ROLL                   <- Tempat meletakkan stock video Envato Elements
-------------------------------------------------------------------
[A1]  VOICE OVER               <- TERKUNCI (MASTER VO - JANGAN DIUBAH)
```
Letakkan klip hasil download dan render pada layer konten (V1 B-Roll, V2 Archieve, V3 Graphic, V4 Geolayer) tepat di bawah batas marking masing-masing (V5 Envato, V6 Archieve, V7 Graphic, V8 Geolayer).

### Aturan Wajib Editing:
1. **Snap Sesuai Marking:**
   * Aktifkan tombol **Snap (`S`)** di timeline Premiere.
   * Panjang klip harus pas dari awal sampai akhir batas marking (`V4`/`V5`). Jangan ada gap / lubang hitam.
2. **Zero Vertical Stacking (Dilarang Menumpuk):**
   * Pada satu waktu hanya ada satu jenis aset. Marking tidak saling tumpang tindih: slot GRAPHIC berarti tidak ada footage atau arsip di waktu itu, begitu juga sebaliknya.
   * Jangan menaruh klip di durasi marking milik kategori lain.
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

