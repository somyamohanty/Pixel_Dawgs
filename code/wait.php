<!DOCTYPE html>

<html>
<script src="http://code.jquery.com/jquery-2.1.0.min.js"></script>


<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
<title>Untitled 1</title>
</head>

<body>

<?php
$username = "ncr55";
$password = "ab1234";
$hostname = "localhost";

$mysqli = new mysqli($hostname, $username, $password, $username);

if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

$query = "SELECT nextimg FROM next";
$result = $mysqli->query($query);
$row = $result->fetch_assoc();
//echo $row['nextimg'];

$query = "SELECT imgid, tag1, tag2, tag3, tag4, tag5 FROM image where ind = ".$row['nextimg'];
//echo $query;
$result = $mysqli->query($query);
$row = $result->fetch_assoc();
//echo $row['imgid'].$row['tag1'].$row['tag2'].$row['tag3'].$row['tag4'].$row['tag5'];
?>

<script>
var tag1 = "";
var tag2 = "";
var tag3 = "";
var tag4 = "";
var tag5 = "";

var offset ;
var relativeX ;
var relativeY ;
</script>

<script>
function myFunctiontg1() {	
	tag1 = relativeX+':'+relativeY+','+tag1;
	document.getElementById("tag1").innerHTML = tag1;
}

function myFunctiontg2() {	
	tag2 = relativeX+':'+relativeY+','+tag2;
	document.getElementById("tag2").innerHTML = tag2;
}

function myFunctiontg3() {	
	tag3 = relativeX+':'+relativeY+','+tag3;
	document.getElementById("tag3").innerHTML = tag3;
}
function myFunctiontg4() {	
	tag4 = relativeX+':'+relativeY+','+tag4;
	document.getElementById("tag4").innerHTML = tag4;
}
function myFunctiontg5() {	
	tag5 = relativeX+':'+relativeY+','+tag5;
	document.getElementById("tag5").innerHTML = tag5;
}
function myFunctionsave() {	
	window.location.href = "addentry.php?tag1="+String(tag1)
					+"&tag2="+String(tag2)
					+"&tag3="+String(tag3)
					+"&tag4="+String(tag4)
					+"&tag5="+String(tag5);
}

</script>

<script>

$(function() {
$("#test").click(function(e) {
  //offset = $(this).offset();
  relativeX = (e.pageX );
  relativeY = (e.pageY);
  //alert(relativeX+':'+relativeY);
  //$(".position").val("afaf");
  document.getElementById("demo").innerHTML = relativeX+':'+relativeY;
});
});
   </script>

<a id="test" >
	<?php echo "<img src='http://127.0.0.1/".$row['imgid']."_segmented.jpg' style='border-style:none;position:relative;top:-8px;left:-8px;' alt='error'/>"; ?>
</a>
<?php echo "<img src='http://127.0.0.1/".$row['imgid'].".jpg' style='border-style:none;position:relative;top:-8px;left:-8px;' alt='error'/>"; ?>

<table>
  <tr>
    <td>
	<p id="demo">Is this the end of the world?</p>
	<button onclick="myFunctiontg1()" type="button"><?php echo $row['tag1']; ?></button> <p id="tag1"></p>
	<button onclick="myFunctiontg2()" type="button"><?php echo $row['tag2']; ?></button> <p id="tag2"></p>
	<button onclick="myFunctiontg3()" type="button"><?php echo $row['tag3']; ?></button> <p id="tag3"></p>
	<button onclick="myFunctiontg4()" type="button"><?php echo $row['tag4']; ?></button> <p id="tag4"></p>
	<button onclick="myFunctiontg5()" type="button"><?php echo $row['tag5']; ?></button> <p id="tag5"></p>
	<button onclick="myFunctionsave()" type="button">Save</button> 
    </td>
  </tr>
</table>


</body>
</html>
