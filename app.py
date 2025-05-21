import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Set
import random
from ihs.base import BaseIHS
from ihs.advanced import AdvancedIHS
from ihs.gf2 import GF2IHS

st.set_page_config(page_title="IHS Solver", layout="wide")

st.title("Implicit Hitting Set Solver")
st.write("Compare different algorithms for solving the Implicit Hitting Set problem")

# Sidebar controls
st.sidebar.header("Problem Parameters")
n_elements = st.sidebar.slider("Number of Elements", 5, 50, 20)
n_conflicts = st.sidebar.slider("Number of Conflicts", 3, 20, 8)
conflict_size = st.sidebar.slider("Conflict Size", 2, 10, 3)

# Generate random conflicts
@st.cache_data
def generate_conflicts(n_elements, n_conflicts, conflict_size):
    conflicts = []
    for _ in range(n_conflicts):
        conflict = set(random.sample(range(n_elements), conflict_size))
        conflicts.append(conflict)
    return conflicts

conflicts = generate_conflicts(n_elements, n_conflicts, conflict_size)

# Display conflicts
st.header("Conflict Sets")
conflict_df = pd.DataFrame([
    {"Conflict": i, "Elements": str(sorted(conflict))}
    for i, conflict in enumerate(conflicts)
])
st.dataframe(conflict_df)

# Solve using different algorithms
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Base Algorithm")
    base_ihs = BaseIHS()
    for conflict in conflicts:
        base_ihs.add_conflict(conflict)
    base_solution = base_ihs.find_minimal_hitting_set()
    st.write("Solution:", sorted(base_solution))
    st.write("Size:", len(base_solution))

with col2:
    st.subheader("Advanced Algorithm")
    advanced_ihs = AdvancedIHS()
    for conflict in conflicts:
        advanced_ihs.add_conflict(conflict)
    advanced_solution = advanced_ihs.find_minimal_hitting_set()
    st.write("Solution:", sorted(advanced_solution))
    st.write("Size:", len(advanced_solution))

with col3:
    st.subheader("GF(2) Algorithm")
    gf2_ihs = GF2IHS()
    for conflict in conflicts:
        gf2_ihs.add_conflict(conflict)
    gf2_solution = gf2_ihs.find_minimal_hitting_set()
    st.write("Solution:", sorted(gf2_solution))
    st.write("Size:", len(gf2_solution))

# Visualization
st.header("Solution Comparison")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Solution sizes
sizes = [len(base_solution), len(advanced_solution), len(gf2_solution)]
ax1.bar(['Base', 'Advanced', 'GF(2)'], sizes)
ax1.set_title('Solution Size Comparison')
ax1.set_ylabel('Size of Hitting Set')

# Element coverage
all_elements = set().union(*conflicts)
coverage = [
    len(base_solution) / len(all_elements),
    len(advanced_solution) / len(all_elements),
    len(gf2_solution) / len(all_elements)
]
ax2.bar(['Base', 'Advanced', 'GF(2)'], coverage)
ax2.set_title('Element Coverage')
ax2.set_ylabel('Coverage Ratio')

st.pyplot(fig)

# Manual conflict input
st.header("Manual Conflict Input")
st.write("Enter your own conflicts (comma-separated numbers):")
conflict_input = st.text_input("New Conflict", "1,2,3")
if st.button("Add Conflict"):
    try:
        new_conflict = set(map(int, conflict_input.split(',')))
        if all(x < n_elements for x in new_conflict):
            conflicts.append(new_conflict)
            st.success("Conflict added!")
            st.experimental_rerun()
        else:
            st.error("Elements must be less than the number of elements!")
    except ValueError:
        st.error("Invalid input! Please enter comma-separated numbers.") 