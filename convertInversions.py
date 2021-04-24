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

####
#method 1 recursoin
####
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
        
####
#method 2, no recursion, 2 loops
#each time a swap may cause additional swap to prior items since the prior items are already sorted, but the new swap may bring a new smaller item
#for the internal loop, doesn't need to swap, just need to check how many items bigger than the current arr[i] is fine, 
#since the items before i are already checked and counted for swap steps
#but still exceed time limitation
####
def countInversions(arr):
    def swap(arr,i,j):
        if i != j:
            arr[i],arr[j]=arr[j],arr[i]
            return 1
        else:
            return 0
    steps=0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            steps += swap(arr,i,i+1)
            for j in range(i-1,-1,-1):
                if arr[j] > arr[i]:
                    steps += 1
    return steps

####
#method 3, above is O(n^2)
#try to make as O(nlogn), then use bisect, but still 4 cases time exceeded
####
import bisect
def countInversions(arr):
    def swap(arr,i,j):
        if i != j:
            arr[i],arr[j]=arr[j],arr[i]
            return 1
        else:
            return 0
    steps=0
    newarr=[]
    for i in range(len(arr)-1):

        if arr[i] > arr[i+1]:
            steps += swap(arr,i,i+1)
            if i > 0:
                index = bisect.bisect(newarr,arr[i])
                steps += i-index
        bisect.insort(newarr, arr[i])
    return steps
