"""
G1 Humanoid Robot Configuration for Isaac Lab.

IMPORTANT: When you transfer to Isaac Lab PC, check which USD path exists:
  1. Run: python scripts/check_g1_usd.py
  2. Uncomment the correct usd_path below
"""

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR

##
# Configuration for Unitree G1 Humanoid
##

G1_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        # ============================================================
        # CHOOSE ONE USD PATH (uncomment when you find the right one)
        # ============================================================
        
        # OPTION 1: G1 in Isaac Lab official assets (check first!)
        usd_path=f"{ISAAC_NUCLEUS_DIR}/Robots/Unitree/G1/g1.usd",
        
        # OPTION 2: G1 in local extensions
        # usd_path="${USER_PATH_TO_ISAACLAB}/source/extensions/omni.isaac.lab_assets/data/Robots/Unitree/G1/g1.usd",
        
        # OPTION 3: Custom G1 USD you downloaded
        # usd_path="C:/Users/YourName/Downloads/g1_robot/g1.usd",
        
        # OPTION 4: Temporary - Use Go2 quadruped as placeholder for testing
        # usd_path=f"{ISAAC_NUCLEUS_DIR}/Robots/Unitree/Go2/go2.usd",
        
        # ============================================================
        
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 1.0),  # Spawn 1 meter above ground
        joint_pos={
            # G1 has 37 DoF - all start at neutral position
            ".*": 0.0,
        },
        joint_vel={
            ".*": 0.0,
        },
    ),
    actuators={
        # Leg actuators (hip, knee, ankle)
        "legs": ImplicitActuatorCfg(
            joint_names_expr=[".*_hip_.*", ".*_knee_.*", ".*_ankle_.*"],
            stiffness=80.0,
            damping=4.0,
            effort_limit=300.0,
            velocity_limit=10.0,
        ),
        # Torso and arm actuators
        "upper_body": ImplicitActuatorCfg(
            joint_names_expr=["torso_.*", ".*_shoulder_.*", ".*_elbow_.*"],
            stiffness=40.0,
            damping=2.0,
            effort_limit=100.0,
            velocity_limit=10.0,
        ),
    },
)
