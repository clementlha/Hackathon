<html>
<head>
	<title>Hackathon</title>
	<meta charset="utf-8">
	<link href="styles/style.css" rel='stylesheet' type="text/css" media="all">
</head>
<body>
	<?php
		$directory = "frames/Nouveau dossier";
		$images = glob($directory . "/*.png");
		foreach($images as $image)
		{
		  echo "<img src='$image'>";
		}
	?>
</body>
</html>