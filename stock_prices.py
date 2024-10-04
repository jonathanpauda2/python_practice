from typing import List

class Solution:
    def examples(self,x: List[int]) -> int:
        x = [2200,2350,2600,2130,2190]
        # insert another value at index 1
        x.insert(1,2840)
        #print out the new array
        print(x)

        #get length of the array
        array_length=len(x)
        print("the length of the array is", array_length)
        #on what day were stock proces 2600
        #this function of array.index says search the array and find the first instance of 2600 as the value and return the index
        index_of_2600= x.index(2600)
        print(index_of_2600)

s = Solution()
s.examples([])

