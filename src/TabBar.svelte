<script>
    import { createEventDispatcher } from 'svelte';
    import Tab, {Icon, Label} from '@smui/tab';
    import TabBar from '@smui/tab-bar';
    import Button from '@smui/button';
    //export let active = 'Login';

    import { onMount } from "svelte";
  
    export let items = [];
    export let activeTabValue;

    onMount(() => {
    // Set default tab value
    if (Array.isArray(items) && items.length && items[0].value) {
      activeTabValue = items[0].value;
    }
  });

    const handleClick = tabValue => () => (activeTabValue = tabValue);
</script>


<!--TabBar tabs={['Login', 'About Us', 'Contact Us']} let:tab bind:active>
    <!-- Notice that the `tab` property is required! >
    <Tab {tab}>
    <Label>{tab}</Label>
    </Tab>
</TabBar-->

  
<ul>
{#if Array.isArray(items)}
    {#each items as item}
    <li class={activeTabValue === item.value ? 'active' : ''}>
        <span on:click={handleClick(item.value)}>{item.label}</span>
    </li>
    {/each}
{/if}
</ul>
  
<style>
ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none;
    border-bottom: 1px solid #dee2e6;
}

span {
    border: 1px solid transparent;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
    display: block;
    padding: 0.5rem 1rem;
    cursor: pointer;
}

span:hover {
    border-color: #e9ecef #e9ecef #dee2e6;
}

li.active > span {
    color: #495057;
    background-color: #fff;
    border-color: #dee2e6 #dee2e6 #fff;
}
</style>