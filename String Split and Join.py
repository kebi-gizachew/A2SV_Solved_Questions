

def split_and_join(line):
    # write your code here
    l=line.split(" ")
    t="-".join(l)
    return t

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
