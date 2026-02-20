class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for q in image:
            r, l = len(image[0])- 1 , 0
            while r >= l:
                if l == r:
                    q[l] = q[l] ^ 1
                else:
                    q[l] , q[r] = q[r]^1 , q[l]^1
                r -= 1
                l += 1
        return image

        # for r in image:
        #     r = r.reverse()
        # for i in range(len(image)):
        #     for j in range(len(image[0])):
        #         if image[i][j] == 0:
        #             image[i][j] = 1
        #         else:
        #             image[i][j] = 0
        # return image
        