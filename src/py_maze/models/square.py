"""
Represents a square cell within a maze.

This class defines a square cell within a maze grid, characterized by its index,
row, column, border configuration, and optional role. The 'Square' objects are
typically used to construct the maze layout and associate roles with specific cells.

Attributes:
    - index (int): An identifier for the square within the maze.
    - row (int): The row position of the square within the maze grid.
    - column (int): The column position of the square within the maze grid.
    - border (Border): An enumeration representing the borders of the square.
    - role (Role): An optional enumeration representing the role of the square
      (e.g., entrance, exit, wall, etc.). Default is 'Role.NONE' indicating no
      specific role.

Usage Example:
    You can create 'Square' objects to define the layout of a maze, set specific
    roles for certain cells, and access their attributes as needed.

    Example:
    ```
    from py_maze.models.square import Square
    from py_maze.models.border import Border
    from py_maze.models.role import Role

    # Create a square representing an entrance with no walls
    entrance = Square(index=0, row=0, column=0, border=Border.EMPTY, role=Role.ENTRANCE)

    # Access square attributes
    print(entrance.index)  # 0
    print(entrance.row)  # 0
    print(entrance.column)  # 0
    print(entrance.border)  # Border.EMPTY
    print(entrance.role)  # Role.ENTRANCE
    ```

Notes:
    - 'Square' objects are typically used to define maze cells and their roles.
    - The 'frozen=True' parameter ensures that 'Square' objects are immutable.
"""

from dataclasses import dataclass

from py_maze.models.border import Border
from py_maze.models.role import Role

@dataclass(frozen=True)
class Square:
    index: int
    row: int
    column: int
    border: Border
    role: Role = Role.NONE