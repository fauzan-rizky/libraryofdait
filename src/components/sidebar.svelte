<script>
    let { sections = [], open = false, onClose = () => {} } = $props();

    $effect(() => {
        if (open && window.innerWidth <= 768) {
            document.body.style.overflow = 'hidden';
            return () => {
                document.body.style.overflow = '';
            };
        }
    });

    function isMobile() {
        return window.innerWidth <= 768;
    }

    function handleNav(e, href) {
        if (!isMobile()) return;
        const [path, hash] = href.split('#');
        if (path !== window.location.pathname) {
            return;
        }
        e.preventDefault();
        const el = document.getElementById(hash);
        if (el) {
            el.scrollIntoView({ behavior: 'smooth' });
            history.pushState(null, '', href);
        }
        setTimeout(onClose, 300);
    }
</script>

<div class="sidebar" class:open>
    <button class="sidebar-close" onclick={onClose}>✕</button>
    {#each sections as section}
        <h5 class="sidebar-title">
            <a href={section.href} onclick={(e) => handleNav(e, section.href)}>{section.title}</a>
        </h5>
        <ul>
            {#each section.items as item}
                <li>
                    {#if item.href}
                        <a href={item.href} onclick={(e) => handleNav(e, item.href)}>{item.label}</a>
                    {:else}
                        {item.label}
                    {/if}
                </li>
            {/each}
        </ul>
    {/each}
</div>

<div class="sidebar-spacer"></div>

<style>
    * {
        transition: all 0.25s ease;
        text-decoration: none;
    }
    h5 {
        background-color: rgb(226, 226, 226);
        padding: 0.156rem;
    }

    ul {
        margin-top: 0.625rem;
        padding-left: 0.313rem;
        border-left: 1px solid black;
        list-style-type: none;
    }

    li {
        padding: 0.313rem 0;
    }
    li:hover {
        padding-left: 0.625rem;
    }

    a {
        color: inherit;
        text-decoration: none;
    }

    .sidebar {
        width: min(20vw, 384px);
        height: 94vh;
        padding: 0.625rem;
        outline: 1px solid black;
        background-color: white;

        position: fixed;
    }

    .sidebar-spacer {
        width: min(20vw, 384px);
        height: max-content;
    }

    .sidebar-title {
        text-align: center;
    }

    .sidebar-close {
        display: none;
    }

    @media (max-width: 768px) {
        .sidebar {
            position: fixed;
            top: 6vh;
            left: 0;
            width: 70vw;
            height: 94vh;
            outline: 1px solid black;
            background-color: white;
            padding: 0.625rem;
            z-index: 5;
            transform: translateX(-100%);
            transition: transform 0.3s ease;
            overflow: hidden;
        }

        .sidebar.open {
            transform: translateX(0);
        }

        .sidebar-spacer {
            width: 0;
        }

        .sidebar-close {
            display: block;
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            padding: 0;
            margin-bottom: 0.5rem;
        }
    }
</style>