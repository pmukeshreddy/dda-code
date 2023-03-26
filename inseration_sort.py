# Python 3 program for implement deletion in Heaps

# To heapify a subtree rooted with node i which is
# an index of arr[] and n is the size of heap
def heapify(arr, n, i):

	largest = i #Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2

	#If left child is larger than root
	if (l < n and arr[l] > arr[largest]):
		largest = l

	#If right child is larger than largest so far
	if (r < n and arr[r] > arr[largest]):
		largest = r

	# If largest is not root
	if (largest != i):
		arr[i],arr[largest]=arr[largest],arr[i]

		#Recursively heapify the affected sub-tree
		heapify(arr, n, largest)

#Function to delete the root from Heap
def deleteRoot(arr):
	global n

	# Get the last element
	lastElement = arr[n - 1]

	# Replace root with last element
	arr[0] = lastElement

	# Decrease size of heap by 1
	n = n - 1

	# heapify the root node
	heapify(arr, n, 0)

# A utility function to print array of size n
def printArray(arr, n):

	for i in range(n):
		print(arr[i],end=" ")
	print()

# Driver Code
if __name__ == '__main__':

	# Array representation of Max-Heap
	#	 10
	#	 / \
	# 5 3
	# / \
	# 2 4
	arr = [ 34,5,6,1,2,3,4]

	n = len(arr)

	deleteRoot(arr)

	printArray(arr, n)
	
	# This code is contributed by Rajat Kumar.
