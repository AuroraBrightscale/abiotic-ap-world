"""Abiotic Factor AP world"""

# TODO This import should be "from worlds.AutoWorld..."
from worlds.AutoWorld import World, WebWorld
from BaseClasses import ItemClassification
from .regions import regions, AbioticRegion
from .items import items, AbioticItem
from .locations import locations, AbioticLocation


class AbioticFactorWebWorld(WebWorld):
    """Web information for Abiotic Factor AP"""
    pass


class AbioticFactorWorld(World):
    """Abiotic Factor AP World"""
    game = "Abiotic Factor"
    web = AbioticFactorWebWorld()
    item_name_to_id = {}
    location_name_to_id = {}
    origin_region_name = "Office Sector Plaza"

    def create_item(self, name: str) -> AbioticItem:
        data = items[name]
        return AbioticItem(name, data.classification, data.code, self.player)

    def create_event(self, event: str) -> AbioticItem:
        """Helper class to create an event"""
        return AbioticItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        self.multiworld.itempool.append(self.create_item("The Golden Leyak"))
        # TODO - Just fill everything with junk
        for _ in range(2):
            self.multiworld.itempool.append(
                self.create_item(self.get_filler_item_name()))
        # self.multiworld.itempool += [self.create_item(name)
        #                              for name, _ in items]

    def get_filler_item_name(self) -> str:
        return "Random Resource"

    def create_regions(self) -> None:
        main_region = AbioticRegion(
            self.origin_region_name, self.player, self.multiworld)
        main_region.add_locations(locations, AbioticLocation)
        self.multiworld.regions.append(main_region)

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            "The Golden Leyak", self.player)
