from typing import NamedTuple

from BaseClasses import Item, ItemClassification


class AbioticItem(Item):
    game: str = "Abiotic Factor"


class AbioticItemData(NamedTuple):
    code: int | None = None
    classification: ItemClassification = ItemClassification.progression


items: dict[str, AbioticItemData] = {
    "Random Resource": AbioticItemData(0x01, ItemClassification.filler),
    "Progressive Keypad Hacker": AbioticItemData(0xE0),
    "The Golden Leyak": AbioticItemData(0xFF)
}
