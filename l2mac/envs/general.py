"""
This module provides the implementation of environments for the L2MAC project.

Classes:
  Environment: A base class for creating different environments.
  GeneralEnvironment: A subclass of Environment tailored for general use cases.

Functions:
  get_env(domain: Domain, config: L2MACConfig, logger, seed: int): 
    Factory function to create and return an environment based on the specified
    domain.

Modules:
  random: Python's built-in module for generating random numbers.
  numpy (np): A fundamental package for scientific computing with Python.
  l2mac.config: Module containing configuration settings for L2MAC.
  l2mac.utils.run: Module containing utility functions for running L2MAC tasks.
"""
import random

import numpy as np

from l2mac.config import L2MACConfig
from l2mac.utils.run import Domain


def get_env(domain: Domain, config: L2MACConfig, logger, seed: int):
  if domain == Domain.CODEBASE:
    return GeneralEnvironment(config=config,
                              logger=logger,
                              seed=seed,
                              env_name="Codebase")
  elif domain == Domain.BOOK:
    return GeneralEnvironment(config=config,
                              logger=logger,
                              seed=seed,
                              env_name="Book")
  else:
    raise ValueError(
        f'Domain {domain} environment not found, please use "codebase" or '
        '"book", or implement a new domain for your task.'
    )


class Environment:
  """
  A class to represent a general environment.
  Attributes:
  -----------
  config : dict
    Configuration settings for the environment.
  logger : logging.Logger
    Logger instance for logging environment messages.
  env_name : str
    Name of the environment.
  seed : int
    Seed for random number generation to ensure reproducibility.
  Methods:
  --------
  log(message):
    Logs a message with the environment name if a logger is provided.
  reset():
    Resets the environment to an initial state.
  step(action):
    Takes an action in the environment and returns the result.
  """
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
  """
  GeneralEnvironment is a subclass of the Environment class designed to provide
    a general-purpose environment for various applications.
  Attributes:
    seed (int): The seed value for random number generation to ensure
      reproducibility.
    description (str): A description of the environment.
    attribute_names (list): A list of attribute names relevant to the
      environment.
    prepend_code_libraries (str): A string containing code libraries to be
      prepended.
  Methods:
    __init__(config, logger, seed, env_name="Codebase"):
      Initializes the GeneralEnvironment with the given configuration, logger,
        seed, and environment name.
    set_seed(seed):
      Sets the seed for random number generation to ensure reproducibility.
    reset():
      Resets the environment to its initial state.
    get_obs():
      Retrieves the current observation from the environment.
  """
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
