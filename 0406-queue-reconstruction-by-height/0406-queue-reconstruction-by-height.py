class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        arr = []
        people.sort(key = lambda x: (x[0] , -x[1]))
        for i in range(len(people) - 1 , -1 , -1):
            x , y = people[i]
            arr = arr[:y] + [people[i]] + arr[y:]
        return arr

        