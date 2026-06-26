"""
G1 Monkey - Adversarial Motion Priors for Unitree G1 Humanoid.

This package implements AMP (Adversarial Motion Priors) training for the Unitree G1
humanoid robot using NVIDIA Isaac Lab.
"""

from .assets import G1_CFG
from .configs import G1AmpEnvCfg

__all__ = ["G1_CFG", "G1AmpEnvCfg"]
__version__ = "0.1.0"
