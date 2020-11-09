<script>
	import Button from "./Button.svelte";
	import Nav from "./Nav.svelte";
	import Login from "./Login.svelte";
	export let name;
</script>

<style>
	/* h1 {
		color: purple;
	} */
</style>

<Nav></Nav>

<h1>Hello {name}!</h1>

<Button title="Hello computer"></Button>