import time
import random
from typing import List, Set, Tuple
import pandas as pd
import matplotlib.pyplot as plt
from ihs.base import BaseIHS
from ihs.advanced import AdvancedIHS
from ihs.gf2 import GF2IHS

def generate_random_conflicts(n_elements: int, n_conflicts: int, conflict_size: int) -> List[Set[int]]:
    """Generate random conflict sets for testing."""
    conflicts = []
    for _ in range(n_conflicts):
        conflict = set(random.sample(range(n_elements), conflict_size))
        conflicts.append(conflict)
    return conflicts

def benchmark_algorithms(n_elements: int, n_conflicts: int, conflict_size: int, n_trials: int = 5):
    """Benchmark different IHS algorithms."""
    results = []
    
    for trial in range(n_trials):
        conflicts = generate_random_conflicts(n_elements, n_conflicts, conflict_size)
        
        # Test Base IHS
        base_ihs = BaseIHS()
        for conflict in conflicts:
            base_ihs.add_conflict(conflict)
        start_time = time.time()
        base_solution = base_ihs.find_minimal_hitting_set()
        base_time = time.time() - start_time
        
        # Test Advanced IHS
        advanced_ihs = AdvancedIHS()
        for conflict in conflicts:
            advanced_ihs.add_conflict(conflict)
        start_time = time.time()
        advanced_solution = advanced_ihs.find_minimal_hitting_set()
        advanced_time = time.time() - start_time
        
        # Test GF2 IHS
        gf2_ihs = GF2IHS()
        for conflict in conflicts:
            gf2_ihs.add_conflict(conflict)
        start_time = time.time()
        gf2_solution = gf2_ihs.find_minimal_hitting_set()
        gf2_time = time.time() - start_time
        
        results.append({
            'trial': trial,
            'base_time': base_time,
            'advanced_time': advanced_time,
            'gf2_time': gf2_time,
            'base_size': len(base_solution),
            'advanced_size': len(advanced_solution),
            'gf2_size': len(gf2_solution)
        })
    
    return pd.DataFrame(results)

def plot_benchmark_results(results: pd.DataFrame):
    """Plot benchmark results."""
    # Time comparison
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.boxplot([results['base_time'], results['advanced_time'], results['gf2_time']],
                labels=['Base', 'Advanced', 'GF2'])
    plt.title('Execution Time Comparison')
    plt.ylabel('Time (seconds)')
    
    # Solution size comparison
    plt.subplot(1, 2, 2)
    plt.boxplot([results['base_size'], results['advanced_size'], results['gf2_size']],
                labels=['Base', 'Advanced', 'GF2'])
    plt.title('Solution Size Comparison')
    plt.ylabel('Size of Hitting Set')
    
    plt.tight_layout()
    plt.savefig('benchmark_results.png')
    plt.close()

if __name__ == '__main__':
    # Run benchmark with different problem sizes
    sizes = [
        (10, 5, 3),    # Small
        (50, 20, 5),   # Medium
        (100, 40, 8)   # Large
    ]
    
    for n_elements, n_conflicts, conflict_size in sizes:
        print(f"\nBenchmarking with {n_elements} elements, {n_conflicts} conflicts, size {conflict_size}")
        results = benchmark_algorithms(n_elements, n_conflicts, conflict_size)
        print("\nResults:")
        print(results.describe())
        plot_benchmark_results(results) 