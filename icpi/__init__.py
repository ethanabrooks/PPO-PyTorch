from gym.envs.registration import register

# # ICPI
# # ----------------------------------------

# elif env_id == "chain":
#     env = TimeLimit(
#         chain.Env(d=1, data=data, goal=4, n=8, random_seed=seed, hint=hint),
#         max_episode_steps=8,
#     )
register(
    "chain-v0",
    entry_point="icpi.base:create",
    kwargs={
        "entry_point": "icpi.chain:Env",
        "d": 1,
        "goal": 4,
        "n": 8,
        "random_seed": 0,
        "max_episode_steps": 8,
    },
)
# elif env_id == "distractor-chain":
#     env = TimeLimit(
#         chain.Env(d=2, data=data, goal=4, n=8, random_seed=seed, hint=hint),
#         max_episode_steps=8,
#     )
register(
    "distractor-chain-v0",
    entry_point="icpi.base:create",
    kwargs={
        "entry_point": "icpi.chain:Env",
        "d": 2,
        "goal": 4,
        "n": 8,
        "random_seed": 0,
        "max_episode_steps": 8,
    },
    max_episode_steps=8,
)
# elif env_id == "maze":
#     env = TimeLimit(
#         maze.Env(data=data, hint=hint, random_seed=seed), max_episode_steps=8
#     )
register(
    "maze-v0",
    entry_point="icpi.base:create",
    kwargs={"entry_point": "icpi.maze:Env", "random_seed": 0, "max_episode_steps": 8},
)
# elif env_id == "mini-catch":
#     env = catch.Wrapper(
#         data=data, env=catch.Env(columns=4, rows=5, seed=seed), hint=hint
#     )
register(
    "mini-catch-v0",
    entry_point="icpi.base:create",
    kwargs={
        "entry_point": "icpi.catch:Env",
        "columns": 4,
        "rows": 5,
        "seed": 0,
        "max_episode_steps": 100,
    },
)
# elif env_id == "point-mass":
#     max_steps = 8
#     env = TimeLimit(
#         point_mass.Env(
#             data=data,
#             hint=hint,
#             max_distance=6,
#             _max_trajectory=max_steps,
#             pos_threshold=2,
#             random_seed=seed,
#         ),
#         max_episode_steps=max_steps,
#     )
register(
    "point-mass-v0",
    entry_point="icpi.base:create",
    kwargs={
        "entry_point": "icpi.point_mass:Env",
        "max_distance": 6,
        "_max_trajectory": 8,
        "pos_threshold": 2,
        "random_seed": 0,
        "max_episode_steps": 8,
    },
)
# elif env_id == "space-invaders":
#     env = space_invaders.Env(
#         data=data,
#         width=4,
#         height=5,
#         n_aliens=2,
#         random_seed=seed,
#         hint=hint,
#     )
register(
    "space-invaders-v0",
    entry_point="icpi.base:create",
    kwargs={
        "entry_point": "icpi.space_invaders:Env",
        "width": 4,
        "height": 5,
        "n_aliens": 2,
        "random_seed": 0,
        "max_episode_steps": 100,
    },
)
