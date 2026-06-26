"""
Test script to verify package structure (without Isaac Lab dependencies).
"""

import os
import sys

print("=" * 60)
print("🔍 Testing G1 Monkey Package Structure...")
print("=" * 60)

# Check if package is installed
try:
    import g1_monkey
    package_path = os.path.dirname(g1_monkey.__file__)
    print(f"\n✅ Package found at: {package_path}")
except ImportError:
    print("\n❌ Package not installed! Run: pip install -e .")
    sys.exit(1)

# Check file structure
required_files = [
    "g1_monkey/__init__.py",
    "g1_monkey/assets/__init__.py",
    "g1_monkey/assets/g1_cfg.py",
    "g1_monkey/configs/__init__.py",
    "g1_monkey/configs/amp_cfg.py",
    "g1_monkey/configs/amp_env.py",
    "g1_monkey/configs/agents/__init__.py",
    "g1_monkey/configs/agents/rsl_rl_ppo_cfg.py",
]

print("\n📂 Checking file structure...")
all_exist = True
for file in required_files:
    full_path = os.path.join(os.getcwd(), file)
    if os.path.exists(full_path):
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ MISSING: {file}")
        all_exist = False

# Check scripts
print("\n📜 Checking scripts...")
script_files = [
    "scripts/prep_amp_g1.py",
    "scripts/train_amp.py",
    "scripts/check_g1_usd.py",
]

for script in script_files:
    full_path = os.path.join(os.getcwd(), script)
    if os.path.exists(full_path):
        print(f"   ✅ {script}")
    else:
        print(f"   ⚠️  MISSING: {script}")

# Check setup.py
print("\n⚙️  Checking setup files...")
if os.path.exists("setup.py"):
    print("   ✅ setup.py")
else:
    print("   ❌ MISSING: setup.py")
    all_exist = False

# Final verdict
print("\n" + "=" * 60)
if all_exist:
    print("🎉 SUCCESS! Package structure is correct!")
    print("=" * 60)
    print("\n📦 Next Steps:")
    print("   1. Copy entire 'g1_monkey' folder to Isaac Lab PC")
    print("   2. On Isaac Lab PC, run: pip install -e .")
    print("   3. Run training: python scripts/train_amp.py")
else:
    print("❌ INCOMPLETE! Fix missing files above.")
    print("=" * 60)

# Show what can't be tested locally
print("\n⚠️  NOTE: Cannot test Isaac Lab imports on this PC")
print("   These will be validated on the Isaac Lab PC:")
print("   - omni.isaac.lab imports")
print("   - G1 robot USD file")
print("   - Simulation environment")
