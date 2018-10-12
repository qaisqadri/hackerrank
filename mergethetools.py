# https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    # your code goes here
    l=int(len(string)/k)
    ui=list()
    a=0
    b=a+k
    # print(l)
    while len(ui) < l:
        s=string[a:b]
        t=list(s)
        ss=''
        visited=list()
        for x in t:
            if x not in visited:
                visited.append(x)
                ss=ss+x
        ui.append(ss)



        a=b
        b=b+k
    

    for x in ui:
        print(x)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)