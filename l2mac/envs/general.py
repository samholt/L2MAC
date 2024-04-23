import random

import numpy as np

from l2mac.config import L2MACConfig
from l2mac.utils.run import Domain


def get_env(domain: Domain, config: L2MACConfig, logger, seed: int):
    if domain == Domain.codebase:
        return GeneralEnvironment(config=config, logger=logger, seed=seed, env_name="Codebase")
    elif domain == Domain.book:
        return GeneralEnvironment(config=config, logger=logger, seed=seed, env_name="Book")
    else:
        raise Exception(
            f'Domain {domain} environment not found, please use "codebase" or "book", or implement a new domain for your task.'
        )


class Environment:
    def __init__(self, config, logger, env_name, seed):
        self.config = config
        self.logger = logger
        self.env_name = env_name
        self.seed = seed

    def log(self, message):
        if self.logger is not None:
            self.logger.info(f"[Environment: {self.env_name}] {message}")

    def reset(self):
        pass

    def step(self, action):
        pass


class GeneralEnvironment(Environment):
    def __init__(self, config, logger, seed, env_name="Codebase"):
        super().__init__(config, logger, env_name, seed)
        self.seed = None
        self.description = None
        self.attribute_names = None
        self.prepend_code_libraries = ""

    def set_seed(self, seed):
        self.seed = seed
        random.seed(seed)
        np.random.seed(seed)

    def reset(self):
        pass

    def get_obs(self):
        pass
