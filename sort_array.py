def sort_array(arr):
"""This function manually sorts an input array from ascending to descending order."""
  sorted_arr = []
  
  # Start off our list
  sorted_arr.append(arr.pop())
  print(sorted_arr)
  for number in arr:
	  # With input arr, we compare it to each number currently in the list.
    for i in range(len(sorted_arr)):
      if number < sorted_arr[i]:
        if i==0:
			# based on conditions, we add it to the list.
          sorted_arr = [number] + sorted_arr
          break
        else:
          sorted_arr = sorted_arr[0:i]+[number]+sorted_arr[i:]
          break
      elif number >= sorted_arr[i] and i==(len(sorted_arr)-1):
        sorted_arr = sorted_arr + [number]
        break
  return sorted_arr
