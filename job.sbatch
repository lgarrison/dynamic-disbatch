#!/bin/bash
#SBATCH -J dynamic-disBatch
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --partition=gpu
#SBATCH --gpus-per-task=1
#SBATCH -C h100
#SBATCH --cpus-per-task=16
#SBATCH --mem=1000G
#SBATCH --time=1-0

. env.sh
script=$(realpath run_disbatcher.py)

workdir=job$SLURM_JOBID
mkdir -p $workdir
cd $workdir

python $script
