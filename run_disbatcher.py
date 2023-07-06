#!/usr/bin/env python

from pathlib import Path

from disbatchc.disBatch import DisBatcher

AMIN = 0
AMAX = 6
BMIN = 100
BMAX = 160

SEEDS = [0, 123456, 654321, 3333, 958666764, 635830919, 82, 50438]

SRCDIR = Path(__file__).parent.resolve()
OUTDIR = Path('/mnt/home/lgarrison/ceph/dynamic-disBatch/')

SCRIPT = Path(SRCDIR / 'do_work.py')


def get_task(A, B, i):
    '''
    Generate a task for parameters A and B, with seed index i.
    '''
    if i >= len(SEEDS):
        print(f'Warning: exceed max retry count for {A=} {B=}')
        return None
    
    jobdir = OUTDIR / f'{A}_{B}'
    prefix = f'mkdir -p {jobdir}; cd {jobdir}'
    cmd = f'{prefix}; python {SCRIPT} --seed={SEEDS[i]} {A} {B} &> {i}.log'
    task = dict(A=A, B=B, i=i, cmd=cmd)
    return task


def main():
    disbatcher = DisBatcher(tasksname='dynamic-disBatch')

    # Submit all the tasks with the first seed
    tasks = []
    for A in range(AMIN, AMAX, 2):
        for B in range(BMIN, BMAX, 20):
            task = get_task(A, B, 0)
            disbatcher.submit(task['cmd'])
            tasks += [task]

    # Wait for tasks to complete. Resubmit as necessary.
    njob = len(tasks)
    ndone = 0
    while ndone < njob:
        status = disbatcher.wait_one_task()
        print(status)
        if status['ReturnCode'] in (74, 84):
            # resubmit with new seed
            oldtask = tasks[status['TaskId']]
            newi = oldtask['i'] + 1
            
            newtask = get_task(oldtask['A'], oldtask['B'], newi)
            if newtask is None:
                continue
            disbatcher.submit(newtask['cmd'])
            tasks += [newtask]
        else:
            # done task
            ndone += 1
    
    disbatcher.done()


if __name__ == '__main__':
    main()
