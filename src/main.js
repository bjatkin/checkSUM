import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		name: 'world'
	}
});

document.body.style.margin = "0px";
window.app = app;

export default app;