"""
Training script for G1 AMP locomotion using Isaac Lab.

This launches Isaac Sim and trains the G1 robot to walk using AMP.
"""

import argparse
from omni.isaac.lab.app import AppLauncher

# Parse arguments
parser = argparse.ArgumentParser(description="Train G1 with AMP")
parser.add_argument("--num_envs", type=int, default=2048, help="Number of parallel environments")
parser.add_argument("--task", type=str, default="Isaac-Amp-G1-v0", help="Task name")
parser.add_argument("--headless", action="store_true", default=False, help="Run headless (no GUI)")
parser.add_argument("--video", action="store_true", default=False, help="Record video")
parser.add_argument("--max_iterations", type=int, default=10000, help="Max training iterations")

args_cli = parser.parse_args()

# Launch Isaac Sim
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

# --- After Isaac Sim launches, import everything else ---
import gymnasium as gym
import os
import torch

import omni.isaac.lab_tasks  # Registers all tasks
from omni.isaac.lab_tasks.utils import parse_env_cfg
from omni.isaac.lab_tasks.utils.wrappers.rsl_rl import RslRlVecEnvWrapper

import g1_monkey.config.amp_cfg  # Registers G1 task

# Import RSL-RL for training
from rsl_rl.runners import OnPolicyRunner


def main():
    """Main training loop."""
    
    print("\n" + "="*60)
    print("🚀 G1 AMP Training with Isaac Lab")
    print("="*60)
    
    # Create environment
    env = gym.make(args_cli.task, num_envs=args_cli.num_envs)
    
    # Wrap environment for RSL-RL
    env = RslRlVecEnvWrapper(env)
    
    print(f"✅ Created {args_cli.num_envs} parallel G1 environments")
    print(f"📊 Observation space: {env.num_obs}")
    print(f"🎮 Action space: {env.num_actions}")
    
    # Load training config
    agent_cfg = parse_env_cfg(args_cli.task, use_gpu=True)
    
    # Create output directory
    log_dir = os.path.join("logs", "g1_monkey_amp")
    os.makedirs(log_dir, exist_ok=True)
    
    print(f"📁 Logs will be saved to: {log_dir}")
    
    # Create trainer
    runner = OnPolicyRunner(env, agent_cfg, log_dir=log_dir, device="cuda:0")
    
    print("\n🎓 Starting training...")
    print(f"⏱️  Max iterations: {args_cli.max_iterations}")
    print(f"💾 Checkpoints saved every 50 iterations")
    
    # Train
    runner.learn(num_learning_iterations=args_cli.max_iterations, init_at_random_ep_len=True)
    
    print("\n✅ Training complete!")
    print(f"📦 Model saved in: {log_dir}")
    
    # Cleanup
    env.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise
    finally:
        simulation_app.close()
