<?php
  $conn = new mysqli('172.20.0.2', 'root', '96e5aca02ebf', 'tonghop');
  $query = "UPDATE users SET money=10000000 WHERE id= 38";
  $sth = $conn->query($query);
  echo $sth;
