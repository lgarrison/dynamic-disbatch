# dynamic-disBatch

This is an example of using [disBatch's](https://github.com/flatironinstitute/disBatch) `DisBatcher` Python interface to submit tasks and dynamically resubmit them based on the return code. Each task uses 1 GPU.

## Organization

* `job.sbatch`: the main entry point; submit with `sbatch job.sbatch`
* `run_disbatcher.py`: invoked by `job.sbatch` to launch the tasks dynamically
* `do_work.py`: a dummy "science" script that takes a seed and some parameters, and uses 1 GPU
* `env.sh`: an example environment setup script, used by `job.sbatch`

## Usage
Modify the `OUTDIR` path in `run_disbatcher.py`. Logs from `do_work.py` will go there.

Submit with:
```console
$ sbatch job.sbatch
```

disBatch logs go in a directory named `job$SLURM_JOBID`. Some status information will be written into the `slurm-*.out` log.
