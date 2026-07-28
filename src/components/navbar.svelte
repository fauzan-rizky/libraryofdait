<script>
    let sideToggleEl;
    let {
        sidebarOpen = false,
        onSidebarToggle = () => {},
        showSidebar = false,
    } = $props();
    let navMenuOpen = $state(false);
    let navOnEl;
    let navOffEl;

    $effect(() => {
        if (sideToggleEl) {
            sideToggleEl.style.transform = sidebarOpen
                ? "rotate(90deg)"
                : "rotate(0deg)";
        }
    });

    $effect(() => {
        if ((navOnEl, navOffEl)) {
            navOnEl.style.transform = navMenuOpen
                ? "rotate(90deg)"
                : "rotate(0deg)";
            navOnEl.style.opacity = navMenuOpen ? 0 : 1;
            navOffEl.style.transform = navMenuOpen
                ? "rotate(90deg)"
                : "rotate(0deg)";
            navOffEl.style.opacity = navMenuOpen ? 1 : 0;
        }
    });

    const navMenu = () => {
        // navOnEl.style.transform = navMenuOpen ? "rotate(90deg)" : "rotate(0deg)";
        // navOnEl.style.opacity = navMenuOpen ? 1 : 0;
        // navOffEl.style.transform = navMenuOpen ? "rotate(90deg)" : "rotate(0deg)"
        // navOffEl.style.opacity = navMenuOpen ? 0 : 1;
        // if (navMenuOpen == false) {
        //     navOnEl.style.transform = "rotate(90deg)";
        //     navOnEl.style.opacity = 0;
        //     navOffEl.style.transform = "rotate(90deg)";
        //     navOffEl.style.opacity = 1;
        // }
        // if (navMenuOpen == true) {
        //     navOnEl.style.transform = "rotate(0deg)";
        //     navOnEl.style.opacity = 1;
        //     navOffEl.style.transform = "rotate(0deg)";
        //     navOffEl.style.opacity = 0;
        // }
        navMenuOpen = !navMenuOpen;
    };
</script>

<div id="navbar">
    {#if showSidebar}
        <button
            class="sidebar-toggle"
            onclick={onSidebarToggle}
            aria-label="Buka sidebar"
        >
            <svg
                width="100%"
                height="100%"
                viewBox="0 0 508 508"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <g id="sideToggle">
                    <rect
                        id="Rectangle 11"
                        x="5"
                        y="5"
                        width="498"
                        height="498"
                        fill="#FE0AB9"
                        stroke="black"
                        stroke-width="10"
                    />
                    <g id="sideArrow" bind:this={sideToggleEl}>
                        <rect
                            id="Rectangle 15"
                            x="123.495"
                            y="74"
                            width="338"
                            height="63"
                            rx="31.5"
                            transform="rotate(30 123.495 74)"
                            fill="black"
                        />
                        <rect
                            id="Rectangle 16"
                            width="338"
                            height="63"
                            rx="31.5"
                            transform="matrix(0.866025 -0.5 -0.5 -0.866025 123.604 433.839)"
                            fill="black"
                        />
                    </g>
                </g>
            </svg>
        </button>
    {/if}
    <a href="/" id="logo-link">
        <h2 id="navbar-title">Library of DAIT</h2>
    </a>
    <a class="links" href="/belajar"><h2>Belajar</h2></a>
    <a class="links" href="/tentang"><h2>Tentang</h2></a>
</div>
<div class="navbar-spacer"></div>

{#if navMenuOpen}
    <div
        class="nav-overlay"
        onclick={() => navMenu()}
        role="presentation"
        onkeydown={(e) => e.key === "Enter" && (navMenuOpen = false)}
    >
        <div class="nav-menu" onclick={(e) => e.stopPropagation()} role="none">
            <a
                href="/"
                class="nav-menu-link"
                id="navbar-mobile-title"
                onclick={() => (navMenuOpen = false)}>Library of DAIT</a
            >
            <a
                href="/belajar"
                class="nav-menu-link"
                onclick={() => (navMenuOpen = false)}>Belajar</a
            >
            <a
                href="/tentang"
                class="nav-menu-link"
                onclick={() => (navMenuOpen = false)}>Tentang</a
            >
        </div>
    </div>
{/if}

<button
    class="nav-toggle"
    onclick={() => navMenu()}
    aria-label="Buka menu navigasi"
>
    <svg viewBox="0 0 508 508" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g id="navToggle">
            <rect
                id="Rectangle 11"
                x="5"
                y="5"
                width="498"
                height="498"
                fill="#00FFF7"
                stroke="black"
                stroke-width="10"
            />
            <g id="navOff" bind:this={navOffEl}>
                <rect
                    id="Rectangle 12"
                    x="130.464"
                    y="85.9155"
                    width="411"
                    height="63"
                    rx="31.5"
                    transform="rotate(45 130.464 85.9155)"
                    fill="black"
                />
                <rect
                    id="Rectangle 14"
                    x="85.9158"
                    y="376.537"
                    width="411"
                    height="63"
                    rx="31.5"
                    transform="rotate(-45 85.9158 376.537)"
                    fill="black"
                />
            </g>
            <g id="navOn" bind:this={navOnEl}>
                <rect
                    id="Rectangle 12_2"
                    x="48"
                    y="93"
                    width="411"
                    height="63"
                    rx="31.5"
                    fill="black"
                />
                <rect
                    id="Rectangle 13"
                    x="48"
                    y="222"
                    width="411"
                    height="63"
                    rx="31.5"
                    fill="black"
                />
                <rect
                    id="Rectangle 14_2"
                    x="48"
                    y="351"
                    width="411"
                    height="63"
                    rx="31.5"
                    fill="black"
                />
            </g>
        </g>
    </svg>
</button>

<style>
    a, button, #navOff, #navOn, #sideArrow {
        transition: all 0.1s linear;
    }
    #navbar-title,
    #navbar-mobile-title {
        color: #00fff7;
        text-shadow: 3px -3px 0 #fe0ab9;
        font-weight: 100;
    }

    a {
        background: transparent;
        margin-left: 1%;
        text-decoration: none;

        font-family: "Jersey 25", sans-serif;
        font-style: normal;

        padding: 0;
    }

    h2 {
        font-weight: 100;
    }

    #logo-link {
        height: 100%;
        display: flex;
        align-items: center;
    }

    #navbar {
        background-color: white;
        display: flex;
        align-items: center;
        border-bottom: 1px solid black;

        padding: 5px 0 0 5px;
        position: fixed;
        width: 100vw;
        height: 6vh;
        z-index: 10;
    }

    #navToggle {
        width: 44px;
        height: 44px;
    }

    #navOff {
        opacity: 0;
    }

    #navOff,
    #navOn,
    #sideArrow {
        transform-origin: center;
    }

    .navbar-spacer {
        height: 6vh;
        width: 100vw;
    }

    .sidebar-toggle {
        display: none;
        width: 44px;
        height: 44px;
        background: none;
        border: none;
        cursor: pointer;
        padding: 4px;
        z-index: 12;
    }

    .nav-toggle {
        display: none;
        position: fixed;
        top: calc(0.75vh);
        right: 8px;
        width: 44px;
        height: 44px;
        background: none;
        border: none;
        cursor: pointer;
        padding: 4px;
        z-index: 12;
    }

    .nav-overlay {
        position: fixed;
        inset: 0;
        background: white;
        z-index: 11;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: navFadeIn 0.3s ease forwards;
    }

    @keyframes navFadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    .nav-menu {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 75%;
        gap: 2rem;
    }

    .nav-menu-link {
        font-family: "Jersey 25", sans-serif;
        font-size: 3rem;
        text-decoration: none;
        color: black;
    }

    .nav-menu-link:hover {
        color: #fe0ab9;
    }

    @media (max-width: 768px) {
        #navbar {
            justify-content: space-between;
            padding: 5px 8px 0;
        }

        #navbar-title {
            font-size: clamp(2rem, 7vw, 2.8rem);
            text-shadow: 2px -2px 0 #fe0ab9;
            white-space: nowrap;
        }

        #logo-link {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
        }

        .links {
            display: none;
        }

        .sidebar-toggle {
            display: block;
        }

        .nav-toggle {
            display: block;
        }
    }
</style>
