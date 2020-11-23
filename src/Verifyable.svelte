<div style="height: 60px;">
    <div class="third"><p class="theme-primary-color mdc-typography--body1" stye="margin: 0px;">{label}</p></div>
    <div class="third">
        <p class="theme-primary-color mdc-typography--body1" style="margin: 0px;">{progressMsgs[pCount].msg}:</p>
        <div style="text-align: left;">
            <LinearProgress progress={progressMsgs[pCount].percent}/>
        </div>
    </div>
    <div class="third">
        {#if !tokenGenerated}
            <Button variant="raised" style="color: white;" disabled={pCount<3} on:click={generate}><Label>Generate Verification Token</Label></Button>
        {/if}
    </div>
</div>
{#if tokenGenerated}
    <div class='title'>
        {#if !QRcodeGenerated && wantsQRCode}
            <p class="mdc-typography--headline5 theme-primary-color">
                Create QR code for on-the-go codes?
            </p>
            <div class="center">
                <Button style="width: 60%; color: white;" on:click={generateQRCode} variant="raised"><Label>Yes</Label></Button>
                <Button color="secondary" style="width: 35%;" on:click={noQRCode}><Label>No</Label></Button>
            </div>
        {/if}
    </div>

    {#if QRcodeGenerated && !scanned}
        <br>
        <br>
        <div class="center">
            <QrCode value = {otpauth}></QrCode>
        </div>
        <div>
            <Button style="width: 60%; color: white;" on:click={generateToken} variant="raised"><Label>I have scanned the QR code</Label></Button>
        </div>
    {/if}


    {#if scanned}
        <div class="center" style="height: 60px;">
            <div class="half" use:lock>
                <Textfield id="readonly" variant="outlined" bind:value={verificationCode} label="Verification Token"/>
            </div>
            <div class="half"><Button variant="raised" style="color: white; margin-top: 10px;" on:click={copyCode}><Label>Copy To Clipboard</Label></Button></div>
        </div>
    {/if}
    
{/if}

<script>
    import Button, {Label}  from "@smui/button";
    import LinearProgress from '@smui/linear-progress';
    import Textfield from '@smui/textfield';
    import QrCode from 'svelte-qrcode';
    import { authenticator } from 'otplib';

    export let userEmail = 'user@email.tld'; //need this to change to the user's email address

    const service = 'checkSUM';
    let _secret;//This secret would need to be stored in the database so that the token can be recreated
    //Or we store the token so then we don't need to know the information of the users trying to log in. Just if the code is contained in a certain greater than 13 age. I say we do this of course it would always be changing tho so maybe we do it your way when generate code is clicked but we use the tried and test functions of TOTP to make the token. Or we make the codes change every hour instead of every 30sec like they do with TOTP

    export let label = "Birth Date: MM/DD/YYYY";
    export let pCount = 0;
    let progressMsgs = [
        {msg: "Recieving Data", percent: 0.0},
        {msg: "Processing Request", percent: 0.33},
        {msg: "Performing Backgroun Check", percent: 0.66},
        {msg: "Complete", percent: 1.0},
    ]

    let verificationCode = "";
    let tokenGenerated = false;
    let QRcodeGenerated = false;
    let wantsQRCode = true;
    let scanned = false;
    let otpauth;
    let seconds;
    let seconds2;

    export function updateProgress(state) {
        if (state > 0 && state < 4) {
            progress =  progressMsg[0].msg;
            progressMsg = progressMsgs[0].msg;
        }
    }

    function lock() {
        document.querySelectorAll("#readonly > input").forEach(e => 
			e.setAttribute("readonly", "true")
		);
    }

    let generateQRCode = () => {
        _secret = authenticator.generateSecret();
        otpauth = authenticator.keyuri(userEmail, service, _secret);
        QRcodeGenerated = true;
    }

    let noQRCode = () => {
        wantsQRCode = false;
        scanned = true;
        generateToken();
    }

    let generate = () => {
        tokenGenerated = true;
    }

    let prevVerificationCode = "";
    let generateToken = () => {
        if (!wantsQRCode) {
            _secret = authenticator.generateSecret();
            verificationCode = authenticator.generate(_secret);
            prevVerificationCode = verificationCode
            storeSecret(verificationCode).then(resp => console.log(resp));
        }
        scanned = true;
        setInterval(function(){
            verificationCode = authenticator.generate(_secret)
            if (prevVerificationCode != verificationCode) {
                storeSecret(verificationCode).then(resp => console.log(resp));
                prevVerificationCode = verificationCode;
            }
        }, 1000);
    }

    let copyCode = () => {
        navigator.clipboard.writeText(verificationCode)
            .then(() => {
              alert('code copied to clipboard');
            })
            .catch(err => {
              alert('there was an error copying  the code: ', err);
            });
    }

    let storeSecret = (secret) => {
        let baseURL = `http://localhost:8080/checkSUM/`; 
        return fetch(baseURL+"store_secret", {
            method: "POST",
            headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
                secret: secret,
                email: userEmail,
			}),
        }).
        then(resp => resp.json());
    }
</script>

<style>
    .center {
        margin: auto;
        max-width: 400px;
    }

    .half {
        width: 50%;
        float: left;
    }

    .third {
        width: 33%;
        float: left;
    }

    .title {
        margin: auto;
        text-align: center;
        max-width: 800px;
    }
</style>