# Contributing to Library of DAIT

Terima kasih udah mau berkontribusi! Dokumen ini berisi panduan singkat tentang apa yang bisa dan nggak bisa di-contribute.

## Cara Contribute

1. Fork repo ini
2. Buat branch baru: `git checkout -b feat/apa-yang-lu-buat`
3. Commit perubahan
4. Push ke fork lu: `git push origin feat/apa-yang-lu-buat`
5. Buka Pull Request ke repo ini

## Yang Bisa Di-contribute ✅

### Konten Belajar
- **Modul baru** — Tambah materi pembelajaran baru di `src/routes/belajar/`
- **Perbaikan konten** — Typo, salah nulis, atau penjelasan yang kurang jelas di halaman belajar
- **Gambar/ilustrasi** — Tambah ilustrasi pendukung di `src/images/learning/`
- **Referensi & link** — Tambah link bermanfaat yang relevan
- **Rewording** - Perbaikan atau penambahan kata supaya bisa lebih gampang dimengerti atau lebih jelas

### Teknis
- **Bug fix** — Error di komponen (navbar, sidebar, dll)
- **Improve UI/UX** — Bikin navigasi lebih enak, transisi lebih mulus, mobile lebih responsif
- **Aksesibilitas** — Perbaikan aria labels, keyboard navigation, dll
- **Performa** — Optimasi gambar, lazy loading, dll

### Lainnya
- **Ide baru** — Mau usul fitur? Buka issue dulu, diskusiin
- **Test** — Bantu tes di berbagai browser/device terus lapor masalah
- **Design** - Khusus FrontEnd, untuk pengubahan design diskusikan terlebih dahulu

## Yang Jangan Di-contribute ❌

- **Hapus konten existing** — Kecuali udah didiskusiin lewat issue
- **Ubah warna/font utama** — Design system (`#00fff7`, `#fe0ab9`, font stack) udah tetap
- **Ubah struktur routing** — Struktur `src/routes/` udah tetap, jangan diotak-atik
- **Ganti package manager** — Pake Bun atau npm aja. Jangan nambah yarn/pnpm lockfile
- **Ubah pipeline gambar** — Semua gambar harus `.webp`, proses konversi via `scripts/webp-convert.py`
- **Push langsung ke `main`** — Semua perubahan lewat PR, minimal 1 review

## Development

```bash
bun install    # atau npm install
bun run dev    # atau npm run dev
```

Pastikan `bun run build` nggak error sebelum bikin PR.

## Struktur Folder (Sekilas)

```
src/
├── routes/          → Halaman & routing
├── components/      → Komponen Svelte
├── images/          → Gambar (wajib .webp)
├── styles/          → CSS global
└── lib/assets/      → favicon & asset kecil
```

## Punya Pertanyaan?

Buka aja issue atau tanya di diskusi.
