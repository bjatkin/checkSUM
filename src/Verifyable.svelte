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
            <Button variant="raised" style="color: white;" disabled={pCount<3} on:click={generateToken}><Label>Generate Verification Token</Label></Button>
        {/if}
        {#if tokenGenerated}
            <Button class="theme-error-color" on:click={cancleToken}><Label>Cancle Token</Label></Button>
        {/if}
    </div>
</div>
{#if tokenGenerated}
    <div class="center" style="height: 60px;">
        <div class="half" use:lock>
            <Textfield id="readonly" variant="outlined" bind:value={verificationCode} label="Verification Token"/>
        </div>
        <div class="half"><Button variant="raised" style="color: white; margin-top: 10px;" on:click={copyCode}><Label>Copy To Clipboard</Label></Button></div>
    </div>
{/if}

<script>
    import Button, {Label}  from "@smui/button";
    import LinearProgress from '@smui/linear-progress';
    import Textfield from '@smui/textfield';

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
    function generateToken() {
        let ref = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        let first = ""
        let last = ""
        for (let i = 0; i < 4; i++) {
            first += ref.charAt(Math.floor((Math.random() * ref.length)));
            last += ref.charAt(Math.floor((Math.random() * ref.length)));
        }
        verificationCode = first+"-"+last
        tokenGenerated = true;
    }

    function cancleToken() {
        verificationCode = ""
        tokenGenerated = false;
    }

    function copyCode() {
        navigator.clipboard.writeText(verificationCode)
            .then(() => {
              alert('code copied to clipboard');
            })
            .catch(err => {
              alert('there was an error copying  the code: ', err);
            });
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
</style>