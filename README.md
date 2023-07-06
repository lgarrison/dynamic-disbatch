# dynamic-disBatch

This is an example of using [disBatch's](https://github.com/flatironinstitute/disBatch) `DisBatcher` Python interface to submit tasks and dynamically resubmit them based on the return code. Each task uses 1 GPU.

## Organization

* `job.sbatch`: the main entry point
* `run_disbatcher.py`: invoked by `job.sbatch` to launch the tasks dynamically
* `do_work.py`: a dummy "science" script that takes a seed and some parameters, and uses 1 GPU
