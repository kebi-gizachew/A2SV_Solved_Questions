def swap_case(s):
    arr=[]
    for i in s:
        if 97<=ord(i)<=122:
            t=ord(i)-97
            char=chr(65+t)
            arr.append(char)
        elif 65<=ord(i)<=90:
            t=ord(i)-65
            char=chr(97+t)
            arr.append(char)
        else:
            arr.append(i)
    return "".join(arr)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
