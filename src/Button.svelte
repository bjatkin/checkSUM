<script>
    export let title;

    function handleClick() {
    alert('Thank you for saying hello back')
}
</script>

<button on:click={handleClick}>
	{title}
</button>