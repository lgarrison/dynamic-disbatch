import click
import torch

@click.command
@click.argument('A', type=int)
@click.argument('B', type=int)
@click.option('--seed', type=int)
def main(a, b, seed):
    print(f'Hello from job {a=} {b=} {seed=}')
    print(f'{torch.cuda.device_count()=}')

    if a == 4 and b == 140 and seed != 50438:
        exit(74)

if __name__ == '__main__':
    main()
