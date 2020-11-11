<script>
    import Button, {Label, Icon} from '@smui/button';
    export let title;
</script>


<Button variant="raised" on:click={() => alert('Signing in...')}><Label>{title}</Label></Button>
