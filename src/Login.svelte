<script>
    import RaisedButton from "./RaisedButton.svelte";
    import Button from "./Button.svelte";
    import TextBox from "./TextBox.svelte";
    //TODO add svg and move things aroung
</script>

<br />
<TextBox type = "email" label="Email"></TextBox>
<br />
<TextBox type = "password" label="Password"></TextBox>
<br />
<RaisedButton title = "SIGN IN"></RaisedButton>
<br />
<Button title = "forgot password?" message = 'Forgot Password!!'></Button>
<Button title = "Create account" message = 'Creating an account'></Button>