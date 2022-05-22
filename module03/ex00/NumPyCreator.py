import numpy as np

class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)

npc = NumPyCreator()
print(npc.from_list([[1,2,3],[6,3,4]]))
