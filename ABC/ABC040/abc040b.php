<?php
    $i = trim(fgets(STDIN));
    $ans = $i - (int)pow((int)sqrt($i), 2);
    for($cnt = 1; $cnt < $i; $cnt++) {
        $t = abs((int)($i / $cnt) - $cnt);
        $ans = min($ans,  $t + $i - (int)($i / $cnt) * $cnt);
    }
    echo $ans, "\n";
