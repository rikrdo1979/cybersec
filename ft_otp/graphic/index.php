<?php
	ini_set('display_errors', 1);
	ini_set('display_startup_errors', 1);
	error_reporting(E_ALL);
?>

<!DOCTYPE html>
<html lang="en">
	<head>
		<!-- Basic Page Needs
			–––––––––––––––––––––––––––––––––––––––––––––––––– -->
		<meta charset="utf-8">
		<title>Safe Password and QR Generator</title>
		<meta name="description" content="">
		<meta name="author" content="">
		<!-- Mobile Specific Metas
			–––––––––––––––––––––––––––––––––––––––––––––––––– -->
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!-- FONT
			–––––––––––––––––––––––––––––––––––––––––––––––––– -->
		<link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">
		<!-- CSS
			–––––––––––––––––––––––––––––––––––––––––––––––––– -->
		<link rel="stylesheet" href="css/normalize.css">
		<link rel="stylesheet" href="css/skeleton.css">
		<link rel="stylesheet" href="css/custom.css">
		<!-- Favicon
			–––––––––––––––––––––––––––––––––––––––––––––––––– -->
		<link rel="icon" type="image/ico" href="images/favicon.ico">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fork-awesome@1.2.0/css/fork-awesome.min.css" integrity="sha256-XoaMnoYC5TH6/+ihMEnospgm0J1PM/nioxbOUdnM8HY=" crossorigin="anonymous">
	</head>
	<body>
		<!-- Primary Page Layout
			–––––––––––––––––––––––––––––––––––––––––––––––––– -->
		<div class="container">
			<form enctype="multipart/form-data" action="#" method="POST">
				<div class="row">
					<div class="twelve columns" style="margin-top: 5%">
						<input class="u-full-width" type="text" name="phrase" placeholder="Write your prhase!"></input>
					</div>
				</div>
				<div class="row">
					<div class="twelve columns">
						<input class="button-primary u-full-width" type="submit" value="Convert to HEX" onclick="this.form.submit(); this.disabled = true; this.value = 'Procesando...';" ></input>
					</div>
				</div>
			</form>
				<div class="row">
					<div class="twelve columns">
					<?php
						function url_encode($string){return urlencode(utf8_encode($string));}
						
						if (isset($_POST['phrase'])){
							$phrase = $_POST['phrase'];
							$str = bin2hex($phrase);
							$len = strlen($str);
							if ($len >= 64){
								echo "<center><h3>Your phrase is valid!</h3></center><br><br>";
								echo "Your input: <code>".$phrase."</code><br><br>";
								echo "HEX Output: <code>".$str."</code><br><br>";
								echo "Lenght: <code>".$len."</code><br><br>";
								$gettoken = exec('./ft_otp -k -php');
								echo "Your Token: <code>".$gettoken."</code><br>";
								$getqr = exec('./ft_otp -g "'.$phrase.'" -php');
								$urldecod = "otpauth://totp/rikrdo@cybersec.es?secret=".$getqr."&issuer=ft_otp";
								$urlencod = url_encode($urldecod);
								echo '<center><img src="https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl='.$urlencod.'&choe=UTF-8" title="'.$urldecod.'" /></center>';
								}
							else {
								echo "<h3>Not valid, try again!</h3>";
							}
						}
					?>
				</div>
			</div>
		</div>
	</body>
</html>
