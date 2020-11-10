<script>
	import Login from "./Login.svelte";
	import TabBar from "./TabBar.svelte";
	import Signup from "./Signup.svelte";
<<<<<<< HEAD
=======

	let tabItems = [
    { label: "Login", value: 1 },
    { label: "About Us", value: 2 },
	{ label: "Contact Us", value: 3 }
  	];
	let currentTab;
	  
	function print(currentTab) {
		alert(currentTab);
	}
>>>>>>> signup
</script>

<TabBar bind:activeTabValue={currentTab} items={tabItems}/>

<code class="language-text"></code>

{#if 1 === currentTab}
  <Login></Login>
{/if}

{#if 2 === currentTab}
	About Us Component goes here
{/if}

<<<<<<< HEAD
<!--Login></Login-->
<Signup></Signup>
=======
{#if 3 === currentTab}
	Contact Us Component goes here
{/if}
>>>>>>> signup
