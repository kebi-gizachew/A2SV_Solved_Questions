class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        temp=[]
        flag=False
        t=""
        for i in source:
            k=0
            while k<len(i):
                if not flag and k+1<len(i) and i[k:k+2]=="/*":
                    flag=True
                    k+=2
                elif flag and k+1<len(i) and i[k:k+2]=="*/":
                    flag=False
                    k+=2
                elif not flag and k+1<len(i) and i[k:k+2]=="//":
                    break
                elif flag:
                    k+=1
                else:
                    t+=i[k]
                    k+=1
            if t and not flag:
                temp.append(t)
                t=""
        return temp

                



        