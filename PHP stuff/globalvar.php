<?php

$owo = 3

function add_2 () {
	global $owo;
	$owo += 2;
}

add_2();
echo $owo;
?>