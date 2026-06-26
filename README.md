# 🐵 G1 Monkey - AMP Training for Unitree G1 Humanoid

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/YOUR_USERNAME/g1_monkey)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Isaac Lab](https://img.shields.io/badge/Isaac_Lab-1.0+-orange)](https://isaac-sim.github.io/IsaacLab/)

This package provides an **Adversarial Motion Priors (AMP)** training environment for the **Unitree G1 humanoid robot** in Isaac Lab. Train humanoid robots to perform natural, human-like locomotion using reinforcement learning and motion capture data.

---

## 📋 **Table of Contents**

- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Training](#-training)
- [Testing](#-testing--evaluation)
- [Monitoring](#-monitoring-training)
- [Configuration](#-configuration)
- [Package Structure](#-package-structure)
- [Performance & Hardware](#-performance--hardware-requirements)
- [Troubleshooting](#-troubleshooting)
- [Advanced Usage](#-advanced-usage)
- [Contributing](#-contributing)
- [Citation](#-citation)
- [License](#-license)
- [Contact](#-contact--support)

---

## 📋 **Prerequisites**

Before installing G1 Monkey, ensure you have:

- **Isaac Lab** installed and working ([Installation Guide](https://isaac-sim.github.io/IsaacLab/))
- **Linux/Ubuntu 20.04+** (Required for Isaac Sim)
- **Python 3.10+** (Included with Isaac Lab)
- **NVIDIA GPU** with CUDA support:
  - Minimum: RTX 3060 (12GB VRAM)
  - Recommended: RTX 3090/4090 (24GB VRAM) or A100
- **CUDA 11.8+** and appropriate NVIDIA drivers
- **16GB+ RAM** (32GB recommended)
- **50GB+ free disk space**

### **Verify Isaac Lab Installation**

```bash
# Check Isaac Lab is working
cd /path/to/IsaacLab
./isaaclab.sh -p -c "import omni.isaac.lab; print('Isaac Lab OK')"


