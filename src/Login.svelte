<script>
    import RaisedButton from "./RaisedButton.svelte";
    import Button from "./Button.svelte";
    import TextBox from "./TextBox.svelte";
    import AccountPage from "./AccountPage.svelte";
    import ForgotPass from "./ForgotPass.svelte";
    import CreateAccount from "./Signup.svelte";
    //TODO add svg and move things aroung
    let accountload = false;
    let buttonClicked = false;
    let forgotload = false;
    let setupload = false;

    function loadAccount(){
        accountload = true;
        buttonClicked = true;
    }
    function loadForgot() {
        forgotload = true;
        buttonClicked = true;
    }
    function setup() {
        setupload = true;
        buttonClicked = true;
    }

</script>

{#if buttonClicked == false}
    <br />
    <TextBox type = "email" label="Email Address"></TextBox>
    <br />
    <TextBox type = "password" label="Password"></TextBox>
    <br />
    <RaisedButton title = "SIGN IN" on:click={loadAccount}></RaisedButton>
    <br />
    <Button title = "forgot password?" on:click={loadForgot} />
    <Button title = "Create account" on:click={setup} />
{/if}

{#if buttonClicked == true}
    {#if accountload == true}
        <AccountPage></AccountPage>
    {/if}
    {#if forgotload == true}
        <ForgotPass></ForgotPass>
    {/if}
    {#if setupload == true}
        <CreateAccount></CreateAccount>
    {/if}
{/if}