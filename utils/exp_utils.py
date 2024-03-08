import time
import random
import torch
import numpy as np
from omegaconf import DictConfig, OmegaConf
from scipy.integrate import solve_ivp
from functools import partial
from collections import deque
from tqdm import tqdm
import shelve

def seed_all(seed=None):
    """
    Set the torch, numpy, and random module seeds based on the seed
    specified in config. If there is no seed or it is None, a time-based
    seed is used instead and is written to config.
    """
    # Default uses current time in milliseconds, modulo 1e9
    if seed is None:
        seed = round(time() * 1000) % int(1e9)

    # Set the seeds using the shifted seed
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)

def config_to_dict(config):
    """
    Convert a config object to a dictionary.
    """
    return OmegaConf.to_container(config, resolve=True)

def dict_to_config(d):
    """
    Convert a dictionary to a config object.
    """
    return OmegaConf.create(d)

class DotDict(dict):
    def __getattr__(self, name):
        return self.get(name, None)
    
    def __setattr__(self, name, value):
        self[name] = value

def to_dot_dict(d):
    dot_dict = DotDict()
    for key, value in d.items():
        if isinstance(value, dict):
            dot_dict[key] = to_dot_dict(value)
        else:
            dot_dict[key] = value
    return dot_dict