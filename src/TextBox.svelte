<script>
    import Textfield from '@smui/textfield'
    export let type;
    export let label;
    export let value = '';
</script>


<Textfield variant="outlined" type={type} bind:value={value} label={label} input$autocomplete={type} />