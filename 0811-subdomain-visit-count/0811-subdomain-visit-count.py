class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        tempo=defaultdict(int)
        for i in cpdomains:
            x=i.split()
            num=int(x[0])
            arr=x[1].split(".")
            for k in range(len(arr)):
                r=".".join(arr[k:])
                if r not in tempo:
                    tempo[r]=num
                else:
                    tempo[r]+=num
        finale=[]
        for j,i in tempo.items():
            t=str(i)+" "+j
            finale.append(t)
        return finale


        


        