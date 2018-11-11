#!/bin/bash
\g++ cont.cpp -std=c++14 -o cont
time ./cont < example/example_01_in.txt > result.txt
cat result.txt
