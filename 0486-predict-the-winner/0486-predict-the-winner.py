class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        Bool = False
        def trial(arr):
            if len(arr) == 0:
                return 0
            l1 = arr[-1] - trial(arr[:len(arr) -1])
            l2 = arr[0] - trial(arr[1:])
            return max(l1 , l2)
        l1, l2 =0 , 0
        return trial(nums) >= 0
            



        

        