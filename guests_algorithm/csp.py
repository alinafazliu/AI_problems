from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


# Base class for all constraints
class Constraint(Generic[V, D], ABC):

    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...


class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables  # variables to be constrained
        self.domains: Dict[V, List[D]] = domains  # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def forward_checking(self, assignment: Dict[V, D] = {}, counters: List[int] = [0, 0, 0, 0, 0]) -> Optional[
        Dict[V, D]]:

        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            print("Number of cycles: " + str(counters[4]))
            return assignment

        counters[4] += 1

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        for value in self.domains[first]:
            illegal = False
            for i in range(len(counters)):
                if i == value:
                    if counters[i] + 1 > 5:
                        illegal = True
                else:
                    continue
                if counters[i] > 5:
                    illegal = True
            if illegal:
                continue

            local_assignment = assignment.copy()
            local_assignment[first] = value

            if self.consistent(first, local_assignment):
                counters[value] += 1
                result: Optional[Dict[V, D]] = self.forward_checking(local_assignment, counters)
                counters[value] -= 1

                if result is not None:
                    return result
            else:
                break

        return None
