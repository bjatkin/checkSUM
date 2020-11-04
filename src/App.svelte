<script>
	import Button from "./Button.svelte";
	export let name;
</script>

<style>
	h1 {
		color: rgb(0, 128, 11);
	}
</style>

<h1>Hello {name}!</h1>

<Button title="Hello computer"></Button>