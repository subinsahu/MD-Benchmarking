#!/bin/bash

list='benchmarks.dat'
printf '#GPU \t performance (ns/day) for nMPI=\n' > $list
printf '# \t 1*GPU \t 2*GPU \t 4*GPU\t 5*GPU\n' >> $list

for g in 1 2 4 8; do

awk -v g=$g 'BEGIN {printf "%d\t", g}
          ($1>=g){printf "%.1f \t", $2}
	  END{printf "\n"} ' G$g/benchmarks.dat >> $list
done




