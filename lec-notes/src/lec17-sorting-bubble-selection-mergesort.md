---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---



# Sorting

---

### Sorting

* sorting = process of arranging group of items into ascending/descending order based on some criteria
* examples:
    * alphabetize list of names
    * sort list of numbers from highest to lowest
    * sort people by height
    * sort people by age

---

### Sorting

* We've been using built-in sorting methods/functions `.sort()` or `sorted()` 
* How do we actually describe an algorithm used to sort?
* Is there more than one?

---

### Activity

* Need 5 volunteers

---

### Bubble Sort

* Make passes through list
* On each pass, swap out of order elements

---

### Bubble Sort - Complexity

* How many passes through list are made?
* How much work does each pass take?
* Can we stop early if not all passes needed?

---

### Selection Sort

* Goes through list positions one by one
* Selects value that should go there
* More formally:
    * go through list to find smallest value
    * swap that value with value in first spot
    * scan rest of list to find next smallest value
    * swap that value with value in second spot
    * continue with remaining spots for each position in the list

---

### Selection Sort - Complexity

* Think about the work it does:
    * How many times does it go through the list?
    * For each pass, how many elements does it look at?

---


### Merge Sort

* divide and conquer algorithm
* recursive
* process:
    * divide array into 2 halves
    * **recursively** sort each half (by calling mergesort on each half)
    * merge sorted halves (take 2 sorted lists and combine into one sorted list)

---


### Merge Sort - Complexity

* Tree like, recursive halving/combining
* How much work at each step of tree?
* How many levels to the tree?


