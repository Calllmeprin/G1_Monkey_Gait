"""Installation script for g1_monkey package."""

from setuptools import setup, find_packages

setup(
    name="g1_monkey",
    version="0.1.0",
    description="Adversarial Motion Priors for Unitree G1 in Isaac Lab",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch",
    ],
    python_requires=">=3.10",
)
