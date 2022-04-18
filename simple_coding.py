from importlib.abc import Finder
from operator import le

from pip import List


def find_recuring_letters(str):
    letters_frequency = set()
    for letter in str:
        if letter not in letters_frequency:
            letters_frequency.add(letter)
        else:
            return letter
    
#print(find_recuring_letters("anna"))

def removeDuplicates (nums):
    n = len(nums)
    for i in range(n):
        j = i 
        while j < len(nums)-1 and  nums[j+1] == nums[i]:
            nums.remove(nums[j+1])
            nums.append(_)
            n-=1
            j+=1
            
                


removeDuplicates([1,2,2])