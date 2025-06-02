import numpy as np
import pandas as pd
import numba, timeit, os

# get number of threads from sbatch parameters if on HPC cluster
numba.set_num_threads(int(os.getenv("SLURM_CPUS_PER_TASK", 1)))
# set number of threads below and comment line above if on your own PC
#numba.set_num_threads(6)
stuff = pd.DataFrame(np.random.rand(250000,6), columns=['a','b','c','d','e','f'])
print(stuff.info())
# if in Jupyter, uncomment 2 lines starting with % and comment out all lines after them
#%timeit stuff.rolling(500).mean()
#%timeit stuff.rolling(500).mean(engine='numba', engine_kwargs={"parallel": True})
n_loops = 10
repeats = 10
serial_times = timeit.repeat('stuff.rolling(500).mean()',
                             number=n_loops, globals={'stuff': stuff})
numba_times = timeit.repeat('stuff.rolling(500).mean(engine="numba", engine_kwargs={"parallel": True})',
                            number=n_loops, globals={'stuff': stuff})
print("Mean serial code time: ", 1000*np.mean([t/n_loops for t in serial_times]), " ms")
print("Mean Numba code time: ", 1000*np.mean([t/n_loops for t in numba_times[1:]]), " ms")
# 1st numba iteration is longer, so we cut it