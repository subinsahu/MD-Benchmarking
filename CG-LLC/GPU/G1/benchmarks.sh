#!/bin/bash
out='benchmarks.txt'
printf ".........................\n\n" > $out
fls=`ls *.log`
for fl in $fls; do
    grep "selected for this" $fl >> $out
    grep "MPI rank" $fl | tail -1 >> $out
    tail -3 $fl | awk '$1=="Performance:" {printf "%.1f ns/day", $2}' >> $out
    printf "\n.........................  \n\n" >> $out
done
cat $out



list='benchmarks.dat'
printf '#MPI \t ns/day\n' > temp.dat

awk '($3=="MPI") {printf "%d \t", $2}
     ($2=="ns/day") {printf "%.1f \n", $1}' $out >> temp.dat

sort -nk1 temp.dat  > $list

cat $list

