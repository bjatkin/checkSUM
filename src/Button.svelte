<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    import Button, {Label, Icon} from '@smui/button';
    export let title = "YO";
</script>

<Button><Label>{title}</Label></Button>