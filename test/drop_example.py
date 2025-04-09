"""
Simple example script to test type completions.
"""

import numpy as np
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})
from isaacsim.core.api import World
from isaacsim.core.api.objects import DynamicCuboid, DynamicCone, DynamicCylinder
from isaacsim.sensors.camera import Camera
import isaacsim.core.utils.numpy.rotations as rot_utils

world = World()
world.scene.add_default_ground_plane()  # type: ignore

camera = Camera(
    prim_path="/World/Camera",
    name="camera",
    position=(0, 0, 5),
    resolution=(640, 480),
    orientation=rot_utils.euler_angles_to_quats(np.array([0, 90, 0]), degrees=True)
)

cube1 = DynamicCuboid(
    prim_path="/World/Cube1",
    name="cube",
    position=(0, 0, 5),
    color=np.array([255, 0, 0]),
)
cube2 = DynamicCuboid(
    prim_path="/World/Cube2",
    name="cube",
    position=(0, 0.5, 6),
    color=np.array([0, 255, 0]),
)
cube3 = DynamicCuboid(
    prim_path="/World/Cube3",
    name="cube",
    position=(0, 1, 7),
    color=np.array([0, 0, 255]),
)

cone1 = DynamicCone(
    prim_path="/World/Cone1",
    name="cone",
    position=(0, 0, 8),
    color=np.array([255, 0, 0]),
)
cone2 = DynamicCone(
    prim_path="/World/Cone2",
    name="cone",
    position=(0, -0.5, 9),
    color=np.array([0, 255, 0]),
)
cone3 = DynamicCone(
    prim_path="/World/Cone3",
    name="cone",
    position=(0, -1, 10),
    color=np.array([0, 0, 255]),
)

cylinder1 = DynamicCylinder(
    prim_path="/World/Cylinder1",
    name="cylinder",
    position=(0, 0, 11),
    color=np.array([255, 0, 0]),
)
cylinder2 = DynamicCylinder(
    prim_path="/World/Cylinder2",
    name="cylinder",
    position=(0.5, 0, 12),
    color=np.array([0, 255, 0]),
)
cylinder3 = DynamicCylinder(
    prim_path="/World/Cylinder3",
    name="cylinder",
    position=(1, 0, 13),
    color=np.array([0, 0, 255]),
)

world.reset()
camera.initialize()
camera.add_distance_to_camera_to_frame()
camera.set_focal_length(0.5)

while True:
    world.step(render=True)
