class Solution:
    def smallestNumber(self, pattern: str) -> str:
        path = [i for i in range(1, len(pattern) + 2)]
        def trial(path , pInd):
            if not path:
                return path
            for i in range(len(path) -2 , -1 , -1):
                if pattern[pInd] == "D" and path[i] < path[i + 1]:
                    path[i] , path[i +1] = path[i + 1] , path[i]
                    path[i:] = trial(path[i:] , len(pattern) - 1)
                elif pattern[pInd] == "I" and path[i] > path[i + 1]:
                    path[i] , path[i + 1] = path[i + 1], path[i]
                    path[i:] = trial(path[i:] , len(pattern) - 1)
                pInd -= 1
            return path
        trial(path , len(pattern) - 1)
        return "".join([str(i) for i in path])











        #     if i >= len(pattern):
        #         return
        #     if j >= 9:
        #         return
        #     if pattern[i] == "I":
        #         path.append(j +1)
        #         trial(num , i +1 , j + 1)
        #     else:
        #         temp = path.pop()
        #         path.append(j +1)
        #         path.append(temp)
        #         trial(num , i +1 , temp)
        # trial(pattern , 0 , 1)
        # return "".join([str(i) for i in path])

            


        