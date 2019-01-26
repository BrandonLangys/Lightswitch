<?php
$num =  $_GET['num']; //gets the number




$f = fopen('text.txt' , 'w') or die("Unable to open file"); //open the text file to write

fwrite($f, $num); //writes either 1 or 0

sleep(5);


fclose($f); //closes the file

header(''); //send page back to local host
?>