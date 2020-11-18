<script>
	import Login from "./Login.svelte";
	import Contact from "./ContactPage.svelte";
	import About from "./AboutUsPage.svelte";
	import Tab, {Icon, Label} from '@smui/tab';
	import TabBar from '@smui/tab-bar';
	import Signup from "./Signup.svelte";
	import MyAccount from "./AccountPage.svelte";


	let loginActive = "Login";
	let loginTabItems = ["Login", "About Us", "Contact Us"];

	let signupActive = "Sign Up";
	let signupTabItems = ["Sign Up", "About Us", "Contact Us"];

	let myAccountActive = "My Account";
	let myAccountTabItems = ["My Account", "About Us", "Contact Us"];
	let userEmail = '';
    let userPassword = '';
	let activePage = "Login";
	let user;

	async function doGet() {
		alert("Email: " + userEmail + " Pass: " + userPassword);
		fetch(`http://localhost:8080/checkSUM/database/`, {
			method: 'POST',
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				email: userEmail,
				password: userPassword
			})
		}).
		then(resp => resp.text()).
		then(resp => {
			console.log(resp);
		})
	}

	async function doPost() {
		alert("Email: " + user.email + " Pass: " + user.password);
		databaseData = await fetch(`http://127.0.0.1:8080/checkSUM/database/`, {
			method: 'POST',
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				email: user.email,
				password: user.password,
				fname: user.firstName,
				lname: user.lastName,
				bday: user.birthdate,
				bcity: user.birthCity,
				bstate: user.birthState
			})
		})
	}

	let login = () => {
		/* 
			Do login stuff here like verify a username and password	
		*/
		myAccountActive = "My Account";
		activePage = "My Account";
		doGet();
	}

	let signup = () => {
		signupActive = "Sign Up";
		activePage = "Sign Up";
	}

	let createAccount = () => {
		/*
			Do signup stuff here like set up a user account
		*/
		myAccountActive = "My Account";
		activePage = "My Account";
		doPost();
	} 

</script>

<style>
	.header {
		margin: 0px;
		padding: 0px 10px 10px;
		background-color: #25cbea;
	}
</style>

<div class="header">
		{#if !(activePage == "Login" && loginActive == "Login") }
			<div style="width:175px; float: left;">
				<svg style="width:175px; height: 50px;" viewBox="0 0 210 60">
					<g id="layer1">
						<path
						id="rect887"
						style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.144273;stroke-opacity:1"
						d="m 41.754279,13.103355 v 31.827692 h 6.414863 V 33.353983 a 2.4531599,2.4531599 0 0 1 -0.0039,-0.1307 2.4531599,2.4531599 0 0 1 2.45323,-2.452997 2.4531599,2.4531599 0 0 1 2.452285,2.401887 h 0.01719 v 11.759114 h 6.337375 V 33.171933 h -0.0016 a 8.7670845,8.7670845 0 0 0 -8.766589,-8.676614 8.7670845,8.7670845 0 0 0 -0.02446,0 8.7670845,8.7670845 0 0 0 -2.464063,0.36055 V 13.103355 Z" />
						<path
						id="circle954"
						style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.172211;stroke-opacity:1"
						d="m 87.770982,23.289559 a 8.7670845,8.7670845 0 0 0 -8.737358,8.467017 h -0.0063 v 6.685684 h 0.0087 a 8.7670845,8.7670845 0 0 0 8.759718,8.410267 8.7670845,8.7670845 0 0 0 8.760649,-8.436167 h -6.368894 a 2.4145293,2.4145293 0 0 1 -2.391755,2.08372 2.4145293,2.4145293 0 0 1 -2.410598,-2.28061 v -0.26517 -5.763684 -0.27012 a 2.4145293,2.4145293 0 0 1 2.383748,-2.27826 2.4145293,2.4145293 0 0 1 0.0268,0 2.4145293,2.4145293 0 0 1 2.398345,2.13695 h 6.364174 a 8.7670845,8.7670845 0 0 0 -8.762519,-8.489627 8.7670845,8.7670845 0 0 0 -0.0245,0 z" />
						<path
						id="rect966"
						style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.144273;stroke-opacity:1"
						d="m 97.460905,13.103355 v 31.827692 h 6.414845 v -7.871194 l 5.79006,7.831404 h 7.56882 l -10.35576,-14.006761 8.37,-10.351034 h -7.67055 l -3.70257,4.578877 V 13.103355 Z" />
						<path
						id="path1028"
						style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.172211;stroke-opacity:1"
						d="m 69.443039,23.289559 a 8.7670845,8.7670845 0 0 0 -8.74233,8.767057 8.7670845,8.7670845 0 0 0 0.0254,0.665527 v 4.69568 a 8.7670845,8.7670845 0 0 0 -0.0254,0.667647 8.7670845,8.7670845 0 0 0 8.767058,8.767057 8.7670845,8.7670845 0 0 0 8.765151,-8.585947 h -6.357372 a 2.4145293,2.4145293 0 0 1 -2.407779,2.2335 2.4145293,2.4145293 0 0 1 -2.408019,-2.23892 h -0.0078 v -4.484677 h 11.178117 v -2.009067 a 8.7670845,8.7670845 0 0 0 -8.762321,-8.477857 8.7670845,8.7670845 0 0 0 -0.02446,0 z m -0.0023,6.352677 a 2.4145293,2.4145293 0 0 1 0.02681,0 2.4145293,2.4145293 0 0 1 2.396947,2.12448 h 0.03181 v 7.8e-4 h -4.844378 v -7.8e-4 h 0.01883 a 2.4145293,2.4145293 0 0 1 2.370092,-2.12448 z" />
						<path
						id="path1133"
						style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.172495;stroke-opacity:1"
						d="m 129.82006,12.341165 a 8.8636399,6.1680995 0 0 0 -8.86364,6.168087 8.8636399,6.1680995 0 0 0 4.1e-4,0.0419 h 0.0166 v 10.053264 a 3.0804648,2.1436581 0 0 0 -0.0238,0.2653 3.0804648,2.1436581 0 0 0 3.03666,2.14325 v 0.001 h 8.57366 v 9.806494 h 0.0307 a 2.7793054,1.9340849 0 0 1 -2.77052,1.78267 2.7793054,1.9340849 0 0 1 -2.75921,-1.70341 h 0.017 v -6.234107 h -6.12503 v 6.234137 h 0.01 a 8.8636414,6.1681005 0 0 0 8.85759,5.937357 8.8636414,6.1681005 0 0 0 8.86081,-6.018857 h -0.0513 V 29.293266 a 3.0804648,2.1436581 0 0 0 0.0606,-0.42326 3.0804648,2.1436581 0 0 0 -3.08029,-2.143527 3.0804648,2.1436581 0 0 0 -0.53592,0.0326 h -8.01717 v -8.257357 h -0.0162 a 2.7793054,1.9340849 0 0 1 2.7483,-1.92601 2.7793054,1.9340849 0 0 1 0.0311,0 2.7793054,1.9340849 0 0 1 2.77941,1.93388 2.7793054,1.9340849 0 0 1 -7.8e-4,0.0419 h 0.019 v 6.083217 h 6.04062 v -6.083217 h 0.025 a 8.8636399,6.1680995 0 0 0 4e-4,-0.0419 8.8636399,6.1680995 0 0 0 -8.86361,-6.168087 z" />
						<path
						id="circle1157"
						style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.172495;stroke-opacity:1"
						d="M 142.93731,13.283785 V 40.75284 h 0.005 a 8.8636414,6.1681005 0 0 0 8.86283,6.084347 8.8636414,6.1681005 0 0 0 8.86361,-6.168097 8.8636414,6.1681005 0 0 0 -4e-4,-0.0573 h -0.0537 V 13.316145 h -6.06968 V 40.82062 h 0.0307 a 2.7793054,1.9340849 0 0 1 -2.77051,1.78267 2.7793054,1.9340849 0 0 1 -2.77658,-1.85041 h 0.0352 V 13.283825 Z" />
						<path
						id="rect1167"
						style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.28033;stroke-opacity:1"
						d="m 164.42584,13.190755 0.0941,0.17032 v 32.475022 h 6.12058 V 24.442119 l 2.09808,3.798317 -0.042,0.0756 h 6.20984 0.0836 l -0.0416,-0.0756 2.12595,-3.849197 v 21.525238 h 6.06364 V 13.413065 l 0.12277,-0.22231 h -6.20984 l -5.20743,9.428214 -5.20785,-9.428214 z" />
						<path
						id="path1878"
						style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.282904;stroke-opacity:1"
						d="m 28.558463,10.036338 a 8.9489001,10.225126 0 0 0 -8.867675,10.076164 h 0.0072 V 31.225536 H 18.991089 V 46.596487 H 38.984184 V 31.225536 H 25.900744 V 20.112502 h 0.0016 a 2.7398914,3.1306346 0 0 1 2.729032,-2.98178 2.7398914,3.1306346 0 0 1 0.0078,0 2.7398914,3.1306346 0 0 1 2.731617,2.88607 v 4.649037 a 3.1129007,3.5118825 0 0 0 -0.02377,0.43543 3.1129007,3.5118825 0 0 0 3.112989,3.511737 3.1129007,3.5118825 0 0 0 3.112471,-3.511737 3.1129007,3.5118825 0 0 0 -10e-4,-0.0863 h 0.0041 v -4.902497 h 0.01137 a 8.9489001,10.225126 0 0 0 -8.947774,-10.076164 8.9489001,10.225126 0 0 0 -0.08062,0 z" />
					</g>
				</svg>
			</div>
		{/if}
		<div>
			{#if activePage == "Login"}
				<TabBar style="max-width: 700px;" tabs={loginTabItems} let:tab bind:active={loginActive}>
					<Tab on:click={() => console.log(activePage)} style="color: white;" {tab}>
						<Label on:click={() => console.log(activePage)} style="color: white;">{tab}</Label>
					</Tab>
				</TabBar>
			{/if}
			{#if activePage == "Sign Up"}
				<TabBar style="max-width: 700px;" tabs={signupTabItems} let:tab bind:active={signupActive}>
					<Tab on:click={() => console.log(activePage)} style="color: white;" {tab}>
						<Label on:click={() => console.log(activePage)} style="color: white;">{tab}</Label>
					</Tab>
				</TabBar>
			{/if}
			{#if activePage == "My Account"}
				<TabBar style="max-width: 700px;" tabs={myAccountTabItems} let:tab bind:active={myAccountActive}>
					<Tab on:click={() => console.log(activePage)} style="color: white;" {tab}>
						<Label id="testThis" on:click={() => console.log(activePage)} style="color: white;">{tab}</Label>
					</Tab>
				</TabBar>
			{/if}
		</div>
</div>

{#if activePage == "Login" && loginActive == "Login" }
	<Login login={login} signup={signup} bind:userEmail={userEmail} bind:userPassword={userPassword}></Login>
{/if}

{#if loginActive == "About Us" || signupActive == "About Us" || myAccountActive == "About Us"}
	<About></About>
{/if}

{#if loginActive == "Contact Us" || signupActive == "Contact Us" || myAccountActive == "Contact Us"}
	<Contact></Contact>
{/if}

{#if activePage == "Sign Up" && signupActive == "Sign Up"}
	<Signup createAccount={createAccount} bind:user={user}></Signup>
{/if}

{#if activePage == "My Account" && myAccountActive == "My Account"}
	<MyAccount></MyAccount>
{/if}