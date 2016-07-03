<?php
    $n = trim(fgets(STDIN));
    $arr = explode(" ", trim(fgets(STDIN)));
    $dp = array(0, abs($arr[1] - $arr[0]));
    for($i = 2; $i < $n; $i++) {
        $dp[] = min(
            $dp[$i-2] + abs($arr[$i] - $arr[$i-2]),
            $dp[$i-1] + abs($arr[$i] - $arr[$i-1]));
    }
    $dp[$n-1] = min($dp[$n-1], $dp[$n-2] + abs($arr[$n-2] - $arr[$n-1]));
    echo $dp[$n-1], "\n";
