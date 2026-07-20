<script>
import Sidebar from "../../../components/sidebar.svelte";

let sidebarSections = $state([
        {
            title: "Pengenalan",
            href: "./pengenalan/#materi-1",
            items: [
                { label: "Apa itu Ilmu Komputer dan Teknik Informatika", href: "./pengenalan/#materi-1-sub-1" },
                { label: "Prospek bidang dan karir", href: "./pengenalan/#materi-1-sub-2" },
            ],
        },
        {
            title: "Komputer",
            href: "./komputer/#materi-1",
            items: [
                { label: "Sejarah komputer" },
                { label: "Cara kerja komputer" },
                { label: "Logika dan problem solving" },
                { label: "Digital ethics" },
            ],
        },
    ]);
</script>
<Sidebar sections={sidebarSections} />

