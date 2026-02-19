from typing import NamedTuple

from BaseClasses import Item, ItemClassification


class AbioticItem(Item):
    game: str = "Abiotic Factor"


class AbioticItemData(NamedTuple):
    code: int | None = None
    classification: ItemClassification = ItemClassification.progression
    location_key_id: int = 0


items: dict[str, AbioticItemData] = {
    # Junk - 0x0000
    "Random Resource": AbioticItemData(0x0001, ItemClassification.filler),
    # Recipe Unlocks - 0x0100
    "Progressive Keypad Hacker": AbioticItemData(0x0101),
    # Simple Door Unlocks - 0x0200
    "Door Key: Cafeteria Break Room": AbioticItemData(
        0x0201, ItemClassification.useful
    ),
    "Door Key: Door To Level 3 Stairs": AbioticItemData(
        0x0202, ItemClassification.useful
    ),
    "Door Key: Office Sector Level 2 Door Next to Blast Door": AbioticItemData(
        0x0203, ItemClassification.useful
    ),
    # Button Door Unlocks - 0x0300
    "Door Key: Cafeteria Shutters": AbioticItemData(0x0301, ItemClassification.useful),
    "Door Key: Office Sector Plaza Blast Door 1": AbioticItemData(
        0x0302, ItemClassification.filler
    ),
    "Door Key: Office Sector Plaza Blast Door 2": AbioticItemData(
        0x0303, ItemClassification.filler
    ),
    "The Golden Leyak": AbioticItemData(0xFF),
}
