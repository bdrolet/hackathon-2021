import math
from typing import Any
from typing import Dict
from typing import List


def calculate_estimate(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    sum_of_variances = 0
    sum_of_expected_cases = 0
    response = {"features": []}
    for task in tasks:
        expected_case = (task["best"] + 3*task["likely"] + 2*task["worst"])/6
        individual_standard_dev = (task["worst"] - task["best"])/3.3
        variance = pow(individual_standard_dev, 2)
        sum_of_variances += variance
        sum_of_expected_cases += expected_case
        response["features"].append(
            {
                "id": task["id"],
                "task": task["task"],
                "best": task["best"],
                "likely": task["likely"],
                "worst": task["worst"],
                "expected": expected_case
            }
        )
    total_standard_dev = math.sqrt(sum_of_variances)
    response["estimate"] = round(sum_of_expected_cases + 0.84 * total_standard_dev)
    # TODO: Adjust confidence by using historical data.
    response["confidence"] = 0.8
    return response
