<script>
    import hv_mk2 from "../../../../images/learning/pengantar-ikti/hv-mk2.webp";
    import alanturing from "../../../../images/learning/pengantar-ikti/alanturing.webp";
    import computerflowchart from "../../../../images/learning/pengantar-ikti/computerflowchart.webp";
    import problemsolving from "../../../../images/learning/pengantar-ikti/problemsolving.webp";
    import etikadigital from "../../../../images/learning/pengantar-ikti/etikadigital.jpeg";
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
            Logika dan problem solving sebenernya bukan cuma soal programming.
            Setiap hari kita pasti ngadepin masalah—dari yang simpel kayak 
            "mana jalur tercepat ke kampus" sampe yang kompleks kayak 
            "budget bulanan abis kemana aja". Cara kita nanganin itu, 
            bisa pake pendekatan yang sama kayak komputer.
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
            <b>Decomposition</b> — mecah masalah gede jadi bagian kecil yang 
            lebih gampang diurus. Misalnya lo mau bikin tugas akhir, daripada 
            mikir "gila gede banget nih tugas", lo pecah jadi: cari topik, 
            baca referensi, nulis bab 1, bab 2, dst.
        </p>
        <p>
            <b>Pattern Recognition</b> — nyari pola atau kemiripan dari masalah 
            yang pernah kita hadapi sebelumnya. Kalo lo pernah nyelesain soal 
            matematika tipe X, pas liat soal mirip, lo tinggal pake cara yang 
            sama.
        </p>
        <p>
            <b>Abstraction</b> — milah mana info yang penting, mana yang bisa 
            diabaikan. Pas lo nyari kost, lo ga perlu mikirin warna tembok atau 
            merek kulkasnya—yang penting harga, lokasi, dan fasilitas utama.
        </p>
        <p>
            <b>Algorithm Design</b> — nyusun langkah-langkah penyelesaian secara 
            berurutan dan logis. Kayak resep masak: ikutin step by step, dari 
            awal sampe jadi.
        </p>
        <p>
            Contoh gampang: nyiapin sarapan. Kita pecah tugasnya 
            (dekomposisi): ambil piring, ambil roti, olesin selai, seduh kopi. 
            Kita sadar pola: tiap pagi ngelakuin hal yang sama. Kita filter 
            info: ga perlu mikir warna piring atau merek kopi. Terakhir kita 
            urutin langkahnya biar efisien—misalnya seduh kopi dulu biar sambil 
            nunggu kita siapin roti. Itu computational thinking tanpa komputer 
            sama sekali.
        </p>
        <p>
            Intinya, logika dan problem solving adalah fondasi dari Ilmu 
            Komputer, tapi berguna di bidang apapun. Belajar cara ini bikin lo 
            lebih terstruktur dalam ngambil keputusan dan nyelesain masalah, 
            baik di coding maupun di kehidupan sehari-hari.
        </p>
        </div>

        <div id="sub-4">
            <h3>Digital ethics</h3>
        <div class="images">
            <img src={etikadigital} alt="Digital Ethics" />
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
            <b>Digital footprint.</b> Setiap klik, like, komentar, dan search 
            lo meninggalkan jejak digital. Perusahaan kayak Google dan Facebook 
            pake itu buat nargetin iklan, tapi bisa juga dipake orang jahat 
            kalo lo ga hati-hati.
        </p>
        <p>
            <b>Plagiarisme dan hak cipta.</b> Internet tuh gudangnya informasi, 
            tapi bukan berarti lo bisa copy-paste seenaknya. Kalo mau pake karya 
            orang, cantumin sumber. Kalo lo bikin karya sendiri, lo juga berhak 
            dilindungi hak ciptanya.
        </p>
        <p>
            <b>Etika online dan cyberbullying.</b> Di balik layar, lo ngobrol 
            sama manusia beneran. Jangan ngatain, ngebully, atau nyebarin hoax. 
            Screen lo mungkin melindungi identitas lo, tapi dampak ke orang 
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
        font-family: "Jetbrains Mono";
        transition: all 0.25s linear;
        /* outline: 1px solid red; */
    }
</style>
