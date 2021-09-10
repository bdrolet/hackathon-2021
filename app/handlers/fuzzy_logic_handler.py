import math
from typing import Any
from typing import Dict
from typing import List

# TODO: add "size" field to tasks input
def calculate_fuzzy_estimate(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    # TODO: import from historical data - currently set to default values
    avgs = {"small": 1, "medium": 2, "large": 3, "xl": 4}

    num_by_size = {"small": 0, "medium": 0, "large": 0, "xl": 0}
    response = {}
    for task in tasks:
        num_by_size[task["size"]] += 1

    total = 0
    for size in ["small", "medium", "large", "xl"]:
        total += num_by_size[size] * avgs[size]

    response["estimate"] = round(total)
    # TODO: Adjust confidence by using historical data.
    response["confidence"] = 0.8

    # NOTE: response only has estimate and confidence - no features
    return response
