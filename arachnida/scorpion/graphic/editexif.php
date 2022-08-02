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
  <?php
      $image = $_GET['image'];

      if (isset($_POST['bartist'])) {
        $o = null;
        $cartist = "exiftool -artist='".$_POST['artist']."' ./img/".$image;
        exec($cartist, $o, $co);
        if ($o != null){header("Refresh:0");}        
      } 

      $artist = "exiftool -s -s -s -artist ./img/". $image;
      exec($artist, $s, $cs);
      $artista = "ej. John Doe";
      foreach ($s as $artista) {$artista;}

      if (isset($_POST['bcredit'])) {
        $o1 = null;
        $ccredit = "exiftool -credit='".$_POST['credit']."' ./img/".$image;
        exec($ccredit, $o1, $co1);  
        if ($o1 != null){header("Refresh:0");}    
      } 

      $credit = "exiftool -s -s -s -credit ./img/". $image;
      $creditos = "ej. Copyright, John Doe";
      exec($credit, $s1, $cs1);
      foreach ($s1 as $creditos) {$creditos;}
      
      if (isset($_POST['bcomment'])) {
        $o2 = null;
        $ccomment = "exiftool -comment='".$_POST['comment']."' ./img/".$image;
        exec($ccomment, $o2, $co2);  
        if ($o2 != null){header("Refresh:0");}    
      } 

      $comment = "exiftool -s -s -s -comment ./img/". $image;
      $comentario = "ej. Took during John Doe party";
      exec($comment, $s2, $cs2);
      foreach ($s2 as $comentario) {$comentario;}
    ?>

		<div class="container">

		  <div class="row">
		    <div class="twelve column" style="margin-top: 5%">
		      <p>
            <?php echo '<img src="./img/'.$image.'" width="200px"><br>';?>
        </div>
      <div>

      <div class="row">
        <div class="twelve columns">
          <form action="#" method="post">
            <label for="artist">Artist</label>
        </div>
      <div>

      <div class="row">
        <div class="ten columns">       
              <input class="u-full-width" name="artist" type="text" placeholder="<?php echo $artista; ?>" id="artistinput">
        </div>
        <div class="two columns">   
              <button class="button u-full-width" type="submit" name="bartist"><i class="fa fa-floppy-o" aria-hidden="true"></i></button>
            </form>
        </div>
      <div>

      <div class="row">
        <div class="twelve columns">
          <form action="#" method="post">
            <label for="credit">Credit</label>
        </div>
      <div>

      <div class="row">
        <div class="ten columns">
            <input class="u-full-width"  name="credit" type="text" placeholder="<?php echo $creditos; ?>" id="creditinput">
        </div>
        <div class="two columns">
            <button class="button u-full-width" type="submit" name="bcredit"><i class="fa fa-floppy-o" aria-hidden="true"></i></button>
          </form>
        </div>
      <div>

      <div class="row">
        <div class="twelve columns">
          <form action="#" method="post">
            <label for="comment">Comment</label>
        </div>
      <div>
      
      <div class="row">
        <div class="ten columns">	
            <input class="u-full-width" name="comment" type="text" placeholder="<?php echo $comentario; ?>" id="commentinput">
        </div>
        <div class="two columns">
            <button class="button u-full-width" type="submit" name="bcomment"><i class="fa fa-floppy-o" aria-hidden="true"></i></button>
          </form>
      </div>
      </div>
      <br>
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
						<button class="button-primary u-full-width"  onclick="window.location.href ='./writeexif.php?image=<?php echo $image ?>'";>Clean EXIF</button>
					</div>
		  </div>
				</p>
        <div>
	</body>
</html>
