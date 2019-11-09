"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the PowerSet of a number
https://www.geeksforgeeks.org/power-set/
"""

def powerSet(a_set):
	''' powerSet() returns the a list of the power set of a set
	-- param
	a_set : set
	-- return
	list
	'''

	result = [set()]

	for i in a_set:
		result.append({i})

	i = 0
	while i < len(result):
		j = 0
		while j < len(result):
			if result[i] | result[j] not in result:
				result.append(result[i] | result[j])
			j += 1
		i += 1

	return result

a = powerSet({1,2,3,4,5})
a.sort()
print(a)
print(len(a))