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
		<title>Your page title here :)</title>
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
		<!-- Favicon
			–––––––––––––––––––––––––––––––––––––––––––––––––– -->
		<link rel="icon" type="image/ico" href="images/favicon.ico">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fork-awesome@1.2.0/css/fork-awesome.min.css" integrity="sha256-XoaMnoYC5TH6/+ihMEnospgm0J1PM/nioxbOUdnM8HY=" crossorigin="anonymous">
	</head>
	<body>
		<!-- Primary Page Layout
			–––––––––––––––––––––––––––––––––––––––––––––––––– -->
		<div class="container">
		<div class="row">
			<div class="twelve column" style="margin-top: 5%">
				<p>
					<?php
						$image = $_GET['image'];
						echo '<img src="./img/'.$image.'" width="200px"><br><br>';
						$comando = "exiftool -overwrite_original -all= ./img/".$image;
						exec($comando, $salida, $codigoSalida);
						echo $image."<br>";
						echo "<br>";
						foreach($salida as $linea){
						echo $linea."<br>";
						}
						?>
				<div class="row">
					<div class="two columns">
						<a href="javascript: history.back()" class="button u-full-width"><i class="fa fa-reply" aria-hidden="true"></i></a>
					</div>
					<div class="two columns">
						<button class="button u-full-width"  onclick="window.location.href ='./index.php'"><i class="fa fa-home" aria-hidden="true"></i></button>
					</div>
					<div class="four columns">
						<button class="button-primary  u-full-width"  onclick="window.location.href ='./readexif.php?image=<?php echo $image ?>'";>Read EXIF</button>
					</div>
					<div class="four columns">
						<button class="button-primary u-full-width"  onclick="window.location.href ='./editexif.php?image=<?php echo $image ?>'";>Edit EXIF</button>
					</div>
					</p>
				</div>
			</div>
		</div>
	</body>
</html>
