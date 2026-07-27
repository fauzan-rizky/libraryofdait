<script>
    import Navbar from "../../../components/navbar.svelte";
    import SidebarIkti from "./sidebar-ikti.svelte";
    import "../../../styles/materials.css";

    let { children } = $props();
    let sidebarOpen = $state(false);
</script>

<Navbar
    showSidebar={true}
    {sidebarOpen}
    onSidebarToggle={() => sidebarOpen = !sidebarOpen}
/>
<div class="material-entry">
    <SidebarIkti open={sidebarOpen} onClose={() => sidebarOpen = false} />
    {@render children()}
</div>

{#if sidebarOpen}
    <div class="sidebar-overlay" onclick={() => sidebarOpen = false} role="presentation" onkeydown={(e) => e.key === 'Enter' && (sidebarOpen = false)}></div>
{/if}

<style>
    * {
        font-family: "Jetbrains Mono";
    }

    a, button, .sidebar-overlay {
        transition: all 0.25s linear;
    }

    .sidebar-overlay {
        display: none;
    }

    @media (max-width: 768px) {
        .material-entry {
            overflow-x: hidden;
        }

        .sidebar-overlay {
            display: block;
            position: fixed;
            inset: 0;
            top: 6vh;
            background: rgba(0, 0, 0, 0.4);
            z-index: 4;
        }
    }
</style>