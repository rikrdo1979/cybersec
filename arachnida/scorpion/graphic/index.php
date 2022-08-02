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
		<title>Image EXIF Read/Write</title>
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
					<div class="twelve column" style="margin-top: 5%">
						<input class="u-full-width" type="file" name="uploaded_file"></input><br />
					</div>
				</div>
				<div class="row">
					<div class="twelve columns">
						<input class="button-primary u-full-width" type="submit" value="Subir Imágen" onclick="this.form.submit(); this.disabled = true; this.value = 'Subiendo Imágen...';" ></input>
					</div>
				</div>
			</form>
			<?php
				if(!empty($_FILES['uploaded_file']))
				{
					$path = "./img/";
					$newname = $_FILES['uploaded_file']['name'];
					$newname = preg_replace( '/[^a-z0-9.]+/', '-', strtolower( $newname ) );
				    $path = $path . $newname;
					
					if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $path)) 
					{
						echo "La imágen <b>". $newname . "</b> se ha subido";
					} 
					else
					{
						echo "Ha habido un error, intentalo nuevamente!";
					}
				}
				?>
			<div class="row">
				<div class="twelve column" style="margin-top: 5%">
					<?php
						$d = './img/';
						$i = 0;
						foreach(glob($d.'*.{jpg,JPG,jpeg,JPEG,png,PNG,gif,GIF,bmp,BMP}',GLOB_BRACE) as $file){
							$imag[] =  basename($file);
							echo '<div class="rightpos"><a href="./readexif.php?image='.$imag[$i].'"><img src="./img/'.$imag[$i].'" width="100px"></a></div>';
							$i++;
						}
						?>
				</div>
			</div>
		</div>
	</body>
</html>
