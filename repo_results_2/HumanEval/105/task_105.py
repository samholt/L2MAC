def by_length(arr):
	"""
	Given an array of integers, sort the integers that are between 1 and 9 inclusive,
	reverse the resulting array, and then replace each digit by its corresponding name from
	"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

	For example:
	  arr = [2, 1, 1, 4, 5, 8, 2, 3]   
	        -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
	        -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
	  return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
	
	  If the array is empty, return an empty array:
	  arr = []
	  return []
	
	  If the array has any strange number ignore it:
	  arr = [1, -1 , 55] 
	        -> sort arr -> [-1, 1, 55]
	        -> reverse arr -> [55, 1, -1]
	  return = ['One']
	"""
	# Define a dictionary to map numbers to their corresponding names
	num_to_name = {
		1: 'One',
		2: 'Two',
		3: 'Three',
		4: 'Four',
		5: 'Five',
		6: 'Six',
		7: 'Seven',
		8: 'Eight',
		9: 'Nine'
	}
	
	# Filter the array to only include numbers between 1 and 9
	filtered_arr = [num for num in arr if num in num_to_name.keys()]
	
	# Sort the filtered array in ascending order
	filtered_arr.sort()
	
	# Reverse the sorted array
	filtered_arr.reverse()
	
	# Replace each number in the reversed array with its corresponding name
	result = [num_to_name[num] for num in filtered_arr]
	
	return result
