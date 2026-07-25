<script>
    let { sidebarOpen = false, onSidebarToggle = () => {}, showSidebar = false } = $props();
    let navMenuOpen = $state(false);
</script>

<div id="navbar">
    {#if showSidebar}
    <button class="sidebar-toggle" onclick={onSidebarToggle} aria-label="Buka sidebar">
        <svg width="100%" height="100%" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="4" y="8" width="32" height="4" rx="2" fill="black"/>
            <rect x="4" y="18" width="32" height="4" rx="2" fill="black"/>
            <rect x="4" y="28" width="32" height="4" rx="2" fill="black"/>
        </svg>
    </button>
    {/if}
    <a href="/" id="logo-link">
        <h2 id="navbar-title">Library of DAIT</h2>
    </a>
    <a class="links" href="/belajar"><h2>Belajar</h2></a>
    <a class="links" href="/"><h2>Tentang</h2></a>
</div>
<div class="navbar-spacer"></div>

{#if navMenuOpen}
    <div class="nav-overlay" onclick={() => navMenuOpen = false} role="presentation" onkeydown={(e) => e.key === 'Enter' && (navMenuOpen = false)}>
        <div class="nav-menu" onclick={(e) => e.stopPropagation()} role="none">
            <a href="/" class="nav-menu-link" id="navbar-mobile-title" onclick={() => navMenuOpen = false}>Library of DAIT</a>
            <a href="/belajar" class="nav-menu-link" onclick={() => navMenuOpen = false}>Belajar</a>
            <a href="/" class="nav-menu-link" onclick={() => navMenuOpen = false}>Tentang</a>
        </div>
    </div>
{/if}

<button class="nav-toggle" onclick={() => navMenuOpen = !navMenuOpen} aria-label="Buka menu navigasi">
    <svg width="100%" height="100%" viewBox="0 0 397 397" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g id="menuToggle">
            <rect id="mt-frame" x="7.5" y="7.5" width="382" height="382" rx="7.5" fill="#D3D3D3" stroke="black" stroke-width="15"/>
            <rect id="mt-top" x="32" y="51" width="329" height="60" rx="25" fill="black"/>
            <rect id="mt-middle" x="32" y="169" width="329" height="59" rx="25" fill="black"/>
            <rect id="mt-bottom" x="36" y="286" width="329" height="60" rx="25" fill="black"/>
            <rect id="mt-x-left" x="101.041" y="61.3213" width="329" height="59" rx="25" transform="rotate(45 101.041 61.3213)" fill="black"/>
            <rect id="mt-x-right" x="333.679" y="103.041" width="329" height="59" rx="25" transform="rotate(135 333.679 103.041)" fill="black"/>
        </g>
    </svg>
</button>

<style>
    #navbar-title, #navbar-mobile-title {
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

    #mt-x-left, #mt-x-right {
        opacity: 0;
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
        from { opacity: 0; }
        to { opacity: 1; }
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