<?php
  $comment = $_POST["comment"];
  $tmp = exec("/path/to/python /path/to/python_script/shutdown_initiate.py $comment");
  echo "Success - " . $tmp
?>
