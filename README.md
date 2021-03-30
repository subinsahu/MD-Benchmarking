# MD-Benchmarking
Scaling analysis and benchmarking of all-atom MD simulation on Bridges2.
The analysis are performed for GPU (using MPI and CUDA), CPU (with MPI), and CPU (with thread_MPI).
The system has 73,758 atoms with edge length ~9 nm in x,y, and z directions. Each benchmarking simulation is a 10 ps NPT run with 2fs time-step.
I tested scaling against MPI processes (-np), tMPI threads (-nt), openMP threads (-ntomp), GPUs (gres=gpu:x), and nodes (-N x).
Slurm job submission scripts have extention 'job'.
Once the jobs are complete, run 'benchmarks.sh' script to extract the benchmarking information from the log file. The script will print the
summary of the benchmarking each scaling test in the file 'benchmarks.txt' (eg: AA-LLC/CPU/test_np/benchmaks.txt). The script will also create a table of scaling in a file 'benchmarks.dat'. Finally, the scaling analysis can be plotted using the python script plot.py.
