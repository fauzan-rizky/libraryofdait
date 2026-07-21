# AGENTS.md — Library of DAIT

## Identitas

- Panggil user: **Ojan**
- Panggilan agent: **DS**

## Stack

- SvelteKit 2 + Svelte 5 runes (`$state`, `$props`, `$derived`)
- Vite 8, adapter-auto
- **Bun** (bukan npm) untuk semua command
- No TypeScript, no Tailwind — CSS murni

## Commands

```sh
bun run dev       # dev server
bun run build     # build production
```

## Struktur

- `src/routes/` — file-based routing
- `src/components/` — komponen global (Navbar, Sidebar)
- `src/styles/` — CSS global (`global.css`, `materials.css`)
- `src/images/learning/pengantar-ikti/` — gambar konten belajar

Layout bertingkat: `+layout.svelte` di folder route otomatis bungkus semua page. Layout di `belajar/pengantar-ikti/+layout.svelte` berisi Navbar + Sidebar.

## Konvensi Kode

- **CSS class: kebab-case** (`full-screen-container`, `material-entry`, dll)
- **Responsive:** root `font-size: clamp(16px, 0.833vw, 32px)`, padding/margin pake `rem`
- **Anchor ID:** halaman pake `#materi-1` (judul), sub-bab pake `#sub-1`, `#sub-2`, dst
- **Font:** `"Jetbrains Mono"` di halaman materi, `"Rajdhani"` di beranda, `"Jersey 25"` di navbar

## Gaya Konten

Penjelasan IT dengan gaya "bahasa bayi" — informal, analogi sehari-hari (restoran, dapur), istilah teknis ditebalkan `<b>`.

## Sidebar

Komponen reusable di `src/components/sidebar.svelte`. Menerima prop `sections` via `$props()`:
- Format: `{ title, href, items: [{ label, href? }] }`
- Data sidebar didefinisikan di `belajar/pengantar-ikti/sidebar-ikti.svelte`
