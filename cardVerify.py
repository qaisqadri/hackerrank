
# https://www.hackerrank.com/challenges/validating-credit-card-number/problemrint(x)
import re
def verify(cc):
        #print(type(cc))
        #print(cc)
    for card in cc:
        
        flag=False
        if re.match('^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$',card):
            # t=card.split("-")
            # flag = False
            # if len(t)==4 and len(t[0])==4 and len(t[1])==4 and len(t(2)==4) and len(t(3)==4):
            #     flag==True
            # if flag==True:
            l=list(card)
            for x in l:
                if x == '-':
                    l.remove(x)
                # print(l)
            for x in range(len(l)-4):
                #print(l[x],l[x+1],"  ",l[x+1],l[x+2],"  ",l[x+2],l[x+3])

                if l[x]==l[x+1] and l[x+1]==l[x+2] and l[x+2]==l[x+3]:

                    flag=False
                    break
                else:
                    flag=True
        # else:
        #     flag=False
        # print(l)
            
            if flag:
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")



if __name__=='__main__':
        n=int(input())
        cc=list()
        for a in range(n):
                n=input()
                cc.append(n)
        verify(cc)


