<html>
<head>
	<title>Hackathon</title>
	<meta charset="utf-8">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<link href="styles/style.css" rel='stylesheet' type="text/css" media="all">
</head>
<body>
	<?php
		$directory = "frames/Nouveau dossier";
		$images = glob($directory . "/*.png");
	?>
	<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div id="custCarousel" class="carousel slide" data-ride="carousel" align="center">
                <!-- slides -->
                <div class="carousel-inner">
					<?php
						for($i = 0; $i < count($images); ++$i) {
						  echo "<div id='carousel-item-$i' class='carousel-item'> <img src='$images[$i]'> </div>";
						}
					?>
                </div> <!-- Left right --> <a class="carousel-control-prev" href="#custCarousel" data-slide="prev"> <span class="carousel-control-prev-icon"></span> </a> <a class="carousel-control-next" href="#custCarousel" data-slide="next"> <span class="carousel-control-next-icon"></span> </a> <!-- Thumbnails -->
                <ol class="carousel-indicators list-inline">
					<?php
						for($i = 0; $i < count($images); ++$i) {
						  echo "<li id='list-inline-item-$i' class='list-inline-item'> <a class='image' id='carousel-selector-$i' data-slide-to='$i' data-target='#custCarousel'> <img src='$images[$i]' class='img-fluid'> </a> </li>";
						}
					?>
                </ol>
            </div>
        </div>
    </div>
	</div>
	
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
	<script>
	<?php
		for($i = 0; $i < count($images); ++$i) {
			echo "$('#list-inline-item-$i').hover(
				()=>{
					$('.carousel-item').removeClass('active');
					$('.list-inline-item').removeClass('active');
					$('#carousel-item-$i').addClass('active');
					$('#list-inline-item-$i').addClass('active');
				}
			);";
		}
	?>
	</script>
	<script src="jquery-3.6.0.min.js"></script>
</body>
</html>