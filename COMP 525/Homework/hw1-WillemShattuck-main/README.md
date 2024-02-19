[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FnPBM7AP)
GUIDELINES:
 - You may only use range based loops.  
 - You may not use enumerate
 - You may not use `len()` to get the size of the internal list.  The used
 variable keeps track of this.  

TODO:

- Fix the `str` function so it adds commas between each number.  

- When you run out of used space, double the space in the array,
copy the old elements, one at a time, into the new list and set the internal list to the new list.  Be sure to also increase the `size` variable. 

- Add a method to pop the last element from the list.  This method
will return the last element and decrement `used`.  If there are no elements in the list to pop, return None.

- Add a method to find the index of a value.  This is the same as the `index` method of the list data structure.  Your function only needs to accept one value.  


	`Animals= ["cat", "dog", "tiger"]` 
	
	`print(Animals.index("dog"))` # returns 1

	If a value is not found, return `ValueError` 

- Add a method called `at(index)` that returns the value at that index or `IndexError` if the index is out of bounds.

- Add a method called `insert(index, value)` that inserts a value at an index.
This will move over the values in the list.  Do not use `list insert` behind the scenes; you must move the values over one at a time and keep track of the number of used elements in the list.  If the index is out of  bounds, return `False`.  If the
operation succeeds, return `True`. 

- Add at least one testing function for each one of the above.  
- Add the testing method to the test file and test with pytest. 

- Incremental development: At least 6 commits.  

