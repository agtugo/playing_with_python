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