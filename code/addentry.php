<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<title>Untitled 1</title>
</head>

<body>
<?php

	echo "<h1>Adding tag  co-ordinates to Database</h1>";
/*echo $_GET["tag1"]."</br>";
echo $_GET["tag2"]."</br>";
echo $_GET["tag3"]."</br>";
echo $_GET["tag4"]."</br>";
echo $_GET["tag5"];*/

$username = "svk38";
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
$inde = $row['nextimg'] + 1;
//echo $inde;

$query = "UPDATE image
SET tag1c = '".$_GET["tag1"]."', tag2c = '".$_GET["tag2"]."', tag3c = '".$_GET["tag3"]."', tag4c = '".$_GET["tag4"]."', tag5c = '".$_GET["tag5"]."' WHERE ind =".$row['nextimg'] ;
//echo $query;

if ($mysqli->query($query) === TRUE) {
    echo "coordinates added successfully<br/>";
} 
else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}


$query = "UPDATE  next SET  nextimg = ".$inde." WHERE  nextimg =".$row['nextimg']." LIMIT 1 ";
//echo $query;

if ($mysqli->query($query) === TRUE) {
    echo "next id updated successfully<br/>";
} 
else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

header('Location: http://pluto.cse.msstate.edu/~svk38/wait.php');

?>

</body>
</html>
