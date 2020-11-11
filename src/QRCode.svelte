<script>
	import QrCode from "svelte-qrcode"
	let code = "otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example";
</script>

<div class="container">
	<h1>
		checkSUM QR Code
	</h1>
  <QrCode value={code} />
</div>