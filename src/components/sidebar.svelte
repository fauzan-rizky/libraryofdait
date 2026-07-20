<script>
    /**
     * SIDEBAR — Komponen navigasi samping yang reusable.
     * 
     * Cara pake:
     *   <Sidebar sections={sidebarSections} />
     * 
     * Format prop `sections` (array of objects):
     * 
     * [
     *   {
     *     title: "Judul Section",   // → tampil di dalam <h5>
     *     href: "./link-section",    // → href di <a> dalam <h5>
     *     items: [                   // → <ul><li>
     *       { label: "Nama item", href: "./link-item" },
     *       { label: "Item tanpa link" }  // kalau ga punya href, render polos
     *     ]
     *   }
     * ]
     */
    let { sections = [] } = $props();
</script>

<div class="sidebar">
    {#each sections as section}
        <h5>
            <a href={section.href}>{section.title}</a>
        </h5>
        <ul>
            {#each section.items as item}
                <li>
                    {#if item.href}
                        <a href={item.href}>{item.label}</a>
                    {:else}
                        {item.label}
                    {/if}
                </li>
            {/each}
        </ul>
    {/each}
</div>

<div class="sidebarSpacer"></div>

<style>
    * {
        transition: all 0.25s ease;
        text-decoration: none;
    }
    h5 {
        background-color: rgb(226, 226, 226);
        padding: 2.5px;
    }

    ul {
        margin-top: 10px;
        padding-left: 5px;
        border-left: 1px solid black;
        list-style-type: none;
    }

    li:hover {
        padding-left: 10px;
    }
    .sidebar {
        width: 20vw;
        height: 94vh;
        padding: 10px;
        outline: 1px solid black;
        background-color: white;

        position: fixed;
    }

    .sidebarSpacer {
        width: 20vw;
        height: max-content;
    }
</style>
