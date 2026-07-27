<script>
import Sidebar from "../../../components/sidebar.svelte";

let { open = false, onClose = () => {} } = $props();

let sidebarSections = [
    {
        title: "Dasar Pemrograman",
        href: "/belajar/mulprog/ddp/#materi-1",
        items: [
            { label: "Pemrograman dan coding", href: "/belajar/mulprog/ddp/#sub-1" },
            { label: "Bahasa pemrograman", href: "/belajar/mulprog/ddp/#sub-2" },
            { label: "Istilah-istilah di pemrograman", href: "/belajar/mulprog/ddp/#sub-3", children: [
                { label: "Syntax", href: "/belajar/mulprog/ddp/#sub-3-1" },
                { label: "High-level dan Low-level", href: "/belajar/mulprog/ddp/#sub-3-2" },
                { label: "Compiler dan Interpreter", href: "/belajar/mulprog/ddp/#sub-3-3" },
                { label: "Bug dan Debugging", href: "/belajar/mulprog/ddp/#sub-3-4" },
                { label: "IDE dan Code Editor", href: "/belajar/mulprog/ddp/#sub-3-5" }] },
            { label: "GitHub", href: "/belajar/mulprog/ddp/#sub-4" },
        ],
    },
    {
        title: "Setup",
        href: "/belajar/mulprog/setup/#materi-1",
        items: [
            { label: "Prasyarat", href: "/belajar/mulprog/setup/#sub-1" },
            { label: "Package manager", href: "/belajar/mulprog/setup/#sub-2" },
            { label: "Konfigurasi Github", href: "/belajar/mulprog/setup/#sub-3", children: [
                { label: "Akun GitHub", href: "/belajar/mulprog/setup/#sub-3-1" },
                { label: "Install Git", href: "/belajar/mulprog/setup/#sub-3-2" },
            ] },
            { label: "Install VSCode", href: "/belajar/mulprog/setup/#sub-4" },
            { label: "Install Python", href: "/belajar/mulprog/setup/#sub-5"}
        ],
    },
    {
        title: "Program Pertama",
        href: "/belajar/mulprog/progpel/#materi-1",
        items: [],
    },
];
</script>
<Sidebar {open} {onClose} sections={sidebarSections} />
