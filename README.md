# Quick Sort — Algorithm Practice Problems

A collection of 8 Python programming problems based on **Quick Sort and partitioning techniques**, designed to strengthen problem-solving skills, coding interview preparation, and Advanced Algorithm Design concepts.

## 📌 Overview

Quick Sort is a Divide and Conquer sorting algorithm that selects a pivot, partitions the array, and recursively sorts the resulting subarrays.

This repository contains implementations of standard Quick Sort and related techniques, including Quickselect, three-way partitioning, and randomized pivot selection.

## 🎯 Objectives

- Understand the Divide and Conquer approach.
- Implement Quick Sort using Python.
- Understand pivot selection and partitioning.
- Solve array-sorting and selection problems.
- Analyse best, average, and worst-case complexities.
- Practise algorithm variations for coding interviews and examinations.

## 📚 Problems Covered

| No. | Problem | Concept | Difficulty |
|---|---|---|---|
| 1 | Sort an Array Using Quick Sort | Basic Quick Sort | Easy |
| 2 | Find the Pivot's Final Position | Partitioning | Easy |
| 3 | Sort an Array Containing Duplicates | Duplicate handling | Easy |
| 4 | Find the Kth Smallest Element | Quickselect | Medium |
| 5 | Sort a Selected Portion of an Array | Subarray sorting | Medium |
| 6 | Sort in Descending Order | Modified partitioning | Medium |
| 7 | Three-Way Quick Sort | Duplicate optimization | Hard |
| 8 | Randomized Quick Sort | Random pivot selection | Hard |

## 🛠️ Technologies Used

- **Language:** Python 3
- **Platform:** GitHub Codespaces / VS Code
- **Concepts:** Divide and Conquer, Recursion, Partitioning, Quickselect, Randomization

## ⚙️ How to Run

1. Clone or open this repository in GitHub Codespaces.
2. Create a Python file for the problem you want to execute.
3. Copy the corresponding solution into the file.
4. Open the terminal and run:

```bash
python3 filename.py
```

Replace `filename.py` with the name of your Python file.

No external libraries are required for Questions 1–7. Question 8 uses Python's built-in `random` module.

## 🧠 Algorithm: Quick Sort

### Pseudocode

```text
QUICKSORT(A, low, high)
    if low < high
        p = PARTITION(A, low, high)
        QUICKSORT(A, low, p - 1)
        QUICKSORT(A, p + 1, high)
```

### Partitioning Strategy

This implementation uses the last element as the pivot.

1. Select the pivot.
2. Move elements less than or equal to the pivot to the left.
3. Place the pivot in its correct sorted position.
4. Recursively sort the left and right subarrays.

## 📊 Time and Space Complexity

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n²) |

**Auxiliary space:**
- Average case: O(log n) for the recursion stack.
- Worst case: O(n) for the recursion stack.

Quick Sort generally sorts in place, but it is not stable in these implementations.

## 🔍 Key Learnings

- Choosing an effective pivot can improve performance.
- Poorly balanced partitions can result in quadratic time complexity.
- Quickselect finds the kth smallest element without fully sorting the array.
- Three-way partitioning is useful when arrays contain many duplicate values.
- Randomized pivot selection reduces the likelihood of consistently poor partitions.

## 🚀 Learning Outcomes

After completing these problems, you should be able to:

- Implement Quick Sort from scratch.
- Trace partitioning operations step by step.
- Modify sorting logic for different requirements.
- Apply Quickselect to selection problems.
- Explain algorithm correctness and complexity.
- Recognize when related partitioning techniques are appropriate.

## 📖 References

- [LeetCode — Sort an Array](https://leetcode.com/problems/sort-an-array/)
- [LeetCode — Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [LeetCode — Sort Colors](https://leetcode.com/problems/sort-colors/)

## 👩‍💻 Author

Created as part of my **Advanced Algorithm Design and coding practice** to strengthen algorithm implementation, problem-solving, and complexity analysis skills.

---

⭐ If you find this repository useful, consider giving it a star!
