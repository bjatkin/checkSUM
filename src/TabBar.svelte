<script>
    import { createEventDispatcher } from 'svelte';
    import Tab, {Icon, Label} from '@smui/tab';
    import TabBar from '@smui/tab-bar';
    import Button from '@smui/button';
    let active = 'Login';
</script>


<TabBar tabs={['Login', 'About Us', 'Contact Us']} let:tab bind:active>
    <!-- Notice that the `tab` property is required! -->
    <Tab {tab}>
    <Label>{tab}</Label>
    </Tab>
</TabBar>