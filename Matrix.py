from dataclasses import dataclass
from typing import List, Dict


@dataclass
class SubMatrices:
    m : List[List[int]]
    k : int

    def __post_init__(self):
        self.p = len(self.m[0]) 
        self.q = len(self.m)
        self.all_subs = []

    def get_size(self):
        return self.p,self.q
    
    def get_sub(self, origin):
        x = origin[0]
        y = origin[1]
        k = self.k
        m = self.m
        subm = []
        for row in m[y:y+k]:
            subm.append(row[x:x+k])
        return subm
    
    def get_sum(self, origin):
        x = origin[0]
        y = origin[1]
        k = self.k
        m = self.m
        _sum = 0
        for row in m[y:y+k]:
            _sum += sum(row[x:x+k])
        return _sum

    @staticmethod
    def sum_matrix(m):
        sum = 0
        for row in m:
            for ele in row:
                sum += ele
        return sum
    
    def update_all_subs(self):
        self.all_subs = []
        k = self.k
        p = self.p
        q = self.q
        for i in range(p-k+1):
            for j in range(q-k+1):
                position = (i,j)
                self.all_subs.append(self.get_sub(position))
        return self.all_subs
    
    def get_all_subs(self):
        return self.all_subs
    
    def number_subs(self):
        return len(self.all_subs)


def is_inside(container, idx):
    if(idx < 0 or idx >= len(container)):
        return False
    return True

route  = 'ABC'
route_hash : Dict[str,int] = {char:number for (number, char) in enumerate(route)}
travels = ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']

def is_left(station_letter) -> bool:
    return not (route_hash[station_letter] == 0)

if __name__ == '__main__':
    pass
