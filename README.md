### Assignment 5: Quicksort Algorithm – Implementation, Analysis, and Randomization

**Name:** Ranjith Kumar Bollam  
**Course:** MSCS-532 – Algorithms and Data Structures  
**University:** University of the Cumberlands  
**Date:** March 29, 2026  

---

### Overview
This project focuses on the implementation and analysis of the Quicksort algorithm, including both deterministic and randomized versions. The goal is to understand how Quicksort works, evaluate its performance under different scenarios, and analyze how randomization improves efficiency and stability.

Quicksort is a divide-and-conquer sorting algorithm that partitions an array around a pivot element and recursively sorts the resulting subarrays.

###  Technologies Used

- Python 3
- Algorithm Analysis Techniques

###  Implemented Components

### 1. Deterministic Quicksort

- Uses a fixed pivot (last element)
- Partitions array into two subarrays
- Recursively sorts each part

**Time Complexity:**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)


### 2. Randomized Quicksort

- Uses a randomly selected pivot
- Reduces probability of worst-case scenario
- Provides consistent performance  

###  Time Complexity:

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²) (rare)

### Experimental Setup

Algorithms were tested using:
- Random arrays
- Sorted arrays
- Reverse-sorted arrays

###  Key Observations

- Deterministic Quicksort performs well on random data but degrades on sorted inputs
- Randomized Quicksort maintains stable performance
- Pivot selection significantly affects efficiency


###  How to Run the Code

python quicksort.py
python randomized_quicksort.py


###  Files Included

- `quicksort.py`  
- `randomized_quicksort.py` 
- `report.docx` → Project documentation 
- `README.md` → Project documentation  

###  Conclusion

Quicksort is a powerful and efficient sorting algorithm. While deterministic Quicksort is simple, randomized Quicksort provides better performance consistency. This makes it more suitable for real-world applications.
