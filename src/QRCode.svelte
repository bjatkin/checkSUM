<script>
    import QrCode from "svelte-qrcode";
    import { authenticator } from 'otplib';
    const user = 'User@email.com';
    const service = 'checkSUM';
    //This secret would need to be stored in the database so that the token can be recreated
    const _secret = authenticator.generateSecret();
    //Or we store the token so then we don't need to know the information of the users trying to log in. Just if the code is contained in a certain greater than 13 age. I say we do this of course it would always be changing tho so maybe we do it your way when generate code is clicked but we use the tried and test functions of TOTP to make the token. Or we make the codes change every hour instead of every 30sec like they do with TOTP
    let token = authenticator.generate(_secret);
    const otpauth = authenticator.keyuri(user, service, _secret);

    setInterval(function(){token = authenticator.generate(_secret)}, 1000);
</script>

<h1>Token: {token}</h1>
<div class="container">
	<h1>
        checkSUM QR Code
    </h1>
  <QrCode value={otpauth}/>
</div>