from abc import abstractmethod
from dataclasses import dataclass
import functools
from functools import partial
from typing import Collection

def print_args(func):
    @functools.wraps(func)
    def foo(*args):
        print(*args)
        func(*args)
    return foo

@dataclass
class Pool:
    container : Collection
    action = lambda *_: None
    value = 0 
    idx = 0
    
    def __post_init__(self):
        next(iter(self))
                
    def __iter__(self):
        for idx,value in enumerate(self.container):
            print("called")
            print(idx, value)
            self.value = value 
            self.idx = idx
            self.action(value)
            yield value

    def reset(self):
        self.__init__(self, self.container)

    @abstractmethod
    def pool_sum(pools):
        res = sum(pool.value for pool in pools)
        return res
#The objective of this class is to create a callable or an object
#there are many algorithms that requires many nested fors, 
#this could be solved with a recursive approach, the recursive 
#approach could be using calling the function inside the function
#or modifying the result while working on the result.
#This is just another approach. The product function from itertools
#can provide some of this functionality but this would be a generalization
#in general terms this would be similar to this.
#def For(container, appendables,action1, action2):
#    for i in container:
#	appendables.append(i)#The last for should contain the information of all fors
#	action1(appendables) #This action1 is supposed to contain an specific function 
#	action2(appendables) #This will contain the next for in case you need to nest
@dataclass
class For:
    container : Collection
    action = lambda *_: None

def __post_init__(self):
    self.idx = None

def _for(self):
    for i in container():
        listl

if __name__ == '__main__':
    print("=== MAIN ===")
    pools = [Pool([1,2,3,4])]*4
    Pool.pool_sum(pools)
