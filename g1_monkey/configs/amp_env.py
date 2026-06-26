"""
Environment configuration for G1 Humanoid with Adversarial Motion Priors (AMP).
"""

import math
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.envs import ManagerBasedRLEnvCfg
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sim import SimulationCfg
from omni.isaac.lab.terrains import TerrainImporterCfg
from omni.isaac.lab.managers import ObservationGroupCfg as ObsGroup
from omni.isaac.lab.managers import ObservationTermCfg as ObsTerm
from omni.isaac.lab.managers import ActionTermCfg as ActionTerm
from omni.isaac.lab.managers import RewardTermCfg as RewTerm
from omni.isaac.lab.managers import TerminationTermCfg as DoneTerm
from omni.isaac.lab.managers import EventTermCfg as EventTerm

from g1_monkey.assets import G1_CFG

##
# Scene Configuration
##

@configclass
class G1SceneCfg(InteractiveSceneCfg):
    """Scene configuration for G1 on flat terrain."""
    
    # Terrain
    terrain = TerrainImporterCfg(
        prim_path="/World/ground",
        terrain_type="plane",
        collision_group=-1,
        physics_material=None,
    )
    
    # Robot
    robot: G1_CFG = G1_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

##
# Environment Configuration
##

@configclass
class G1AmpEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for G1 AMP environment."""
    
    # Scene settings
    scene: G1SceneCfg = G1SceneCfg(num_envs=4096, env_spacing=4.0)
    
    # Simulation settings
    sim: SimulationCfg = SimulationCfg(
        dt=1.0 / 120.0,
        substeps=1,
        physx=SimulationCfg.PhysXCfg(
            bounce_threshold_velocity=0.2,
            gpu_max_rigid_contact_count=2**23,
            gpu_max_rigid_patch_count=2**23,
        ),
    )
    
    # Observations
    observations: ObsGroup = ObsGroup(
        policy=ObsGroup(
            # Base state
            base_lin_vel=ObsTerm(func="base_lin_vel"),
            base_ang_vel=ObsTerm(func="base_ang_vel"),
            projected_gravity=ObsTerm(func="projected_gravity"),
            
            # Joint state
            joint_pos=ObsTerm(func="joint_pos_rel"),
            joint_vel=ObsTerm(func="joint_vel_rel"),
            
            # Actions
            actions=ObsTerm(func="last_action"),
        )
    )
    
    # Actions
    actions: ActionTerm = ActionTerm(
        func="joint_position_action",
        asset_name="robot",
    )
    
    # Rewards
    rewards: RewTerm = RewTerm()
    
    # Terminations
    terminations: DoneTerm = DoneTerm(
        time_out=DoneTerm(func="time_out", time_out=True),
        base_contact=DoneTerm(func="illegal_contact", params={"sensor_cfg": SceneEntityCfg("robot")}),
    )
    
    # Events (for domain randomization)
    events: EventTerm = EventTerm()
    
    def __post_init__(self):
        """Post initialization."""
        self.decimation = 4
        self.episode_length_s = 10.0
        self.viewer.eye = (7.5, 7.5, 7.5)
        self.viewer.lookat = (0.0, 0.0, 0.0)
