"""
Script to prepare AMP motion data for G1 robot training.

This creates mock motion capture data. In production, you'd use real mocap data.
"""

import os
import numpy as np

def generate_mock_amp_data():
    """
    Generate synthetic motion data for AMP training.
    
    In production, replace this with:
    - Real motion capture data from G1 robot
    - Retargeted human motion data
    - Physics-based reference trajectories
    """
    
    # Create data directory
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data", "amp_motions")
    os.makedirs(data_dir, exist_ok=True)
    
    print(f"📁 Creating AMP motion data in: {data_dir}")
    
    # AMP observation spec for G1 (78 dimensions):
    # - 37 joint positions (G1 has 37 DoFs)
    # - 37 joint velocities
    # - 3 base linear velocity
    # - 1 z-position (height)
    
    num_frames = 1000  # 1000 timesteps of motion
    obs_dim = 78       # Total observation dimension
    
    # Generate synthetic walking motion
    # In real use: load from .npy, .bvh, or motion capture system
    motion_data = np.random.randn(num_frames, obs_dim).astype(np.float32)
    
    # Add some structure to make it more realistic
    for i in range(num_frames):
        # Simulate periodic leg motion (simple sine wave)
        phase = 2 * np.pi * i / 100
        motion_data[i, 0:10] = np.sin(phase + np.linspace(0, np.pi, 10))
        motion_data[i, 37:47] = np.cos(phase + np.linspace(0, np.pi, 10))
    
    # Save the motion data
    output_path = os.path.join(data_dir, "g1_walk.npy")
    np.save(output_path, motion_data)
    
    print(f"✅ Saved {num_frames} frames to: {output_path}")
    print(f"📊 Data shape: {motion_data.shape}")
    print(f"📐 Observation dimensions: {obs_dim}")
    print("\n🎯 Next step: Run train_amp.py to train the policy!")

if __name__ == "__main__":
    generate_mock_amp_data()
