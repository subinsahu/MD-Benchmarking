#!/bin/bash

out='benchmarks.txt'
printf ".........................\n\n" > $out
fls=`ls *.log`
for fl in $fls; do
    grep "MPI process" $fl | head -1 >> $out
    tail -3 $fl | awk '$1=="Performance:" {printf "%.1f ns/day", $2}' >> $out
    printf "\n.........................  \n\n" >> $out
done

cat $out

