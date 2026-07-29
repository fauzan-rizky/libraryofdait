<script>
    import Navbar from "../../components/navbar.svelte";
</script>

<Navbar />
<div id="belajarMenu" class="full-screen-container">
    <div class="category">
        <h3>PERKENALAN DAN SETUP</h3>
        <div class="category-slider">
            <a class="entry-link" href="/belajar/pengantar-ikti/pengenalan">
            
                <div class="category-entry">
                <p class="class-type teori">Teori</p>
                    <div class="class-upper">
                        
                        <h6 class="class-title">Pengantar IK/TI</h6>
                        <p class="class-description">
                            dasar dasar Ilmu Komputer (dan/atau) Teknik Informatika
                        </p>
                    </div>
                    <div class="class-lower">
                        <p class="class-difficulty pemula">Level: Pemula</p>
                    </div>
                </div>
                
            </a>
            <a class="entry-link" href="/belajar/mulprog/ddp">
                <div class="category-entry">
                <p class="class-type tutorial">Tutorial</p>
                    <div class="class-upper">
                        <h6 class="class-title">Dasar pemrograman dan setup</h6>
                        <p class="class-description">
                            mulai ngoding membuat program pertamamu
                        </p>
                    </div>
                    <div class="class-lower">
                        <p class="class-difficulty pemula">Level: Pemula</p>
                    </div>
                </div>
                
            </a>
        </div>
    </div>
</div>

<style>
    * {
        font-family: "Rajdhani";
        /* outline: 1px solid red; */
        font-weight: 600;
    }

    a, .category-entry {
        transition: all 0.25s linear;
    }

    #belajarMenu {
        background-color: white;
        color: black;
        width: 100vw;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        padding: clamp(16px, 3vh, 48px) 15px 10px 15px;
    }

    a {
        color: inherit;
        text-decoration: none;
    }

    .category {
        width: fit-content;
        height: fit-content;
        margin-top: clamp(8px, 1.5vh, 24px);
    }

    .category-slider {
        display: flex;
        width: fit-content;
        height: fit-content;
        align-items: center;

        margin-top: 15px;
        gap: 25px;
    }

    .category-entry {
        border: 1px solid black;
        border-radius: 5px;

        width: clamp(200px, 15vw, 400px);
        height: clamp(210px, 15vw, 400px);
        display: flex;
        flex-direction: column;
        justify-content: space-between;

        position: relative;
    }

    @media (max-width: 768px) {
        .category {
            align-self: center;
            width: 100%;
        }

        .category-slider {
            flex-direction: column;
            width: 100%;
            gap: 1rem;
        }

        .category-entry {
            width: 100%;
            height: auto;
            min-height: clamp(130px, 28vw, 180px);
        }

        .entry-link {
            width: 100%;
        }
    }

    .category-entry:hover {
        transform: translateX(5px) translateY(-5px);
        box-shadow: -5px 5px 0px black;
    }

    .class-upper {
        padding: 5%;
        width: 100%;
        display: flex;
        flex-direction: column;
    }

    .class-lower {
        width: 100%;
    }

    .class-difficulty {
        padding: 0% 5% 0% 5%;
        border-top: 1px solid black;
        margin-bottom: 0;
        border-radius: 0 0 5px 5px;
        color: rgb(0, 0, 0);
    }

    .pemula {
        background-color: rgb(16, 192, 16);
    }

    .class-type {
        margin-bottom: 0;
        background-color: beige;
        padding: 0% 5% 0% 5%;
        border-radius: 5px 5px 0px 0px;
        border-bottom: 1px solid black;
    }

    .teori {
        background-color: #dbeafe;
    }

    .tutorial {
        background-color: #fef3c7;
    }

    .class-title {
        font-size: clamp(1.2rem, 3vw, 1.5rem);
    }

    .class-description {
    font-size: clamp(0.85rem, 2.2vw, 1rem);
    margin-bottom: 0;
}
</style>
