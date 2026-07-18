<script>
    import Navbar from "../../components/navbar.svelte";
</script>

<Navbar />
<div id="belajarMenu" class="fullScreenContainer">
    <div class="category">
        <h3>Perkenalan dan setup</h3>
        <div class="categorySlider">
            <a href="./belajar">
                <div class="categoryEntry">
                    <div class="classUpper">
                        <h6 class="classTitle">Pengantar IK/TI</h6>
                        <p class="classDescription">
                            Belajar tentang dasar dasar Ilmu Komputer dan (atau)
                            Teknik Informatika
                        </p>
                    </div>
                    <div class="classLower">
                        <p class="classDifficulty pemula">Level: Pemula</p>
                    </div>
                </div>
            </a>
        </div>
    </div>
</div>

<style>
    * {
        font-family: "Jetbrains Mono";
        transition: all 0.25s linear;
        /* outline: 1px solid red; */
    }

    a {
        text-decoration: none;
    }

    #belajarMenu {
        padding: 10px 15px 10px 15px;
    }

    .category {
        width: fit-content;
        height: fit-content;
        margin-top: 0.5%;
    }

    .categorySlider {
        display: flex;
        width: fit-content;
        height: fit-content;
        align-items: center;

        margin-top: 15px;
    }

    .categoryEntry {
        border: 1px solid black;
        border-radius: 5px;

        width: 30vh;
        height: 30vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;

        position: relative;

        
    }

    .categoryEntry:hover {
        transform: translateX(5px) translateY(-5px);
        box-shadow: -5px 5px 0px black;
    }

    .classUpper {
        padding: 5%;
        width: 100%;
        height: 75%;
    }

    .classLower {
        width: 100%;
        height: 25%;
    }

    .classDifficulty {
        padding: 0% 5% 0% 5%;
        border-top: 1px solid black;
        border-bottom: 1px solid black;
    }

    .pemula {
        background-color: rgb(16, 192, 16);
    }
</style>
