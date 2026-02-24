class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        real =skill[-1] + skill[0]
        l , r= 0, len(skill)-1
        op =0
        while r>l:
            if skill[r] + skill[l] != real:
                return -1
            op += skill[r] * skill[l]
            l += 1
            r -= 1
        return op
        