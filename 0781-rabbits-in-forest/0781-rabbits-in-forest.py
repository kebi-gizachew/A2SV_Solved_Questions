class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        count = 0
        
        for n, m in c.items():
            same = n + 1
            count_group = ceil(m / same)
            count += count_group * same
            
        return count