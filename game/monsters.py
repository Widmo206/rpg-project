"""Lorem ipsum

Created on Tue May 13 21:47:27 2025
@author: widmo
"""

from typing import NamedTuple
from files import load_text_dir
from game_classes import Stats, Character
import test_items as ti

"""
name: str,
sprite_sheet: dict[str, str],
is_player: bool,
base_stats: Stats,
actions: tuple(UUID, Action),
initial_effects: dict
"""

PLAYER_SPRITE_DIR_PATH = r"assets\sprites\characters\player"


class DefaultStats(NamedTuple):
    """A collection of default stats for various character races."""

               #         MHP, MST, MMA, STR, AGI, ACU, ARM, RES
               # default: 20,  20,  20,  10,  10,  10,   2,   2

    human        = Stats( 20,  50,   0,  10,  10,  10,   2,   4)
    goblin       = Stats(  5,  20,   0,   2,  14,   0,   1,   2)
    hobgoblin    = Stats( 10,  25,   0,   6,  11,   1,   2,   2)
    goblin_chief = Stats( 20,  30,   5,  10,   8,   5,   4,   4)


def player() -> Character:
    """Create a character from preset player."""
    char = Character.new(
        name            = "player",
        sprite_sheet    = load_text_dir(PLAYER_SPRITE_DIR_PATH),
        is_player       = True,
        base_stats      = DefaultStats.human,
        actions         = [],
        initial_effects = {}
        )
    char.inventory.add(ti.PotionHealth, 3)
    char.inventory.add(ti.Dagger)
    char.inventory.add(ti.Sword)
    char.inventory.add(ti.StrHelmet)
    char.inventory.add(ti.AgiBoots)
    char = char.equip("mainhand", ti.Sword)
    char = char.equip("offhand", ti.Dagger)
    char = char.equip("head", ti.StrHelmet)
    char = char.equip("feet", ti.AgiBoots)
    return char


def goblin() -> Character:
    """Create a character from preset goblin."""
    char = Character.new(
        name            = "goblin",
        sprite_sheet    = None,
        is_player       = False,
        base_stats      = DefaultStats.goblin,
        actions         = [],
        initial_effects = {}
        )
    char.inventory.add(ti.Dagger)
    char = char.equip("mainhand", ti.Dagger)
    return char


def hobgoblin() -> Character:
    """Create a character from preset hobgoblin."""
    char = Character.new(
        name            = "hobgoblin",
        sprite_sheet    = None,
        is_player       = False,
        base_stats      = DefaultStats.hobgoblin,
        actions         = [],
        initial_effects = {}
        )
    char.inventory.add(ti.Dagger, 2)
    char = char.equip("mainhand", ti.Dagger)
    char = char.equip("offhand", ti.Dagger)
    return char


def goblin_chief() -> Character:
    """Create a character from preset goblin_chief."""
    char = Character.new(
        name            = "goblin_chief",
        sprite_sheet    = None,
        is_player       = False,
        base_stats      = DefaultStats.goblin_chief,
        actions         = [],
        initial_effects = {}
        )
    char.inventory.add(ti.Sword)
    char = char.equip("mainhand", ti.Sword)
    return char


def bandit() -> Character:
    """Create a character from preset bandit."""
    char = Character.new(
        name            = "bandit",
        sprite_sheet    = None,
        is_player       = False,
        base_stats      = DefaultStats.human,
        actions         = [],
        initial_effects = {}
        )
    char.inventory.add(ti.Dagger)
    char = char.equip("mainhand", ti.Dagger)
    return char


def _test() -> None:
    """Execute a series of test to see if the program is working"""
    test_monster_1 = goblin()
    test_monster_2 = hobgoblin()
    assert test_monster_1.name == "goblin" and test_monster_2.base == DefaultStats.hobgoblin
    print("All tests passed")


if __name__ == "__main__":
    _test()
