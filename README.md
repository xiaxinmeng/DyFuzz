# DyFuzz
A prototype tool to test interpreter by fuzzing built-in library. 

# Environment: Python3.9.2, Ubuntu 16.04


Usage of the tool:
1. cd DyFuzz 
2. python3 run.py


If you want to reproduce the found bugs, try:
1. cd DyFuzz
2. python3 run_experiment.py

The crashing examples are store in a directory "error".
In each crashing file, each line represents an argument. The last line is the API call. The API call is something like nis.map(paramlist[0]). Replace paramlist[0] with the provided arguments and then you can reproduce the crashing.

If you can't reproduce our bugs, try running it again since our approach is based on random mutation. 
