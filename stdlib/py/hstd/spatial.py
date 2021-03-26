"""
Spatial utility functions.
"""
import math
import random
from dataclasses import dataclass
from typing import Optional, List

from .agent import AgentState, AgentFieldError


@dataclass
class Topology:
    x_bounds: List[float]
    y_bounds: List[float]
    z_bounds: Optional[List[float]]


def manhattan_distance(p1: List[float], p2: List[float]) -> float:
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    dz = abs(p1[2] - p2[2])
    return dx + dy + dz


def euclidean_squared_distance(p1: List[float], p2: List[float]) -> float:
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return dx * dx + dy * dy + dz * dz


def euclidean_distance(p1: List[float], p2: List[float]) -> float:
    return math.sqrt(euclidean_squared_distance(p1, p2))


def chebyshev_distance(p1: List[float], p2: List[float]) -> float:
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    dz = abs(p1[2] - p2[2])
    return max(dx, dy, dz)


def distance_between(a: AgentState, b: AgentState, distance="euclidean") -> Optional[float]:
    if a.position is None:
        raise AgentFieldError(a.agent_id, "position", "cannot be None")
    if b.position is None:
        raise AgentFieldError(b.agent_id, "position", "cannot be None")

    if distance == "euclidean":
        return euclidean_distance(a.position, b.position)
    elif distance == "euclidean_sq":
        return euclidean_squared_distance(a.position, b.position)
    elif distance == "manhattan":
        return manhattan_distance(a.position, b.position)
    elif distance == "chebyshev":
        return chebyshev_distance(a.position, b.position)

    raise ValueError(
        "distance must be one of 'euclidean', 'euclidean_sq', 'manhattan' or 'chebyshev'"
    )


def normalize_vector(vec: List[float]) -> List[float]:
    magnitude = math.sqrt(sum(v * v for v in vec))
    return [v / magnitude for v in vec]


def random_position(topology: Topology, z_plane=False):
    xpos = int(random.uniform(topology.x_bounds[0], topology.x_bounds[1]))
    ypos = int(random.uniform(topology.y_bounds[0], topology.y_bounds[1]))
    zpos = 0
    if z_plane:
        if topology.z_bounds is None:
            raise ValueError("topology z_bounds is required if z_plane is True")
        zpos = int(random.uniform(topology.z_bounds[0], topology.z_bounds[1]))

    return [xpos, ypos, zpos]
