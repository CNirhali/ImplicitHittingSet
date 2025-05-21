import numpy as np
from typing import List, Set, Tuple
from .base import BaseIHS

class GF2IHS(BaseIHS):
    def __init__(self):
        super().__init__()
        self.matrix = None
        self.element_to_index = {}
        self.index_to_element = {}
        
    def add_conflict(self, conflict: Set[int]):
        """Add a conflict set and update the GF(2) matrix representation."""
        super().add_conflict(conflict)
        self._update_matrix()
        
    def _update_matrix(self):
        """Update the GF(2) matrix representation of conflicts."""
        # Create mapping between elements and matrix indices
        all_elements = set().union(*self.conflicts)
        self.element_to_index = {elem: idx for idx, elem in enumerate(sorted(all_elements))}
        self.index_to_element = {idx: elem for elem, idx in self.element_to_index.items()}
        
        # Create the incidence matrix
        n_elements = len(all_elements)
        n_conflicts = len(self.conflicts)
        self.matrix = np.zeros((n_conflicts, n_elements), dtype=np.int8)
        
        for i, conflict in enumerate(self.conflicts):
            for element in conflict:
                self.matrix[i, self.element_to_index[element]] = 1
                
    def find_minimal_hitting_set(self) -> Set[int]:
        """Find a minimal hitting set using GF(2) linear algebra."""
        if not self.conflicts:
            return set()
            
        if self.matrix is None:
            self._update_matrix()
            
        n_conflicts, n_elements = self.matrix.shape
        
        # Use Gaussian elimination to find a minimal solution
        matrix = self.matrix.copy()
        solution = set()
        
        # Perform row operations to find a minimal hitting set
        for i in range(n_conflicts):
            # Find the first non-zero element in this row
            for j in range(n_elements):
                if matrix[i, j] == 1:
                    solution.add(self.index_to_element[j])
                    # Eliminate this element from other rows
                    for k in range(i + 1, n_conflicts):
                        if matrix[k, j] == 1:
                            matrix[k] = (matrix[k] + matrix[i]) % 2
                    break
                    
        self.solution = solution
        return solution 