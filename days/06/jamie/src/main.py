from __future__ import annotations
from typing import List, Tuple, Iterator
import sys
import itertools
import functools
from enum import IntEnum


class Direction(IntEnum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

    def turn_right(self) -> Direction:
        return Direction((int(self) + 1) % 4)


class Guard:
    def __init__(self, location: Tuple[int, int], direction: Direction):
        self.location = location
        self.direction = direction

    def turn_right(self):
        self.direction = self.direction.turn_right()

    def step_forward(self):
        self.location = self.next_location()

    def next_location(self) -> Tuple[int, int]:
        y_delta = 0
        if self.direction == Direction.Up:
            y_delta = -1
        elif self.direction == Direction.Down:
            y_delta = 1

        x_delta = 0
        if self.direction == Direction.Right:
            x_delta = 1
        elif self.direction == Direction.Left:
            x_delta = -1

        return (self.location[0] + x_delta, self.location[1] + y_delta)

    def get_sprite(self) -> str:
        match self.direction:
            case Direction.Left:
                return "<"
            case Direction.Right:
                return ">"
            case Direction.Up:
                return "^"
            case Direction.Down:
                return "v"
            case _:
                raise ValueError


class Map:
    def __init__(self):
        self.obstructions = set()
        self.guard = None
        self.size = None

    @staticmethod
    def build_from_line_iter(source: Iterator[str]) -> Map:
        map = Map()
        y_max = 0
        x_max = 0
        for y, line in enumerate(source):
            y_max = y
            for x, char in enumerate(line):
                x_max = max(x_max, x)
                if char == ".":
                    continue
                elif char == "#":
                    map.add_obstruction((x, y))
                elif char == "^":
                    guard = Guard((x, y), direction=Direction.Up)
                    map.set_guard(guard)

        map.set_size((x_max, y_max + 1))
        return map

    def set_guard(self, guard: Guard):
        self.guard = guard

    def set_size(self, size: Tuple[int, int]):
        self.size = size

    def add_obstruction(self, obstruction: Tuple[int, int]):
        self.obstructions.add(obstruction)

    def step(self) -> Tuple[int, int]:
        assert self.guard is not None
        assert self.size is not None

        current_loc = self.guard.location
        # determine if next step would have an obstruction
        if self.guard.next_location() in self.obstructions:
            self.guard.turn_right()
        else:
            self.guard.step_forward()
        return current_loc

    def print(self):
        x_max, y_max = self.size
        for y in range(y_max):
            for x in range(x_max):
                if (x, y) in self.obstructions:
                    print("#", end="")
                elif (x, y) == self.guard.location:
                    print(self.guard.get_sprite(), end="")
                else:
                    print(".", end="")
            print("")

    def guard_on_map(self) -> bool:
        assert self.guard is not None
        assert self.size is not None
        return (
            self.guard.location[0] >= 0
            and self.guard.location[0] < self.size[0]
            and self.guard.location[1] >= 0
            and self.guard.location[1] < self.size[1]
        )


def main():
    map = Map.build_from_line_iter(sys.stdin)
    # map.print()
    locations = set()
    # locations.add(map.guard.location)
    while map.guard_on_map():
        locations.add(map.guard.location)
        map.step()

    print(f"locations: {len(locations)}")


if __name__ == "__main__":
    main()
