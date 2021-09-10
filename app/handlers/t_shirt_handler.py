from typing import Any
from typing import Dict
from typing import List

# Search by business value and then development cost
NET_BUSINESS_VALUE = {
    "xl":       {"xl": 0,   "large": 4,     "medium": 6,    "small": 7},
    "large":    {"xl": -4,  "large": 0,     "medium": 2,    "small": 3},
    "medium":   {"xl": -6,  "large": -2,    "medium": 0,    "small": 1},
    "small":    {"xl": -7,  "large": -3,    "medium": -1,   "small": 0},
}


def get_net_business_value(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    total_value = 0
    response = {"features": []}
    for task in tasks:
        value = NET_BUSINESS_VALUE[task["business"]][task["development"]]
        total_value += value
        response["features"].append(
            {
                "id": task["id"],
                "task": task["task"],
                "business": task["business"],
                "development": task["development"],
                "value": value
            }
        )
    response["value"] = total_value
    return response
