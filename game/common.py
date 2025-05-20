"""Classes and functions shared between several systems.

Created on 2025.03.20
Contributors:
    Jakub
    Adrien
    Romain
"""

from __future__ import annotations
import logging
import time
from typing import NamedTuple, Callable

logger = logging.getLogger(__name__)


class EnumObject(NamedTuple):
    """Store an object with an associated int.

    Usually used to define how the object is used, such as in events and world objects.
    """
    enum: int
    value: object = None


def auto_integer(func: Callable) -> Callable:
    """Convert output of func to int if appropriate."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, float):
            if result.is_integer():
                return int(result)
        return result
    return wrapper


def named_tuple_modifier(data_type: Callable, old_data: NamedTuple, **changes) -> NamedTuple:
    """Generate a new NamedTuple based on an existing one.

    Changes are represented as another NamedTuple of the same type.
    """
    changes = data_type(**changes)

    new_data = []
    for old, new in zip(old_data, changes):
        if new is None:
            new_data.append(old)
        else:
            new_data.append(new)
    return data_type(*new_data)


def move_toward(a: int | float, b: int | float, step: int | float = 1) -> int | float:
    """Return a moved by step towards b without overshooting."""
    return min(a + step, b) if b >= a else max(a - step, b)


def remap_dict(data: dict, key_map: dict) -> dict:
    """Return a new dict with keys of data remapped through key_map and values unchanged."""
    return {key_map[k]: v for k, v in data.items() if k in key_map}


def try_append(collection: list, item: object) -> None:
    """Append an item to collection if it is not None."""
    if item is not None:
        collection.append(item)


def try_sleep(sleep_time: int) -> None:
    """Sleep for sleep_time if it is not 0."""
    if sleep_time > 0:
        time.sleep(sleep_time)


def _test() -> None:
    """Execute a series of test to see if the program is working"""
    time_test_1 = time.time()
    try_sleep(1)
    time_test_2 = time.time()
    list_test = []
    dict_test = {2 : "un"}
    try_append(list_test, 4)
    assert remap_dict(dict_test, {2 : 1})[1] == "un"
    assert abs(time_test_1 - time_test_2) <= 1.1
    assert list_test[0] == 4
    print("All tests passed")


if __name__ == "__main__":
    _test()
