<div class="parent head">
    <div class="center">
        <div class="mdc-typography--headline6 theme-primary-color">Sign Up</div>
    </div>
</div>

{#if user.firstpage}
    <div class="parent">
        <div class="center">
            <Textfield style="width: 100%;" type="email" variant="outlined" bind:value={user.email} label="Email*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a" />
            <HelperText id="helper-text-outlined-a">Enter Your Email Address</HelperText>
        </div>
        <div class="center">
            <Textfield style="width: 100%;" type="email" variant="outlined" bind:value={user.confirmEmail} label="Confirm Email*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a" />
            <HelperText id="helper-text-outlined-a">Re-Enter The Same Email Address</HelperText>
        </div>
        <hr>
        <div class="center">
            <Textfield style="width: 100%;" type="password" variant="outlined" bind:value={user.password} label="Password*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a" />
            <HelperText id="helper-text-outlined-a">Enter The Account Password</HelperText>
        </div>
        <div class="center">
            <Textfield style="width: 100%;" type="password" variant="outlined" bind:value={user.confirmPassword} label="Confirm Password*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a" />
            <HelperText id="helper-text-outlined-a">Re-Enter The Same Password</HelperText>
        </div>
        <hr>
        <div class="right">
            <Button style="color: white; width: 60%;" on:click={() => user.firstpage = false} variant="raised"><Label>Next</Label></Button>
        </div>
    </div>
{/if}

{#if !user.firstpage}
    <div class="parent">
        <div class="center">
            <Textfield style="width: 100%;" variant="outlined" bind:value={user.firstName} label="First Name*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a" />
            <HelperText id="helper-text-outlined-a">Enter Your First Name</HelperText>
        </div>
        <div class="center">
            <Textfield style="width: 100%;" variant="outlined" bind:value={user.lastName} label="Last Name*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a" />
            <HelperText id="helper-text-outlined-a">Enter Your Last Name</HelperText>
        </div>
        <hr>
        <div class="mdc-typography--body1">Birthday</div>
        <div class="center">
            <Textfield style="width: 100%;" variant="outlined" bind:value={user.birthdate} label="Birthdate: MM/DD/YYYY*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a" />
            <HelperText id="helper-text-outlined-a">MM/DD/YYYY</HelperText>
        </div>
        <div class="center">
            <Textfield style="width: 100%;" variant="outlined" bind:value={user.birthCity} label="City of Birth*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a" />
            <HelperText id="helper-text-outlined-a">Enter Your City Of Birth</HelperText>
        </div>

        <div class="center">
            <Select style="width: 100%;" variant="outlined" bind:value={user.birthState} label="State of Birth*" input$aria-controls="helper-text-outlined-a" input$aria-describedby="helper-text-outlined-a">
                <Option value=""></Option>
                {#each states as state}
                    <Option value={state} selected={user.birthState === state}>{state}</Option>
                {/each}
            </Select>
            <HelperText id="helper-text-outlined-a">Enter Your State Of Birth</HelperText>
        </div>
        <hr>
        <div class="right">
            <Button color="secondary" style="width: 35%;" on:click={() => user.firstpage = true}><Label>Back</Label></Button>
            <Button style="width: 60%; color: white;" on:click={createAccount} variant="raised"><Label>Create Account</Label></Button>
        </div>
    </div>
{/if}



<script>
    import Textfield from '@smui/textfield';
    import HelperText from '@smui/textfield/helper-text/index';
    import Button, {Label} from '@smui/button';
    import Select, {Option} from '@smui/select';

    let states = ['Alabama',
        'Alaska',
        'Arizona',
        'Arkansas',
        'California',
        'Colorado',
        'Connecticut',
        'Delaware',
        'Florida',
        'Georgia',
        'Hawaii',
        'Idaho',
        'Illinois',
        'Indiana',
        'Iowa',
        'Kansas',
        'Kentucky',
        'Louisiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnesota',
        'Mississippi',
        'Missouri',
        'Montana',
        'Nebraska',
        'Nevada',
        'New Hampshire',
        'New Jersey',
        'New Mexico',
        'New York',
        'North Carolina',
        'North Dakota',
        'Ohio',
        'Oklahoma',
        'Oregon',
        'Pennsylvania',
        'Rhode Island',
        'South Carolina',
        'South Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont',
        'Virginia',
        'Washington',
        'West Virginia',
        'Wisconsin',
        'Wyoming'];

    let user = { 
        firstpage: true,
        email: '',
        confirmEmail: '',
        password: '',
        confirmPassword: '',
        firstName: '',
        lastName: '',
        birthdate: '',
        birthCity: '',
        birthState: '',
    };

    function createAccount() {
        alert("Created Account with"+
            "\nEmail: "+user.email+
            "\nPassword: "+user.password+
            "\nFirst Name: "+user.firstName+
            "\nLast Name: "+user.lastName+
            "\nBirth Date: "+user.birthdate+
            "\nBirth City: "+user.birthCity+
            "\nBirth State: "+user.birthState
        );
    }
</script>

<style>
    .head {
        margin: 40px 0px 20px;
    }
    .parent {
        text-align: center;
        width: 100%;
    }
    .center {
        margin: auto;
        max-width: 400px;
    }

    .right {
        margin: auto;
        text-align: right;
        max-width: 400px;
    }

    hr {
        max-width: 440px;
    }
</style>