#! /bin/bash

rm times
for fname in th_diff.block0.out1.*.tab
do 
    head -n 1 $fname >> times
done