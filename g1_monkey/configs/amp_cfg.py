"""
Task registration and configuration for G1 AMP environment.
"""

import gymnasium as gym
from omni.isaac.lab_tasks.utils import parse_env_cfg
from .amp_env import G1AmpEnvCfg

##
# Register Gym Environment
##

gym.register(
    id="Isaac-G1-Amp-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": G1AmpEnvCfg,
        "rsl_rl_cfg_entry_point": "g1_monkey.configs.agents.rsl_rl_ppo_cfg:G1AmpPPORunnerCfg",
    },
)

def register_g1_amp_task():
    """Convenience function to register task."""
    pass  # Registration happens on import
