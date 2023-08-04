import datetime
import time
from typing import Optional
from ray import tune
from ray.air.integrations.wandb import setup_wandb
import wandb
import urllib

from train import train


from dollar_lambda import command

project = "icpi"
param_space = {
    "lr_actor": tune.grid_search([0.005, 0.002, 0.001]),
    "lr_critic": tune.grid_search([0.001, 0.0005, 0.0001]),
    "hidden_dim": tune.grid_search([256, 512, 1024]),
    "num_layers": tune.grid_search([0, 1]),
}


@command()
def sweep(env_name: str, gpus_per_proc: float = 0.1, notes: Optional[str] = None):
    timestamp = datetime.datetime.now().strftime("-%d-%m-%H:%M:%S")
    group = f"{env_name}-{timestamp}"

    def train_func(params):
        sleep_time = 1
        while True:
            try:
                run = setup_wandb(
                    config=params,
                    group=group,
                    project=project,
                    rank_zero_only=False,
                    notes=notes,
                )
                break
            except wandb.errors.CommError:
                time.sleep(sleep_time)
                sleep_time *= 2
        print(
            f"wandb: ️👪 View group at {run.get_project_url()}/groups/{urllib.parse.quote(group)}/workspace"
        )
        import icpi

        return train.function(env_name=env_name, run=run, **params)

    tune.Tuner(
        trainable=tune.with_resources(train_func, dict(gpu=gpus_per_proc)),
        param_space=param_space,
    ).fit()


if __name__ == "__main__":
    sweep()
