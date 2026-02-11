class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)
        for i in hand: 
            if count[i] == 0:
                continue 
            k = 1
            while k < groupSize:
                if i + k not in count or count[i + k] == 0:
                    return False
                count[i + k] -= 1
                k += 1
            count[i] -= 1
        return True
        