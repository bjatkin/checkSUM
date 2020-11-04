<script>
    import Button, {Label, Icon} from '@smui/button';
    export let title;

    function handleClick() {
    alert('Thank you for saying hello back')
}
</script>

<Button variant="raised"><Label>{title}</Label></Button>
<Button><Label>{title}</Label></Button>
