import random
from typing import List, Dict

class RandomizedSet:
    dv2i: Dict[int,int] 
    li: List[int]
    def __init__(self):
        self.dv2i = dict()
        self.li = list()
    def insert(self, val: int) -> bool:
        if val in self.dv2i:
            return False
        else:
            self.dv2i[val] = len(self.li)
            self.li.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.dv2i:
            i = self.dv2i[val]       
            lv = self.li[-1]
            self.li[i] = lv        
            self.li.pop()
            self.dv2i[lv] = i
            del self.dv2i[val]                
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(self.li)