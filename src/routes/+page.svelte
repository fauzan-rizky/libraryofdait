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
    <h1 id="title">Library of DAIT</h1>
    <h2 id="subtitle">
        tempat belajar <span class="typing">{displayText}</span> berbahasa
        Indonesia
    </h2>
    <div id="subtitle-mobile">
        <h2 class="subtitle-mobile-text">
            tempat belajar <span class="typing">{displayText}</span> 
        </h2>
        <h2 class="subtitle-mobile-text">berbahasa indonesia</h2>
    </div>
</div>

<style>
    h1,
    h2,
    span {
        background-color: rgba(0, 0, 0, 0);
        font-family: "Jersey 25", sans-serif;
        font-weight: 500;
        font-style: normal;
    }
    #title {
        color: #fe0ab9;
        text-shadow: 0px 0px 20px #00fff7;
    }

    #subtitle,
    #subtitle-mobile, span {
        color: #00fff7;
        text-shadow: 0px 0px 20px #fe0ab9;
    }

    #subtitle-mobile {
        display: none;
    }

    span {
        border-right: 5px solid #fe0ab9;
        animation: blink 1.5s linear infinite;
    }

    #home {
        background: url("../images/cpbg.jpg");
        background-size: cover;
        align-items: center;
        justify-content: center;
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
