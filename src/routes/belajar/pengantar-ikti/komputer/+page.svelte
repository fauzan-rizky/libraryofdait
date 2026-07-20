<script>
    import Navbar from "../../../../components/navbar.svelte";
    import SidebarIkti from "../sidebar-ikti.svelte";
    import "../../../../styles/materials.css";
    import hv_mk2 from "../../../../images/learning/pengantar-ikti/hv-mk2.webp";
    import alanturing from "../../../../images/learning/pengantar-ikti/alanturing.webp";
    
</script>

<Navbar />
<div class="materialEntry">
    <SidebarIkti />

    <div class="material">
        <h3 id="materi-1" class="materi-title">Komputer</h3>
        <div class="images">
            <img src={hv_mk2} alt="Harvard Mark II" />
            <p class="image-description">Komputer Harvard Mark II</p>
        </div>
        <h3 id="materi-1-sub1">
            Sejarah komputer
        </h3>
        
        <p>Komputer modern pada awalnya diciptakan oleh Alan Turing, matematikawan jenius yang pada saat itu berfikir bagaimana caranya
            memecahkan kode sandi Enigma milik Jerman pada saat perang dunia ke-2, beliau lalu berhasil menciptakan salah satu 
            bentuk komputer pertama yang bernama <i>Turing Machine</i>, berfungsi untuk memecah kode Enigma tersebut dan menjadi
            fondasi utama Ilmu Komputer modern. Sayangnya Alan Turing meninggal diduga karena keracunan sianida setelah ditemukan 
            sudah tidak bernyawa dikamarnya dengan sebuah apel yang sudah dimakan sebagian, 
            hal ini juga diabadikan menjadi salah satu logo perusahaan teknologi ternama. 
        </p>
        <div class="images">
            <img src={alanturing} alt="Alan Turing" />
            <p class="image-description">Alan Turing dan mesin buatannya</p>
        </div>
        <p>
            Setelah <i>Turing Machine</i> tersebut, komputer mulai berevolusi secara pesat mulai dari <i>Harvard Mark I</i>, 
            sebuah komputer besar hingga sekarang yang sudah semakin hari semakin ringkas bentuknya seperti 
            handphone dan chip <i>semiconductor</i> yang sudah mencapai ukuran nanometer transistornya 
        </p>
    </div>
</div>

<style>
    * {
        font-family: "Jetbrains Mono";
        transition: all 0.25s linear;
        /* outline: 1px solid red; */
    }
</style>
