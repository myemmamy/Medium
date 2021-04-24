# In an array,arr , the elements at indices i and j (where i<j ) form an inversion if arr[i] > arr[j] . In other words,
# inverted elements arr[j] and arr[j] are considered to be "out of order".
# To correct an inversion, we can swap adjacent elements.
#
# Example arr=[2,4,1]
# To sort the array, we must perform the following two swaps to correct the inversions:
# swap(arr[1],arr[2]) and swap(arr[0],arr[1])
# The sort has two inversions: (4,1) and (2,1).
# Given an array arr, return the number of inversions to sort the array.
# Function Description
#
# Complete the function countInversions in the editor below.
#
# countInversions has the following parameter(s):
#
# int arr[n]: an array of integers to sort
# Returns
#
# int: the number of inversions
# Input Format
#
# The first line contains an integer,d , the number of datasets.
#
# Each of the next d pairs of lines is as follows:
#
# The first line contains an integer, n, the number of elements in arr .
# The second line contains n space-separated integers, arr[i].

#below is use recursion to resolve the problem, but doesn't match harkerrank's time limitation

class Inverse:
    def __init__(self,arr):
        self.arr=arr
        self.steps=0
    def swap(self,i,j):
        if i!= j:
            self.arr[i],self.arr[j]=self.arr[j],self.arr[i]
            return 1
        else:
            return 0
    def sort(self,index):
        for i in range(index):
            if self.arr[i] > self.arr[i+1]:
                self.steps += self.swap(i,i+1)
                self.sort(i)

def countInversions(arr):
    newarr=Inverse(arr)
    newarr.sort(len(arr)-1)
    return newarr.steps


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)
        print(result)
