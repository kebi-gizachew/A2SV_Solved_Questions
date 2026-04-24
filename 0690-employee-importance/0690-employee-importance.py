"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        temp = defaultdict(list)
        for inst in employees:
            temp[inst.id] = inst
        def cycleGraph(id):
            total = temp[id].importance
            for t in temp[id].subordinates:
                total += cycleGraph(t)
            return total
        return cycleGraph(id)





        # impor = 0
        # def graphCycle(id , value, nums):
        #     nonlocal impor
        #     impor += value.importance
        #     for t in nums.subordinates:
        #         graphCycle(t , employees[t - 1].importance , employees[t - 1].subordinates)
        # for x in employees:
        #     if x.id == id:
        #         graphCycle(x , x.importance, x.subordinates)
        # return impor



        