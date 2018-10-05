<?php
$db = mysqli_connect("localhost", "root", "", "productmanager");
$beta = false;
if(!$db) {
	echo "Błąd łączenia z bazą danych</br>" . PHP_EOL;
	if($beta) {
		echo "Error: " . mysqli_connect_errno() ." " . mysqli_connect_error() . PHP_EOL;
	}
	echo "</br>";
	exit;
}
$db->set_charset("utf8");

?>