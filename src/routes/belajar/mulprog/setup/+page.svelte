<script>
    import scoophelp from "../../../../images/learning/mulprog/scoophelp.webp";
    import vscodeme from "../../../../images/learning/mulprog/VSCodeMe.webp";
    import codespaceswelcome from "../../../../images/learning/mulprog/codespaces-welcome.webp";
</script>

<div class="material">
    <div id="materi-1">
        <h3 class="materi-title">Setup</h3>
    </div>
    <div id="sub-1">
        <h3>Prasyarat</h3>

        <p>
            Disini kita utamanya akan menggunakan komputer/PC, tablet juga aman,
            HP bisa tapi ga dianjurkan
        </p>
        <p><b>PC</b></p>
        <p>Processor: I3 atau I5</p>
        <p>Graphics/GPU: (Optional), Integrated atau Dedicated boleh</p>
        <p>
            RAM: 4GB, atau 8GB (sekarang standarnya 8GB kalo pake Windows 10/11
            dikarenakan OS nya makan 4gb atau lebih)
        </p>

        <p>Storage kosong: 500MB-1GB</p>
        <p><b>Mobile</b></p>
        <p>
            disarankan menggunakan HP/Tablet keluaran terbaru atau maksimum 5-6
            tahun belakang
        </p>
        <p>
            khusus mobile silahkan skip hingga kolom Akun Github, lalu Install
            VSCode yang <b>[B]</b>
        </p>
        <p></p>
    </div>
    <div id="sub-2">
        <h3>Package manager</h3>
        <p>
            Untuk memudahkan instalasi dan update serta <b
                >SDK / Software Development Kit</b
            >
            nya (Program untuk compile/interpret kodingan) kita akan menggunakan
            <a href="https://scoop.sh/" target="_blank">Scoop</a>, sebuah
            package manager untuk Windows
        </p>
        <p>
            0. Buka <b>powershell</b> (Windows+R, ketik <code>powershell</code>,
            enter)
        </p>
        <p>
            1. Buka <a href="https://scoop.sh/" target="_blank">scoop.sh</a>,
            copy command instalasi yang ada di halaman utama
        </p>
        <p>
            2. Paste di powershell (<code>CTRL+V</code>), enter, dan tunggu
            hingga selesai
        </p>
        <p>
            3. Verifikasi instalasi: <code>scoop help</code>
        </p>
        <div class="images images-tutorial">
            <img src={scoophelp} alt="Scoop Help" />
        </div>
        <p>
            Kelebihan menggunakan Scoop adalah instalasi hanya dengan satu
            perintah, dan untuk update aplikasi di kemudian hari cukup dengan
            <code>scoop update *</code>
        </p>
    </div>
    <div id="sub-3">
        <h3>Konfigurasi Github</h3>
        <p></p>
        <div id="sub-3-1">
            <p><b>Akun GitHub</b></p>
            <p>
                1. Buka <a href="https://github.com" target="_blank"
                    >github.com</a
                >
                dan klik tombol <b>Sign up</b>
            </p>
            <p>
                2. Klik <b>Continue with Google</b>, lalu pilih akun Google yang
                ingin digunakan
            </p>
            <p>
                3. Masukkan <b>username</b> yang diinginkan dan region set ke Indonesia
            </p>
            <p>
                3.1 (Jika muncul langkah verifikasi) Klik tombol <b>Verify</b> dan
                lakukan langkah verifikasi yang disuruh
            </p>
            <p>
                4. Lanjutkan sesuai arahan di Github, klik <b><i>continue</i></b
                >
                lalu jika ada pernyataan syarat dan ketentuan centang, dan di
                bagian
                <b>
                    <i>receive news and info</i>
                </b> atau terima berita dan info gausah di centang, karena bisa memenuhi
                email, tapi kalau mau centang saja.
            </p>
            <p>
                5. Setelah terverifikasi, akun GitHub sudah siap digunakan —
                tidak perlu mengingat password baru karena sudah terhubung
                dengan akun Google, tetapi dianjurkan untuk mengamankan dengan
                password dan 2FA
            </p>
        </div>
        <div id="sub-3-2">
            <p><b>Install Git</b></p>
            <p>
                1. Buka <b>powershell</b> dan ketik perintah berikut:
                <br />
                <code>scoop install git</code>
            </p>
            <p>
                2. Tunggu hingga proses instalasi selesai (biasanya beberapa
                detik)
            </p>
            <p>
                3. Verifikasi instalasi dengan mengetik:
                <br />
                <code>git --version</code>
                <br />
                Jika muncul tulisan <code>git version x.y.z</code> maka Git sudah
                terinstal
            </p>
            <p>
                4. Konfigurasi identitas Git agar terhubung dengan akun GitHub:
            </p>
            <p>
                <code
                    >git config --global user.name "username-github-kalian"</code
                >
            </p>
            <p>
                <code
                    >git config --global user.email
                    "email-yang-dipake-di-github"</code
                >
            </p>
        </div>
    </div>
    <div id="sub-4">
        <h3>Install VSCode</h3>
        <p>
            Selain Package Manager kita juga butuh Code Editor untuk mengedit
            dan mengerjakan kodingan kita, di tutorial ini kita akan menggunakan
            VSCode, karena UI nya enak untuk dilihat dan gampang di setup buat
            segala kalangan
        </p>
        <p>Tutorial untuk PC [A]</p>
        <p>
            Namun kalau tidak bisa memakai PC ada juga Code Editor cloud based
            yang bisa diakses melalui browser lewat tablet atau HP, kalau tidak
            memungkinkan menggunakan PC [B]
        </p>
        <p><b>[A]</b></p>
        <p>
            1. Install VSCode: <code>scoop install vscode</code>
        </p>
        <p>
            2. Buka VSCode dengan mengetik <code>code</code> di powershell
        </p>
        <p>3. VSCode akan terbuka seperti gambar dibawah</p>
        <div class="images images-tutorial">
            <img src={vscodeme} alt="Vscode Me" />
        </div>
        <p>
            Kalau sudah muncul seperti diatas berarti Scoop dan VSCode sudah
            terinstall.
            <br />
            <a
                href="https://marketplace.visualstudio.com/items?itemName=Carlos18mz.cyberpunk-2077-rebuild"
                target="_blank">PS: Tema VSCode yang diatas</a
            >
        </p>
        <p><b>[B]</b></p>
        <p>
            Untuk di device tablet/mobile kita akan menggunakan cloud based
            editor dari Github yaitu Codespaces
        </p>
        <p>
            1. Kunjungi landing page <a href="https://github.com/features/codespaces" target="_blank">Codespaces di Github</a> dan pilih "Get Started
            for Free"
        </p>
        <p>2. Pilih template "Blank"</p>
        <p>
            3. Kalau sudah masuk biarkan dulu hingga semuanya sudah aman dan
            muncul message Welcome seperti gambar dibawah
        </p>
        <div class="images images-tutorial">
            <img src={codespaceswelcome} alt="Vscode Me" />
        </div>
    </div>
    <div id="sub-5">
        <h3>Install Python</h3>
        <p>
            *Khusus untuk mobile bisa skip step ini karena Python SDK sudah
            termasuk kedalam Codespaces
        </p>
        <p>
            1. Buka powershell dan ketik perintah berikut:
            <br />
            <code>scoop install main/python</code>
        </p>
        <p>
            2. Tunggu hingga selesai, lalu ketik:
            <br />
            <code>python --version</code>
        </p>
        <p>
            Kalau muncul <code>Python x.y.z</code> maka Python SDK sudah terinstal
        </p>
    </div>
</div>

<style>
    * {
        font-family: "Rajdhani";
    }

    a, code {
        transition: all 0.25s linear;
    }

    code {
        background-color: #e0e0e0;
        padding: 0.125rem 0.313rem;
        border-radius: 3px;
    }
</style>
