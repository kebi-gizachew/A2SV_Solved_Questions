class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        i,j=0,len(people)-1
        k=0
        people.sort()
        while j>=i:
            if people[j]+people[i]<=limit:
                i+=1
            j-=1
            k+=1
        return k