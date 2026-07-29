<script>
    import hv_mk2 from "../../../../images/learning/pengantar-ikti/hv-mk2.webp";
    import alanturing from "../../../../images/learning/pengantar-ikti/alanturing.webp";
    import computerflowchart from "../../../../images/learning/pengantar-ikti/computerflowchart.webp";
    import problemsolving from "../../../../images/learning/pengantar-ikti/problemsolving.webp";
    import etikadigital from "../../../../images/learning/pengantar-ikti/etikadigital.webp";
</script>

    <div class="material">
        <div id="materi-1">
            <h3 class="materi-title">Komputer</h3>
            <div class="images">
                <img src={hv_mk2} alt="Harvard Mark II" />
                <p class="image-description">Komputer Harvard Mark II</p>
            </div>
        </div>

        <div id="sub-1">
            <h3>Sejarah komputer</h3>

            <p>
                Komputer modern pada awalnya diciptakan oleh Alan Turing,
                matematikawan jenius yang pada saat itu berfikir bagaimana caranya
                memecahkan kode sandi Enigma milik Jerman pada saat perang dunia
                ke-2, beliau lalu berhasil menciptakan salah satu bentuk komputer
                pertama yang bernama <i>Turing Machine</i>, berfungsi untuk memecah
                kode Enigma tersebut dan menjadi fondasi utama Ilmu Komputer modern.
                Sayangnya Alan Turing meninggal diduga karena keracunan sianida
                setelah ditemukan sudah tidak bernyawa dikamarnya dengan sebuah apel
                yang sudah dimakan sebagian, hal ini juga diabadikan menjadi salah
                satu logo perusahaan teknologi ternama.
            </p>
            <div class="images">
                <img src={alanturing} alt="Alan Turing" />
                <p class="image-description">Alan Turing dan mesin buatannya</p>
            </div>
            <p>
                Setelah <i>Turing Machine</i> tersebut, komputer mulai berevolusi
                secara pesat mulai dari <i>Harvard Mark I</i>, sebuah komputer besar
                hingga sekarang yang sudah semakin hari semakin ringkas bentuknya
                seperti handphone dan chip <i>semiconductor</i> yang sudah mencapai ukuran
                nanometer transistornya
            </p>
        </div>

        <div id="sub-2">
            <h3>Cara kerja komputer</h3>
        
        <p>
            Komputer bisa kita analogikan disini sebagai sebuah restoran. Setiap 
            komponen punya tugas spesifik yang saling terhubung, mirip kayak 
            bagian-bagian di dapur.
        </p>
        <div class="images">
            <img src={computerflowchart} alt="Computer Workflow" />
            <p class="image-description">Computer Workflow</p>
        </div>
        <p>
            <b>Input</b> (keyboard & mouse) berperan sebagai pelanggan yang 
            memberikan pesanan. Instruksi dari pengguna ini kemudian dikirim ke 
            <b>CPU</b> (Central Processing Unit) yang bertindak sebagai koki 
            utama—bertugas memproses semua instruksi, melakukan perhitungan, dan 
            mengambil keputusan.
        </p>
        <p>
            Dalam proses "memasak" tersebut, CPU membutuhkan tempat penyimpanan 
            sementara yang cepat, yaitu <b>RAM</b> (Random Access Memory). RAM 
            bisa dianalogikan sebagai meja dapur tempat koki menyimpan 
            bahan-bahan yang sedang diolah. Namun RAM bersifat 
            <i><a href="https://www.oxfordlearnersdictionaries.com/definition/english/volatile" target="_blank">volatile</a></i>—jika 
            listrik padam, datanya hilang. Karena itu komputer juga punya 
            <b>Storage</b> (HDD atau SSD), yang ibarat kulkas dan lemari dapur: 
            tempat penyimpanan jangka panjang meskipun sedang tidak dipakai.
        </p>
        <p>
            Selain itu ada <b>GPU</b> (Graphics Processing Unit), semacam chef 
            spesialis yang fokus pada tugas tertentu. CPU bisa melakukan segalanya, 
            tetapi GPU dirancang khusus untuk menangani ribuan perhitungan sederhana 
            secara paralel—sangat berguna untuk gaming, rendering video, dan 
            pelatihan AI.
        </p>
        <p>
            Alur kerja komputer secara sederhana dapat digambarkan sebagai berikut:
            <b>Input → CPU ↔ (RAM / Storage) → Output</b>. Instruksi dari perangkat 
            input masuk ke CPU, CPU mengambil atau menyimpan data di RAM atau 
            Storage sesuai kebutuhan, lalu hasilnya dikeluarkan melalui perangkat 
            output seperti monitor atau printer—semua dalam hitungan milidetik.
        </p>
        </div>

        <div id="sub-3">
            <h3>Logika dan problem solving</h3>
        
        <p>
            Logika dan <i>problem solving</i> sebenarnya bukan hanya tentang
            <i>programming</i>. Setiap hari kita pasti menghadapi
            masalah—dari yang sederhana seperti "mana jalur tercepat ke kampus"
            sampai yang kompleks seperti "pengeluaran bulanan membengkak".
            Cara kita menangani hal tersebut bisa menggunakan pendekatan yang
            sama seperti komputer.
        </p>
        <div class="images">
            <img src={problemsolving} alt="Problem Solving" />
            <p class="image-description">Problem Solving</p>
        </div>
        <p>
            Cara berpikir ala komputer ini disebut <b>computational thinking</b>,
            terdiri dari 4 langkah:
        </p>
        <p>
            <b>Decomposition</b> — memecah masalah besar menjadi bagian-bagian
            kecil yang lebih mudah diurus. Misalnya ketika mengerjakan tugas
            akhir, daripada merasa kewalahan dengan besarnya tugas tersebut,
            kita bisa memecahnya menjadi: cari topik, baca referensi, tulis bab
            1, bab 2, dan seterusnya.
        </p>
        <p>
            <b>Pattern Recognition</b> — mencari pola atau kemiripan dari
            masalah yang pernah dihadapi sebelumnya. Jika pernah menyelesaikan
            soal matematika tipe tertentu, saat melihat soal yang mirip, kita
            tinggal menggunakan cara yang sama.
        </p>
        <p>
            <b>Abstraction</b> — memilah informasi mana yang penting dan mana
            yang bisa diabaikan. Saat mencari kost, kita tidak perlu memikirkan
            warna tembok atau merek kulkasnya—yang terpenting adalah harga,
            lokasi, dan fasilitas utama.
        </p>
        <p>
            <b>Algorithm Design</b> — menyusun langkah-langkah penyelesaian
            secara berurutan dan logis. Seperti resep memasak: ikuti langkah
            demi langkah, dari awal hingga selesai.
        </p>
        <p>
            Contoh sederhana: menyiapkan sarapan. Kita pecah tugasnya
            (dekomposisi): ambil piring, ambil roti, oleskan selai, seduh kopi.
            Kita sadari polanya: setiap pagi melakukan hal yang sama. Kita
            saring informasi: tidak perlu memikirkan warna piring atau merek
            kopi. Terakhir kita urutkan langkah-langkahnya agar lebih
            efisien—misalnya seduh kopi terlebih dahulu sambil menunggu kita
            menyiapkan roti. Itulah <i>computational thinking</i> tanpa
            komputer sama sekali.
        </p>
        <p>
            Intinya, logika dan <i>problem solving</i> adalah fondasi dari
            Ilmu Komputer, namun berguna di bidang apapun. Mempelajari cara
            berpikir ini membuat kita lebih terstruktur dalam mengambil
            keputusan dan menyelesaikan masalah, baik dalam <i>coding</i>
            maupun dalam kehidupan sehari-hari.
        </p>
        </div>

        <div id="sub-4">
            <h3>Etika Digital</h3>
        <div class="images">
            <img src={etikadigital} alt="Etika Digital" />
            <p class="image-description">Etika Digital</p>
        </div>
        <p>
            Punya komputer atau akses internet bukan berarti kita bebas 
            ngelakuin apa aja. Sama kayak di dunia nyata, di dunia digital 
            juga ada aturan dan etika yang harus dijaga.
        </p>
        <p>
            <b>Privacy dan data pribadi.</b> Jangan sembarangan share data 
            pribadi kayak alamat, nomor telepon, atau password di internet. 
            Yang udah keupload, susah banget ditarik balik.
        </p>
        <p>
            <b>Digital footprint.</b>             Setiap klik, like, komentar, dan search 
            yang kita lakukan meninggalkan jejak digital. Perusahaan kayak Google dan Facebook 
            pake itu buat nargetin iklan, tapi bisa juga dipake orang jahat 
            kalo kita ga hati-hati.
        </p>
        <p>
            <b>Plagiarisme dan hak cipta.</b>             Internet tuh gudangnya informasi, 
            tapi bukan berarti kita bisa copy-paste seenaknya. Kalo mau pake karya 
            orang, cantumin sumber. Kalo kita bikin karya sendiri, kita juga berhak 
            dilindungi hak ciptanya.
        </p>
        <p>
            <b>Etika online dan cyberbullying.</b> Di balik layar, kita ngobrol 
            sama manusia beneran. Jangan ngatain, ngebully, atau nyebarin hoax. 
            Screen kita mungkin melindungi identitas kita, tapi dampak ke orang 
            lain itu nyata.
        </p>
        <p>
            <b>Digital wellbeing.</b> Komputer dan internet itu alat, bukan 
            tujuan. Jangan sampe scroll medsos 8 jam sehari sampe lupa makan 
            dan mandi. Atur screen time, istirahat, dan inget bahwa dunia nyata 
            juga perlu dijelajahi.
        </p>
        </div>
    </div>

<style>
    * {
        font-family: "Rajdhani";
        /* outline: 1px solid red; */
    }

    a {
        transition: all 0.25s linear;
    }
</style>
