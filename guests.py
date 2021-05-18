from csp import Constraint, CSP
from typing import Dict, List
import time


def sort_tables(files):
    names = set(files.values())

# use a list comprehension, iterating through keys and checking the values match each n
    d = {}
    for n in names:
        d[n] = [k for k in files.keys() if files[k] == n]
    return d 

class DifferentTableConstraint(Constraint[str, str]):
    def __init__(self, M1: str, M2: str) -> None:
        super().__init__([M1, M2])
        self.M1: str = M1
        self.M2: str = M2

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if self.M1 not in assignment or self.M2 not in assignment:
            return True

        return assignment[self.M1] != assignment[self.M2]


class SameTableConstraint(Constraint[str, str]):
    def __init__(self, M1: str, M2: str) -> None:
        super().__init__([M1, M2])
        self.M1: str = M1
        self.M2: str = M2

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if self.M1 not in assignment or self.M2 not in assignment:
            return True

        return assignment[self.M1] == assignment[self.M2]


if __name__ == "__main__":
    variables: List[str] = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14",
                            "M15",
                            "M16", "M17", "M18", "M19", "M20"]
    domains: Dict[str, List[int]] = {}
    for variable in variables:
        domains[variable] = [0, 1, 2, 3]
    # print(domains)
    csp: CSP[str, int] = CSP(variables, domains)
    csp.add_constraint(DifferentTableConstraint("M3", "M18"))
    csp.add_constraint(DifferentTableConstraint("M7", "M8"))
    csp.add_constraint(DifferentTableConstraint("M10", "M11"))
    csp.add_constraint(SameTableConstraint("M5", "M9"))
    csp.add_constraint(SameTableConstraint("M6", "M13"))

    startingTime = time.time()

    solution = csp.forward_checking()
    if solution is None:
        print("No solution found!")
    else:
        sorted_tables = sort_tables(solution)
        for row in sorted_tables:
            print(f"Table {row+1}: {sorted_tables[row]}")

    print("Time to complete in seconds: " + str((time.time() - startingTime)))
