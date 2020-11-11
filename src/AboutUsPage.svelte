<div class="parent head">
    <div class="title">
        <div class="mdc-typography--headline4 theme-primary-color">What is checkSUM?</div>
    </div>
    <div class="center">
        <p class="mdc-typography--body1">
            checkSUM is a verification platform designed to provide strong
            legal verification of information about you (e.g. age) while protecting
            your identity. It works by verifying the information you enter into your
            checkSUM account page. This information is never sold or used to
            send you targeted advertising, nor is it given out to third parites. 
            Once we've had a chance to verify the information you've entered 
            through a background check you can generate a 'Validation Token'. This token can
            be used when you sign up for various accounts online to verify you are
            old enough to use their services.
        </p>
    </div>
    <div class="title">
        <div class="mdc-typography--headline4 theme-primary-color">How does checkSUM make money?</div>
    </div>
    <div class="center">
        <p class="mdc-typography--body1">
            Unlike other web services, checkSUM does not make any of its money by selling
            your information to advertisers. We store your information securely and only
            use it to verify your age to authorized web services. We make money by
            providing out anonomous verification services to companies like YouTube, Facebook, and Google.
        </p>
    </div>
    <div class="title">
        <div class="mdc-typography--headline4 theme-primary-color">What is a Validation Token and how do I get one?</div>
    </div>
    <div class="center">
        <p class="mdc-typography--body1">
            Validation tokens are time-based one-time passwords (TOTP).
            We use them to validate your infomation with other web services. They are
            six digits long and last for 30 seconds. A validation token is an anonomous way for us to provide 
            info to third parties without having to disclose your identity. You can obtain a validation token 
            by going to your account page. From there, you will see a list of verified information associated 
            with your checkSUM account. On this same page you will see a 'Generate Validation Token'. 
            Clicking this will create a cryptographically secure token and show the token on your screen. If you would
            rather not have to login to checkSUM everytime you need a validation token, scan the presented QR code with
            your favorite TOTP Authenticator app such as 
            Google Authenticator(
            <a href="https://apps.apple.com/us/app/google-authenticator/id388497605">iOS</a> | 
            <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US&gl=US">Android</a> ),
             Authy(
            <a href="https://apps.apple.com/us/app/twilio-authy/id494168017">iOS</a> | 
            <a href="https://play.google.com/store/apps/details?id=com.authy.authy&hl=en_US&gl=US">Android</a> ),
             Duo(
            <a href="https://apps.apple.com/us/app/duo-mobile/id422663827">iOS</a> | 
            <a href="https://play.google.com/store/apps/details?id=com.duosecurity.duomobile&hl=en_US&gl=US">Android</a> ), etc.
        </p>
    </div>
    <div class="title">
        <div class="mdc-typography--headline4 theme-primary-color">How are Validation Tokens used?</div>
    </div>
    <div class="center">
        <p class="mdc-typography--body1">
            Whenever a third party service asks you to verify your age, you will see an input box to place your
            six digit token in. The third party website reaches out to us with the inputted validation token 
            and we let the third party know if that token is associated with a user that is old enough to view the
            requested content. We do not give the third party any individual information only a yes or no answer to if the token
            is connected to an age worthy account. Using checkSUM makes it so you do not have to give out your personal information
            to companies when they ask you to verify your age.
        </p>
    </div>
</div>

<style>
    .parent {
        text-align: left;
        width: 100%;
    }

    .center {
        margin: auto;
        max-width: 600px;
    }

    .title {
        margin: auto;
        text-align: center;
        max-width: 800px;
    }

    .head {
        margin: 40px 0px 20px;
    }

</style>