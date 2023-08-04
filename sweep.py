from ray import tune

from train import train


from dollar_lambda import command


@command()
def main(env_name: str, gpus_per_proc: float = 0.1):
    def train_func(config: dict):
        import icpi

        return train.function(env_name=env_name, **config)

    tuner = tune.Tuner(
        trainable=tune.with_resources(train_func, dict(gpu=gpus_per_proc)),
        param_space={
            "lr_actor": tune.grid_search([0.001, 0.0001, 0.0003]),
            "lr_critic": tune.grid_search([0.001, 0.0001, 0.0003]),
            "hidden_dim": tune.grid_search([64, 128, 256]),
            "num_layers": tune.grid_search([0, 1]),
        },
    )
    return tuner.fit()


if __name__ == "__main__":
    main()
