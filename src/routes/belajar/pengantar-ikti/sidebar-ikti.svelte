<script>
import Sidebar from "../../../components/sidebar.svelte";

let { open = false, onClose = () => {} } = $props();

let sidebarSections = [
    {
        title: "Pengenalan",
        href: "/belajar/pengantar-ikti/pengenalan/#materi-1",
        items: [
            { label: "Apa itu Ilmu Komputer dan Teknik Informatika", href: "/belajar/pengantar-ikti/pengenalan/#sub-1" },
            { label: "Prospek bidang dan karir", href: "/belajar/pengantar-ikti/pengenalan/#sub-2" },
        ],
    },
    {
        title: "Komputer",
        href: "/belajar/pengantar-ikti/komputer/#materi-1",
        items: [
            { label: "Sejarah komputer", href: "/belajar/pengantar-ikti/komputer/#sub-1" },
            { label: "Cara kerja komputer", href: "/belajar/pengantar-ikti/komputer/#sub-2" },
            { label: "Logika dan problem solving", href: "/belajar/pengantar-ikti/komputer/#sub-3" },
            { label: "Digital ethics", href: "/belajar/pengantar-ikti/komputer/#sub-4" },
        ],
    },
];
</script>
<Sidebar {open} {onClose} sections={sidebarSections} />

