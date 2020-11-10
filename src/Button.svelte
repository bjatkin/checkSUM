<script>
    import Button, {Label, Icon} from '@smui/button';
    export let title;
    export let message;
</script>

<Button on:click={() => alert(message)}><Label>{title}</Label></Button>