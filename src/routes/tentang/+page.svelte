<script>
    import Navbar from "../../components/navbar.svelte";
    import Daitanimate from "../../components/daitanimate.svelte";
    import "../../styles/text.css";
</script>

<Navbar showSidebar={false} />
<div class="tentang-container">
    <Daitanimate />
    <div class="pc">
    <h1>Depok Association of Information and Technology</h1>
    </div>
    
    <div class="mobile">
        <h1>
            Depok Association 
        </h1>
        <h2>
            Of
        </h2>
        <h1>
            Information and Technology
        </h1>
    </div>
    <p>
        DAIT adalah sebuah asosiasi non-formal dan non-profit yang bertujuan untuk menghubungkan pelajar-pelajar terutama mahasiwa
        dari jurusan Teknik Informatika, Ilmu Komputer atau sejenisnya untuk saling berkolaborasi dan berbagi pengalaman serta ilmu.
        Saat ini DAIT berfokus pada pengembangan project open source seperti ini dan juga kompetisi seperti hackathon dan lain sebagainya.
    </p>
    <p></p>
</div>

<style>
    * {
        color: white;
        font-family: "Slabo 27px", serif;
        font-style: normal;
    }

    p {
        padding-top: 15px;
        background-color: rgba(0, 0, 0, 0);
        font-family: "Jetbrains Mono";
        text-align: justify;
        width: 75%;
    }

    .pc {
        display: block;
    }
    
    .mobile {
        display: none;
        text-align: center;
    }
    
    .tentang-container {
        width: 100vw;
        min-height: calc(100vh - 6vh);
        margin-top: 6vh;
        padding: 2rem 1.5rem;
        
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    @media (max-width: 768px) {
        .pc {
            display: none;
        }

        .mobile {
            display: block;
        }
    }
</style>
