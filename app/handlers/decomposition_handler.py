import math
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple


def calculate_estimate(tasks: List[Dict[str, Any]], create_jiras: bool = False) -> Tuple[int, float]:
    sum_of_variances = 0
    sum_of_expected_cases = 0
    for task in tasks:
        expected_case = (task["best"] + 3*task["likely"] + 2*task["worst"])/6
        individual_standard_dev = (task["worst"] - task["best"])/3.3
        variance = pow(individual_standard_dev, 2)
        sum_of_variances += variance
        sum_of_expected_cases += expected_case
        # TODO: Add code to create jira ticket here if create_jiras flag is true.
    total_standard_dev = math.sqrt(sum_of_variances)
    expected_total = sum_of_expected_cases + 0.84 * total_standard_dev
    # TODO: Adjust confidence by using historical data.
    return round(expected_total), 0.8
