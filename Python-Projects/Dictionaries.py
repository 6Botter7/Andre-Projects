# loadout = {
#     "SMG": {
#         "Mp5": ["High Mobility", "180 damage", "50 range", "Good Hipfire"],
#         "Mp7": ["Very stable", "160 Damage", " 100 range", "Very Accurate"]
#     },
#     "Assault": {
#         "M4A1": ["Stable", "240 damage", "180 range", "Good Mobility"],
#         "Grau": ["High Fire Rate", "200 damage", "230 range", "Very Accurate"]
#     }
# }
from ctypes.wintypes import LPWIN32_FIND_DATAA
from json import load
from typing import ItemsView


loadout = {
    "smg": {
        "1": 20,
        "2": 30,
        "3": 40
    },
    "lmg": {
        "4": 200,
        "5": 300,
        "6": 400
    }
}


current_gun = {
    "loadout-stats": []
}


def pick_up(smg, lmg):
    l1 = print(loadout["lmg"]["4"])
    l2 = print(loadout["smg"]["2"])
    l3 = print("Your going barefisst")


print(loadout["smg"]["1"])
print(loadout["lmg"]["6"])
print(len(loadout))

pick_up("2", "4")
