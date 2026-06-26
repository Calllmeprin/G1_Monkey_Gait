"""
Diagnostic script to find G1 USD file on Isaac Lab PC.
Run this FIRST on your Isaac Lab machine!
"""

import os
from pathlib import Path

def find_g1_usd():
    print("\n" + "="*60)
    print("🔍 Searching for G1 Robot USD files...")
    print("="*60 + "\n")
    
    # Check if Isaac Lab is installed
    try:
        from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR
        print(f"✅ Isaac Lab found!")
        print(f"📁 Nucleus directory: {ISAAC_NUCLEUS_DIR}\n")
        
        # Common paths to check
        search_paths = [
            os.path.join(ISAAC_NUCLEUS_DIR, "Robots", "Unitree"),
            os.path.join(os.getcwd(), "source", "extensions", "omni.isaac.lab_assets", "data", "Robots"),
        ]
        
        print("🔎 Checking these locations:\n")
        
        found_robots = []
        for search_path in search_paths:
            if os.path.exists(search_path):
                print(f"  📂 {search_path}")
                for root, dirs, files in os.walk(search_path):
                    for file in files:
                        if file.endswith(".usd") or file.endswith(".usda"):
                            full_path = os.path.join(root, file)
                            found_robots.append(full_path)
                            print(f"    ✓ {os.path.basename(file)}")
            else:
                print(f"  ❌ {search_path} (not found)")
        
        if found_robots:
            print(f"\n✅ Found {len(found_robots)} robot USD files!")
            print("\n🎯 Copy one of these paths to g1_cfg.py:")
            for robot in found_robots:
                if "g1" in robot.lower():
                    print(f"  🤖 [G1 FOUND!] {robot}")
                else:
                    print(f"     {robot}")
        else:
            print("\n⚠️  No USD files found!")
            print("   You may need to:")
            print("   1. Download G1 from Omniverse Exchange")
            print("   2. Convert from URDF")
            print("   3. Use Go2 as placeholder")
        
    except ImportError:
        print("❌ Isaac Lab not found on this PC!")
        print("   Run this script on your Isaac Lab machine.")

if __name__ == "__main__":
    find_g1_usd()
