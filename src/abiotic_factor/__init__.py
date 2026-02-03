"""Abiotic Factor AP world"""

from worlds.generic.Rules import set_rule
from worlds.AutoWorld import World, WebWorld
from BaseClasses import ItemClassification, Item
from .regions import regions, AbioticRegion
from .items import items, AbioticItem
from .locations import locations, AbioticLocation


class AbioticFactorWebWorld(WebWorld):
    """Web information for Abiotic Factor AP"""


class AbioticFactorWorld(World):
    """Abiotic Factor AP World"""

    game = "Abiotic Factor"
    web = AbioticFactorWebWorld()
    item_name_to_id = {name: data.code for name, data in items.items()}
    location_name_to_id = locations
    origin_region_name = "Office Sector Plaza"

    def create_item(self, name: str) -> AbioticItem:
        data = items[name]
        return AbioticItem(name, data.classification, data.code, self.player)

    def create_event(self, event: str) -> AbioticItem:
        """Helper method to create an event"""
        return AbioticItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        self.multiworld.itempool.append(self.create_item("Progressive Keypad Hacker"))
        (
            self.multiworld.get_location(
                "Manufacturing West - Power Cell Placed", self.player
            ).place_locked_item(self.create_item("The Golden Leyak"))
        )

        items_placed = [
            i
            for i in self.multiworld.itempool
            if i.game == "Abiotic Factor" and i.player == self.player
        ]

        # Fill all remaining locations with junk
        for _ in range(len(locations) - len(items_placed)):
            self.multiworld.itempool.append(
                self.create_item(self.get_filler_item_name())
            )

    def get_filler_item_name(self) -> str:
        return "Random Resource"

    def create_regions(self) -> None:
        main_region = AbioticRegion(
            self.origin_region_name, self.player, self.multiworld
        )
        main_region.add_locations(locations, AbioticLocation)
        self.multiworld.regions.append(main_region)

    def set_rules(self) -> None:
        set_rule(
            self.multiworld.get_location(
                "Manufacturing West - Power Cell Placed", self.player
            ),
            lambda state: state.has("Progressive Keypad Hacker", self.player),
        )
        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            "The Golden Leyak", self.player
        )
