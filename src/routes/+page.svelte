<script>
    import Navbar from "../components/navbar.svelte";
    import "../styles/text.css";
    import { onMount } from "svelte";

    let displayText = $state("");
    let words = ["komputer", "informatika", "web dev", "ngoding", "TIK", "IT"];
    let wordIndex = $state(0);
    let charIndex = $state(0);
    let isDeleting = $state(false);
    let isWaiting = $state(false);
    let speed = 150;
    let pauseTime = 1500; // delay sebelum backspace (ms)

    onMount(() => {
        const interval = setInterval(() => {
            if (isWaiting) return; // skip kalo lagi pause

            const currentWord = words[wordIndex];

            if (!isDeleting) {
                if (charIndex < currentWord.length) {
                    displayText += currentWord[charIndex];
                    charIndex++;
                } else {
                    // Selesai ketik, mulai waiting
                    isWaiting = true;
                    setTimeout(() => {
                        isWaiting = false;
                        isDeleting = true;
                    }, pauseTime);
                }
            } else {
                if (charIndex > 0) {
                    displayText = displayText.slice(0, -1);
                    charIndex--;
                } else {
                    // Selesai backspace, tunggu lagi sebelum ketik kata berikutnya
                    isWaiting = true;
                    isDeleting = false;
                    wordIndex = (wordIndex + 1) % words.length;
                    setTimeout(() => {
                        isWaiting = false;
                    }, pauseTime);
                }
            }
        }, speed);

        return () => clearInterval(interval);
    });
</script>

<Navbar />
<div class="full-screen-container" id="home">
    <h1 class="top-element" id="title">Library of DAIT</h1>
    <h2 class="top-element" id="subtitle">
        tempat belajar <span class="typing">{displayText}</span> berbahasa
        Indonesia
    </h2>
    <div class="top-element" id="subtitle-mobile">
        <h2 class="subtitle-mobile-text">
            tempat belajar <span class="typing">{displayText}</span> 
        </h2>
        <h2 class="subtitle-mobile-text">berbahasa indonesia</h2>
    </div>
    <div class="start-wrapper top-element">
        <div id="start">
            <a href="/belajar" aria-label="belajar">
            <h3>
                MULAI
            </h3></a>
        </div>
    </div>
</div>

<style>
    h1,
    h2,
    span {
        background-color: rgba(0, 0, 0, 0);
        font-family: "Rajdhani";
        font-weight: 700;
        font-style: normal;
    }
    a {
        text-decoration: none;
    }
    #title {
        color: #fe0ab9;
        text-shadow: 0px 0px 15px #00fff7;
    }

    #subtitle,
    #subtitle-mobile, span {
        color: #00fff7;
        text-shadow: 0px 0px 15px #fe0ab9;
    }

    #subtitle-mobile {
        display: none;
    }

    @property --angle {
        syntax: "<angle>";
        initial-value: 360deg;
        inherits: false;
    }

    .start-wrapper::before,.start-wrapper::after {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        transform: translateX(-5px) translateY(-5px);
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        background: linear-gradient(var(--angle),rgba(0, 255, 247, 1) 0%, rgba(254, 10, 185, 1) 100%);
        z-index: 0;

        animation: start-anim 1s steps(360) infinite;
    }

    .start-wrapper::before {
        filter: blur(1.5rem);
    }

    @keyframes start-anim {
        from {
            --angle: 360deg;
        }

        to {
            --angle: 0deg;
        }
    }

    .start-wrapper {
        position: relative;
        transform: translateY(35px);
    }

    #start {
        color: #00fff7;
        background-color: black;

        text-decoration: none;

        padding: 2px 10px 2px 10px;
        position: relative;
        border: 2.5px solid black;
        z-index: 1;
    }
    
    #start a h3 {
        font-weight: 800;
    }

    span {
        border-right: 5px solid #fe0ab9;
        animation: blink 1.5s linear infinite;
    }

    #home::before {
        content: "";
        background: url("../images/cpbg.webp");
        background-size: cover;
        align-items: center;
        justify-content: center;
        filter: brightness(65%);
        width: 100%;
        height: 94%;
        position: absolute;
        z-index: 0;
    }

    #home {
        height: 94vh;
        align-items: center;
        justify-content: center;
        
    }

    .top-element {
                z-index: 1;

    }

    @keyframes blink {
        0% {
            border-right: 5px solid #fe0ab9;
        }

        50% {
            border-right: 5px solid #fe0ab900;
        }

        100% {
            border-right: 5px solid #fe0ab9;
        }
    }

    @media (max-width: 768px) {
        #title {
            font-size: clamp(2.5rem, 12vw, 3.5rem);
        }

        #subtitle {
            display: none;
        }

        #subtitle-mobile {
            width: 90%;
            text-align: center;
            display: block;
        }

        .subtitle-mobile-text {
            font-size: clamp(1.8rem, 6vw, 2.75rem);
        }
    }
</style>
