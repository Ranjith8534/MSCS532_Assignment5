### Assignment 5: Heap Data Structures: Quicksort Algorithm – Implementation, Analysis, and Randomization

**Name:** Ranjith Kumar Bollam  
**Course:** MSCS-532 – Algorithms and Data Structures  
**University:** University of the Cumberlands  
**Date:** March 29, 2026  

---

### Overview

This project focuses on the implementation and analysis of the Quicksort algorithm, including both deterministic and randomized versions. The goal is to understand how Quicksort works, evaluate its performance under different scenarios, and analyze how randomization improves efficiency and stability.

Quicksort is a divide-and-conquer sorting algorithm that partitions an array around a pivot element and recursively sorts the resulting subarrays. It is widely used due to its efficiency and practical performance.

###  Technologies Used

- Python 3
- Heap Data Structure
- Algorithm Analysis Techniques

###  Implemented Components

### 1. Heapsort

- Builds a max-heap from the input array  
- Repeatedly extracts the maximum element  
- Produces a sorted array  

**Time Complexity:**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)


### 2. Priority Queue (Max-Heap)

Supports the following operations:

- Insert task  
- Extract highest priority task  
- Increase priority  
- Decrease priority  

Each task contains:
- ID  
- Priority  
- Arrival time  
- Deadline  

###  Experimental Setup

Algorithms were tested using arrays of sizes:

- 1000  
- 3000  
- 5000  

Data conditions:

- Random arrays  
- Sorted arrays  
- Reverse-sorted arrays  

###  Key Observations

- Heapsort provides **consistent performance** across all input types  
- Quicksort is faster on average but **sensitive to input order**  
- Merge Sort is stable but uses **additional memory**  
- Priority Queue efficiently processes tasks based on priority  


###  How to Run the Code

### Step 1: Clone Repository
git clone https://github.com/Ranjith8534/MSCS532_Assignment4.git

### Step 2: Navigate to Folder
cd MSCS532_Assignment4

### Step 3: Run Program
python test.py

###  Output
The program displays:

- Execution times for Heapsort, Quicksort, and Merge Sort  
- Performance comparison across datasets  
- Priority Queue task scheduling results  


###  Files Included

- `heapsort.py` → Heapsort implementation  
- `priority_queue.py` → Priority Queue implementation  
- `test.py` → Testing and comparison script
- `Ranjith_Assignment4.docx` → Project documentation 
- `README.md` → Project documentation  

###  Conclusion

This project demonstrates that heap-based algorithms provide reliable and predictable performance. Heapsort ensures consistent time complexity, while priority queues enable efficient task scheduling. Understanding these structures is essential for building scalable and efficient systems.
