from typing import NamedTuple
from enum import Enum
from BaseClasses import Location


class LevelRef(str, Enum):
    NA = ""
    FACILITY_OFFICE_1 = "Facility_Office1"
    FACILITY_OFFICE_2 = "Facility_Office2"
    FACILITY_OFFICE_4 = "Facility_Office4"


class LocationType(int, Enum):
    OBJECTIVE = 0
    DOOR = 1
    BUTTON_DOOR = 2
    KEYPAD_DOOR = 3
    RESEARCH = 4


class AbioticLocation(Location):
    game: str = "Abiotic Factor"


class AbioticLocationData(NamedTuple):
    id: int
    location_type: LocationType
    level_ref: LevelRef
    actor_ref: str


def build_locations() -> dict[str, int]:
    """Get a dictionary mapping all locations to their IDs"""
    return {name: value.id for name, value in locations_office_plaza.items()}


locations_office_plaza: dict[str, AbioticLocationData] = {
    # Some of these are checks that for now are going to be open automatically at
    # the start of the seed. Maybe change this behavior later?
    #
    # NOTE: The objective refs are the *next* objective that the player will get after
    # completing the location's objective. So when the current objective updates to
    # <ref>, that means that the previous objective was completed and the check
    # should be sent out
    #########
    # Objectives - 0x0000
    #########
    # "Objective Complete - Open the Cafeteria Door": AbioticLocationData(
    #     0x0001, LocationType.OBJECTIVE, LevelRef.NA, "quest_cafeteriadoor"
    # ),
    "Objective Complete - Report to Sector Security Officer": AbioticLocationData(
        0x0002, LocationType.OBJECTIVE, LevelRef.NA, "quest_evacuateoffices"
    ),
    "Objective Complete - Evacuate Sector Via Manufacturing": AbioticLocationData(
        0x0003, LocationType.OBJECTIVE, LevelRef.NA, "quest_opensilo3"
    ),
    "Objective Complete - Open Silo 3 to Retrieve Power Cells": AbioticLocationData(
        0x0004, LocationType.OBJECTIVE, LevelRef.NA, "quest_flathill"
    ),
    #########
    # Recipe Research - 0x0100
    #########
    "Research - Tier 1 Keypad Hacker": AbioticLocationData(
        0x0101, LocationType.RESEARCH, LevelRef.NA, "recipe_keypadhacker"
    ),
    "Research - Energy Brick": AbioticLocationData(
        0x0102, LocationType.RESEARCH, LevelRef.NA, "recipe_brick_power"
    ),
    #########
    # One Way Doors - 0x0200
    #########
    # "Office Sector Cafeteria Middle Door": AbioticLocationData(
    #     0x0201, LocationType.DOOR, LevelRef.FACILITY_OFFICE_1, "TODO"
    # ),
    "Office Sector Cafeteria Door to Break Room": AbioticLocationData(
        0x0202, LocationType.DOOR, LevelRef.FACILITY_OFFICE_1, "SimpleDoor_ParentBP_C_8"
    ),
    "Office Sector Door To Level 3 Stairs": AbioticLocationData(
        0x0203,
        LocationType.DOOR,
        LevelRef.FACILITY_OFFICE_2,
        "SimpleDoor_ParentBP_C_25",
    ),
    "Office Sector Level 2 Door Next to Blast Door": AbioticLocationData(
        0x0204, LocationType.DOOR, LevelRef.FACILITY_OFFICE_4, "SimpleDoor_ParentBP_C_9"
    ),
    #########
    # Doors controlled by buttons - 0x0300
    #########
    # "Office Sector Cafeteria Shutters": AbioticLocationData(
    #     0x0301,
    #     LocationType.BUTTON_DOOR,
    #     LevelRef.FACILITY_OFFICE_1,
    #     "Button_Generic_C_1|SecurityDoor_C_3",
    # ),
    "Office Sector Plaza Blast Door 1": AbioticLocationData(
        0x0302,
        LocationType.BUTTON_DOOR,
        LevelRef.FACILITY_OFFICE_1,
        "BlastDoor_C_2",
    ),
    "Office Sector Plaza Blast Door 2": AbioticLocationData(
        0x0303,
        LocationType.BUTTON_DOOR,
        LevelRef.FACILITY_OFFICE_1,
        "BlastDoor_C_3",
    ),
    #########
    # Doors controlled by keypads - 0x0400
    #########
    "Office Sector Security Office Keypad": AbioticLocationData(
        0x0401,
        LocationType.KEYPAD_DOOR,
        LevelRef.FACILITY_OFFICE_1,
        "Button_Keypad_C_2|SimpleDoor_ParentBP_C_19",
    ),
    "Office Sector Door Near Manufacturing West Entrance": AbioticLocationData(
        0x0402,
        LocationType.KEYPAD_DOOR,
        LevelRef.FACILITY_OFFICE_4,
        "Button_Keypad_C_2|SimpleDoor_ParentBP_C_5",
    ),
    "Office Sector Secure Door to Security Office": AbioticLocationData(
        0x0403,
        LocationType.KEYPAD_DOOR,
        LevelRef.FACILITY_OFFICE_4,
        "Button_Keypad_Tier1_C_0|SecurityDoor_Small_C_0",
    ),
}
