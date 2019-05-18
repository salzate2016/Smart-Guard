<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>smartGuard</title>

  <!-- Bootstrap core CSS -->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="/startbootstrap-the-big-picture-gh-pages/blue.png" rel="stylesheet">

</head>

<body>

  <!-- Navigation -->
 

  <!-- Page Content -->
  <section>
    <div class="container">
      <div class="">
        <div class="">
          <center><h1>smartGuard</h1>
              <p>Doorbell access at your fingertips!</p></center>
        </div>
      </div>
    </div>
      <div class="">
          <center><img src="image.jpg" width="300" height="300">
		<form action="http://192.168.1.33:8081">
              <input type="submit" value="See Live Feed"></form></center>
      </div>
      <div class="">
        <center><b><font size = '20'>Door Controls:</b>       
         <form method="get" action="gpio.php">                 
                 <input type="submit" style = "font-size: 16 pt" value="Close Door" name="off">
                 <input type="submit" style = "font-size: 16 pt" value="Open Door" name="on">
                 
         </form>
         <?php
         shell_exec("/usr/local/bin/gpio -g mode 25 out");
         if(isset($_GET['off']))
         {
		echo "Door is Closed";
		shell_exec("/usr/local/bin/gpio -g write 25 0");
         }
	else if(isset($_GET['on']))
	{
		echo "Door is Opened";
		shell_exec("/usr/local/bin/gpio -g write 25 1");
	}
	else if(isset($_GET['blink']))
	{
		echo "LED is blinking";
		for($x = 0;$x<=4;$x++)
		{
			shell_exec("/usr/local/bin/gpio -g write 17 1");
			sleep(1);
			shell_exec("/usr/local/bin/gpio -g write 17 0");
			sleep(1);
		}
	}
        ?>
      </div>
  </section>

  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

</body>

</html>
