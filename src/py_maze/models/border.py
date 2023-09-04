"""
Represents the borders of a maze cell as an enumeration of border types.

Enum Members:
    - EMPTY: No borders present.
    - TOP: The top border of the cell.
    - BOTTOM: The bottom border of the cell.
    - RIGHT: The right border of the cell.
    - LEFT: The left border of the cell.

Properties:
    - corner: Returns True if the border forms a corner (e.g., top-left or bottom-right).
    - dead_end: Returns True if the border creates a dead-end within the cell.
    - intersection: Returns True if the border allows multiple paths within the cell.

Usage Example:
    Use these border types to define and analyze maze cells. You can check for
    corners, dead-ends, or intersections within a cell by accessing the
    respective properties.

    Example:
    ```
    cell_border = Border.TOP | Border.LEFT
    if cell_border.corner:
        print("This cell has a corner.")
    ```

Notes:
    - Borders are represented as bit flags, allowing for easy combination.
    - The `corner`, `dead_end`, and `intersection` properties provide helpful
      analysis tools for maze cell borders.
    -  bit_count(self, /)
          Number of ones in the binary representation of the absolute value of self.
          Also known as the population count.

        bin(13) # '0b1101'
        bin(13).bit_count() # 3
"""

from enum import IntFlag, auto

class Border(IntFlag):
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    RIGHT = auto()
    LEFT = auto()

    @property
    def corner(self) -> bool:
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT,
        )

    @property
    def dead_end(self) -> bool:
        return self.bit_count() == 3

    @property
    def intersection(self) -> bool:
        return self.bit_count() < 2