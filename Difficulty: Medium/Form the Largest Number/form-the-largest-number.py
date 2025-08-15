from functools import cmp_to_key

class Solution:
	def findLargest(self, arr):
	    # code here
	    sys.set_int_max_str_digits(500001)
	    arr = [str(x) for x in arr]
	    arr.sort(key = cmp_to_key(lambda a,b: -1 if a+b > b+a else (1 if a+b < b+a else 0)))
	    return str(int("".join(arr)))
	    