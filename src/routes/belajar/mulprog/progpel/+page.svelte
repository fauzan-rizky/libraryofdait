<script>
    import vscodenf from "../../../../images/learning/mulprog/vscodenf.png";
    import vscodecp from "../../../../images/learning/mulprog/newfilecp.png";
    import openfolder from "../../../../images/learning/mulprog/openfolder.png";
    import openterm from "../../../../images/learning/mulprog/openterminal.png";
    import executepython from "../../../../images/learning/mulprog/executepython.png";
    import ghauthlogin from "../../../../images/learning/mulprog/ghauthlogin.png";
    import ghauthsuccess from "../../../../images/learning/mulprog/ghauthsuccess.png";
</script>

<div class="material">
    <div id="materi-1">
        <h3 class="materi-title">Program Pertama</h3>
    </div>
    <div id="sub-1">
        <h3>Hello, world!</h3>
        <p>
            <code>Hello, world!</code> adalah sebuah kata yang sering terdengar
            dikalangan komunitas IT atau di dunia komputer
            <br />
            pada dasarnya <code>Hello, world!</code> sendiri merupakan ekspresi
            atau <i>script</i> sederhana sebagai contoh sintaks dan latihan awal
            untuk programmer baru, bisa juga untuk ngecek apakah
            <b><i>SDK</i></b> sudah terinstal di sistem
        </p>
        <p>
            Pertama tama buka VSCode atau Codespaces seperti di step <b
                >Install VSCode</b
            > di halaman sebelumnya,biasanya akan muncul tab Welcome
        </p>
        <p>
            *Khusus di <b>PC</b>, kalian perlu untuk membuat folder project
            kalian dengan klik icon <b>directory</b> diatas icon <b>search</b>
            di pojok kiri atas, setelah itu windows explorer akan terbuka dan kalian
            bebas mau naruh project kalian dimana, biasanya orang menaruh di dokumen.
            Buat new folder lalu klik dan select folder, pastikan nama folder yang
            dipilih tepat dengan melihat pojok kiri bawah windows explorer
        </p>
        <div class="images images-tutorial">
            <img src={openfolder} alt="Vscode OF" />
        </div>
        <p>
            Lalu klik <b>new file</b> pada <b>tab welcome</b> atau klik icon new
            file di pojok kiri atas sebelah nama directory kalian
        </p>
        <!-- lalu klik <b>new file</b>, atau klik icon new file di pojok kiri atas disebelah nama directory -->
        <div class="images images-tutorial">
            <img src={vscodenf} alt="Vscode NF" />
        </div>
        <p>
            Alternatifnya kalian juga bisa pakai command palette dari
            VSCode/Codespaces itu sendiri dengan <code>CTRL+SHIFT+L</code> atau
            <code>F1</code>
            lalu ketik "new file" dan pilih yang <b>Create: new file...</b>
        </p>
        <div class="images images-tutorial">
            <img src={vscodecp} alt="Vscode NF" />
        </div>
        <p>
            ketik <code>hello.py</code> atau apapun asalkan filenya berarkhiran
            di <code>.py</code>,ini menandakan bahwa file tersebut merupakan
            script Python itu sendiri
        </p>
        <p>
            Setelah membuat filenya, klik filenya hingga muncul tampilan isi
            kosong dari filenya.
            <br />
            Lalu ketik <code>print("Hello, world!")</code> lengkap dengan tanda petik
            dua
        </p>
        <p>
            Lalu pakai command palette dan ketik <b>new terminal</b>, pilih yang
            <b>Terminal: Create New Terminal</b>, biasanya di codespaces udah
            muncul, tapi kalo ga bisa pake command ini
        </p>
        <div class="images images-tutorial">
            <img src={openterm} alt="Vscode Terminal" />
        </div>
        <p>
            Akan muncul <i>shell</i> atau lebih kerap disebut <b>cmd</b> atau
            <b>powershell</b>
            di windows di bagian bawah
            <br />
            ketik <code>python (nama script.py)</code>, kalau disini aku
            namainnya "hello.py" jadi aku bakal isi <code>python hello.py</code>
            <br />
            Enter lalu kata-kata <b>Hello, world!</b> akan muncul di terminal kalian
        </p>
        <div class="images images-tutorial">
            <img src={executepython} alt="Execute Python" />
        </div>
        <p>
            <b>*sfx kemenangan angry bird*</b>, selamat kalian sudah bisa
            "ngomong" sama komputer
            <br />
            <b>New Achievement: no longer larp larp sahur, but a prodigy</b>
        </p>
    </div>
    <div id="sub-2">
        <h3>Git</h3>
        <p>
            Setelah ini kita akan belajar tentang <b>Git</b>, dan bagaimana cara
            upload file atau folder ini ke <b>Github</b>
            sebagai project kalian atau sekedar kenang"an kalian
        </p>
        <p>
            Tapi sebelum itu kita perlu bedain antara <b>Git</b> dan
            <b>Github</b>
            dulu
        </p>
        <p>
            <b>Git</b> adalah program <b>VCS</b> atau
            <b>Version Control Sistem</b>
            atau di Bahasa Indonesianya
            <b>Sistem Kontrol Versi</b>, gunanya dari Git disini adalah untuk
            memanage file" project kita untuk nantinya kita upload ke
            <b>Github</b>
            sebagai update atau <i>rollback</i> yaitu kembali ke versi yang lama.
            Bisa juga digunakan untuk berkolaborasi dan menghubungkan antar tim programmer,
            misalkan A mengerjakan fitur X, B mengerjakan fitur Y dan C mengerjakan
            fitur Z. Mereka semua bisa mengerjakan tugasnya masing masing tanpa harus
            ribet mikirin tugas selain mereka
        </p>
        <p>
            <b>Github</b> adalah platform berbasis web dari Microsoft yang
            digunakan sebagai tempat penyimpanan repository dari <b>Git</b>
            sendiri, berbeda dengan Git, Github ini bisa dianalogikan sebagai GDrive
            dan juga Sosmed anak" IT, sementara <b>Git</b> adalah penghubung antara
            PC/Device kalian dengan Github
        </p>
        <div id="sub-2-1">
            <p><b>Github CLI</b></p>
            <p>
                Untuk menghubungkan <b>Git</b> dan <b>Github</b> kita akan
                menggunakan <b>Github CLI</b> atau <b>gh-cli</b>
                <br />
                *Khusus untuk PC, install dulu pakai scoop. Kalau di Codespaces sudah
                terinstall
            </p>
            <p>
                Buka terminal atau CMD, lalu ketik <code
                    >scoop install main/gh</code
                > dan tunggu hingga selesai
            </p>
            <p>
                *Khusus untuk di Mobile/Codespaces, silahkan ketik command <code>unset GITHUB_TOKEN</code> supaya
                bisa login di Codespaces
            </p>
            <p>
                Setelah selesai terinstall, ketik <code>gh auth login</code>
                <br />
                akan muncul beberapa pertanyaan, ikuti saja seperti dibawah
            </p>
            <div class="images images-tutorial">
                <img src={ghauthlogin} alt="GhAuth Login" />
            </div>
            <p>
                <b>copy</b> kode one time, lalu tekan enter, ini akan membuka
                browser lalu pilih akun github yang mau kalian link setelah itu
                <b>paste</b>
                kodenya dan continue. Lalu pilih <b>Authorize github</b>, dan
                akan di redirect ke terminal lalu muncul pesan
                <b>Authentication complete</b>
            </p>
            <div class="images images-tutorial">
                <img src={ghauthsuccess} alt="GhAuth Login" />
            </div>
            <p>Github CLI sudah menghubungkan Git dan Github</p>
        </div>
    </div>
    <div id="sub-3">
        <h3>Repository Pertamamu</h3>
        <p>
            Repository atau kerap disebut Repo bisa juga dianalogikan sebagai
            sebuah project di Github, didalamnya ada file" yang kalian upload
            dari saat kalian melakukan <code>git push</code> atau mengupload file
            tersebut ke Github. Dan nantinya Repo ini akan terdisplay di profile
            Github kalian (bisa diset ke privat juga kalau gamau di display)
        </p>
        <p>
            Siapkan terminal kalian dan arahkan ke folder project kalian, untuk
            di <b>PC</b> bisa langsung pake yang di VSCode, dan di <b>Mobile</b>
            bisa langsung pake di Codespacesnya juga. dua duanya otomatis akan ke
            set di folder yang kalian buka.
        </p>
        <p>
            0. <code>git init</code>
            <br />
            Sebelum kita lanjut, kita perlu menjalankan perintah ini untuk menginisialisasikan
            atau <i>initialize</i> folder tersebut sebagai
            <b>Git Repository</b>
        </p>
        <p>
            1. <code>git add .</code>
            <br />
            Ini adalah perintah <code>git</code> untuk menambah semua file di
            folder tersebut, titik atau <code>.</code> bisa juga diartikan
            sebagai <code>current folder/directory</code>
            jadi <code>git add .</code> berarti
            <code>git tambah (folder-ini)</code>
        </p>
        <p>
            2. <code>git commit -m "(message)"</code>
            <br />
            Perintah ini berfungsi untuk menandai atau memberi pesan/message apa
            yang kalian ubah di kodingan atau projectnya, misal
            <code>git commit -m "fixed bug at file app.py"</code>
        </p>
        <p>
            3.1 <code>gh repo create</code>
            Disini <code>gh</code> adalah <b>Github CLI</b> yang bertugas
            menghubungkan
            <b>Git</b> dengan <b>Github</b>, perintah ini cukup dijalankan
            sekali saat kalian baru membuat project yang belum di upload/push ke
            Github.
            <br />
            setelah menjalankan ini ada beberapa instruksi, ikuti saja sesuai tutorial
            ini:
        </p>
        <p>
            3.1.1 <b>What whould you like to do?</b>
            <b>Push an existing local repository to github.com</b>
            <br>
            ini mengisyaratkan <code>gh-cli</code> untuk mendorong repository yang sudah di initialize
            ke Github
        </p>
        <p>
            3.1.2 <b>Path to local repository?</b>
            <b>.</b>
            <br>
            sama seperti titik diatas pada saat <code>git add .</code>, titik disini berarti 
            bahwa repository <b>git</b> yang akan di push berada pada folder project yang 
            ditempati
        </p>
        <p>
            3.1.3 <b>Repository name (nama folder ini)</b>
            <b>.</b>
            <br>
            Di bagian ini kalian bebas mengisi nama Repository di Githubnya apa, mau beda pun
            gapapa. Tapi kalau mau samain kayak foldernya tinggal enter aja
        </p>
        <p>
            3.1.4 <b>Description</b>
            <b>.</b>
            <br>
            Deskripsikan project kalian, atau dibiarkan kosong juga gapapa
        </p>
        <p>
            3.1.5 <b>Visibility</b>
            <b>Public/Private (gunakan tanda panah di keyboard dan enter untuk konfirmasi)</b>
            <br>
            Disini kalian bisa pilih <b>Public</b> supaya Repo nya bisa dilihat oleh orang umum, <b>Private</b> kalau kalian hanya ingin ngetest 
            atau ikutin tutorial ini, saya rekomendasi Public jika kalian ingin share Repo nya ke teman" atau ke siapa saja.
        </p>
        <p>
            3.1.6 <b>Add a remote? Yes</b>
            <b>Public/Private (gunakan tanda panah di keyboard dan enter untuk konfirmasi)</b>
            <br>
            Remote disini berfungsi sebagai arah untuk menuju ke Github nya
        </p>
        <p>
            3.1.7 <b>What should the new remote be called? origin</b>
            <b>Public/Private (gunakan tanda panah di keyboard dan enter untuk konfirmasi)</b>
            <br>
            Origin adalah nama remote umum, namun kalian bisa namain apa aja. Tapi sebaiknya biarin Origin saja
        </p>
        <p>
            3.1.7 <b>Would you like to push commits from the current branch to "origin"? Yes</b>
            <b>Public/Private (gunakan tanda panah di keyboard dan enter untuk konfirmasi)</b>
            <br>
            Ini menanyakan apakah kita mau mendorong <b>commit</b> tadi ke Repo di Githubnya, pilih iya supaya filenya
            terupload ke Repo di Github kalian, setelah itu selesai
        </p>
        <p>
            3.2 <code>git push</code>
            <br>
            Perintah ini adalah perintah biasa yang kalian gunakan untuk ngepush, tidak perlu panjang panjang kayak diatas,
            namun hanya berlaku jika sudah di upload ke Github, bisa juga kalian masukin remotenya sendiri tapi sedikit rumit
            jadinya kita pake github-cli
        </p>
        <p>
            <br>
            <i>TL;DR</i>nya kalian hanya perlu menghafal <code>git add .</code>, <code>git commit -m "message"</code>,
            dan <code>git push</code> untuk melakukan VCS sederhana, ada lebih banyak lagi perintah Git seperti: 
            branch, log, diff, switch. Dan lain sebagainya, tapi akan dibahas di kursus terpisah khusus Git dan Github
        </p>
    </div>
</div>

<!-- feat: halaman progpel + repository pertamamu

- Halaman Program Pertama: hello world, git, github cli, repo pertama
- Sidebar mulprog: tambah section Program Pertama + anchor baru
- Setup: tambah Install Python + rename Installasi jadi Konfigurasi -->

<style>
    * {
        font-family: "Jetbrains Mono";
        transition: all 0.25s linear;
    }
</style>
