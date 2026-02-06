class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        tempo=defaultdict(list)
        for i in paths:
            sets=i.split()
            mains=sets[0]
            for k in sets[1:]:
                test=k.split("(")
                tempo[test[1]].append(mains+"/"+test[0])
        return [v for v in tempo.values() if len(v)>1]
        