import numpy as np
from typing import List, Set, Tuple

class BaseIHS:
    def __init__(self):
        self.conflicts = []
        self.solution = set()
        
    def add_conflict(self, conflict: Set[int]):
        """Add a conflict set to the problem."""
        self.conflicts.append(conflict)
        
    def is_hitting_set(self, candidate: Set[int]) -> bool:
        """Check if a candidate set is a hitting set for all conflicts."""
        return all(not candidate.isdisjoint(conflict) for conflict in self.conflicts)
    
    def find_minimal_hitting_set(self) -> Set[int]:
        """Find a minimal hitting set using the base algorithm."""
        if not self.conflicts:
            return set()
            
        # Start with all elements from all conflicts
        all_elements = set().union(*self.conflicts)
        
        # Try removing elements one by one
        current_set = all_elements.copy()
        for element in sorted(all_elements):
            test_set = current_set - {element}
            if self.is_hitting_set(test_set):
                current_set = test_set
                
        self.solution = current_set
        return current_set
    
    def get_solution(self) -> Set[int]:
        """Return the current solution."""
        return self.solution.copy() 