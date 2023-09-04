# The role of each square/square
"""
Defines an enumeration 'Role' for maze squares.

Enum Members:
    - NONE: Represents an undefined or empty role (0).
    - ENEMY: Represents an enemy entity.
    - ENTRANCE: Marks the entrance to the maze.
    - EXIT: Marks the exit of the maze.
    - EXTERIOR: Denotes areas outside the maze.
    - REWARD: Represents a collectible reward.
    - WALL: Marks maze walls and obstacles.

Usage Example:
    Use these roles to identify and categorize maze squares.

    Example:
    ```
    current_tile = Role.ENTRANCE
    if current_tile == Role.WALL:
        print("This tile is a wall.")
    ```

Notes:
    - Roles are assigned incremental integer values, starting with 'NONE' at 0.
    - Compare roles to identify maze squares.
"""
from enum import IntEnum, auto

class Role(IntEnum):
    NONE = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()