if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i=[]
    o,p,q=0,0,0
    while o<=x:
        p=0
        while p<=y:
            q=0
            while q<=z:
                if o+p+q!=n:
                    i.append([o,p,q])
                q+=1
            p+=1
        o+=1
    print(i)
    
