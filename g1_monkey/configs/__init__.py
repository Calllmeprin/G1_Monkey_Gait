"""
Environment and task configurations for G1 AMP training.
"""

from .amp_cfg import register_g1_amp_task
from .amp_env import G1AmpEnvCfg

__all__ = ["G1AmpEnvCfg", "register_g1_amp_task"]
