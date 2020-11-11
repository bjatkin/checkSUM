<script>
	import Login from "./Login.svelte";
	import Contact from "./ContactPage.svelte";

	import Tab, {Icon, Label} from '@smui/tab';
	import TabBar from '@smui/tab-bar';
	import QR from './QRCode.svelte';
	let active = 'Login';
	let tabItems = ["Login", "About Us", "Contact Us"];

</script>

<style>
	.header {
		margin: 0px;
		padding: 0px 10px 10px;
		background-color: #25cbea;
	}
</style>

<div class="header">
	<TabBar style="max-width: 500px;" tabs={tabItems} let:tab bind:active>
		<Tab style="color: white;"{tab}>
		<Label style="color: white;">{tab}</Label>
		</Tab>
	</TabBar>
</div>

{#if active == 'Login'}
  <Login></Login>
{/if}

{#if active == 'About Us'}
	About Us Component goes here
	<QR></QR>
{/if}

{#if active == 'Contact Us'}
	<Contact></Contact>
{/if}