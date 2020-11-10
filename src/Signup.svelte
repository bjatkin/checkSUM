<script>
import Button from "@smui/button/Button.svelte";

import App from "./App.svelte";

    //import RaisedButton from "./RaisedButton.svelte";
    import TextBox from "./TextBox.svelte";
    import DropDownSelect from "./DropDownSelect.svelte";
    let user = { firstpage: true };
    function toggle() { //is not being called idk why
        alert("you clicked!");
        user.firstpage = !user.firstpage;
    }
    //TODO add svg and move things aroung
</script>

<div class="mdc-typography--headline6">Sign Up</div>
<br />

{#if user.firstpage}
    <TextBox type = "email" label="Email Address"></TextBox>
    <br />
    <TextBox type = "email" label="Confirm Email Address"></TextBox>
    <br />
    <TextBox type = "password" label="Account Password"></TextBox>
    <br />
    <TextBox type = "password" label="Confirm Account Password"></TextBox>
    <br />
    <button type="button" on:clink={toggle}>
        Next
    </button>
    <br />
{/if}

{#if !user.firstpage}
    <TextBox type = "text" label="First Name"></TextBox>
    <br />
    <TextBox type = "text" label="Last Name"></TextBox>
    <hr />
    <div class="mdc-typography--body1">Birthday</div>
    <TextBox type = "text" label="Bithdate: MM/DD/YYYY"></TextBox>
    <br />
    <TextBox type = "text" label="City of Birth"></TextBox>
    <DropDownSelect></DropDownSelect>
    <hr />
    <button type="button" on:clink={toggle}>
        Back
    </button>
    <button>
        Create Account
    </button>
{/if}


