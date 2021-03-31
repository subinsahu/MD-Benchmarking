#!/bin/bash
#SBATCH -N 1 --ntasks-per-node 16
#SBATCH -t 0:10:00
#SBATCH -p RM


module load gcc
source /jet/home/susa/pkgs/gromacs/2020.5/bin/GMXRC

export GMX_MAXBACKUP=-1  # do not make back-ups
export GMX_MAXCONSTRWARN=-1


#gmx grompp -f ../prod.mdp -p ../itw_large.top -c ../prod_0.gro -o prod

gmx mdrun -v -s prod.tpr -o prod -g nt16_nopm1.log -nt 16  -ntomp 1



