# Library of DAIT

## Tech Stack
- Svelte 5 (runes mode: `$state`, `$props`, `$effect`, `$derived`)
- SvelteKit 2
- Vite

## Commands
- `npm run dev` — start dev server
- `npm run build` — build for production
- `npm run preview` — preview production build

## Project Structure
- `src/routes/` — halaman (SvelteKit routing)
  - `+page.svelte` — homepage
  - `belajar/` — halaman belajar
  - `tentang/` — halaman tentang
- `src/components/` — komponen (navbar, sidebar, daitanimate)
- `src/styles/` — CSS global
  - `text.css` — responsive typography (clamp)
  - `materials.css` — styling konten belajar
  - `global.css` — global reset
- `src/lib/assets/` — gambar & favicon
- `static/` — file statis

## Styling Conventions
- Font utama: `"Rajdhani"` (navbar, homepage, belajar menu)
- Font mono: `"Jetbrains Mono"` — dulunya dipake, sekarang udah diganti Rajdhani (kecuali di beberapa code block)
- Typography: `clamp()` approach (mobile-first, via `text.css`)
- Pure CSS — no SCSS, all scoped `<style>` blocks

## Svelte 5 Conventions
- Use runes (`$state`, `$props`, `$effect`, `$derived`) — no `export let` or `$:`
- Navigation via `$app/stores` (`page`, `navigating`)
- Transitions from `svelte/transition`
