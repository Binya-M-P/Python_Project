class magicsquare:
    def __init__(self,f,c):
        self.f=f
        self.c=c
    def msd(self):
        #n=self.f
        x=f
        o=self.c
        l=(o*o)-1
        ms=[]
        for i in range(o):
            r=[]
            for j in range(o):
                r.append(-1)
            ms.append(r)
        while(x<=f+l):
            if(x==f):
                i=0
                j=int(o/2)
                ms[i][j]=x
                x=x+1
                continue
            if(i==0):
                if(j<o-1):
                    i=o-1
                    j=j+1
                    ms[i][j]=x
                else:
                    i=i+1
                    ms[i][j]=x
            elif(j==o-1):
                i=i-1
                j=0
                ms[i][j]=x

            elif(i!=0):
                if(ms[i-1][j+1]!=-1):
                    i=i+1
                    ms[i][j]=x
                else:
                    i=i-1
                    j=j+1
                    ms[i][j]=x
            x=x+1
        print("\n\nMagic Square : ")
        for i in range(o):
            for j in range(o):
                print('%3d'%(ms[i][j]),end=" ")
            print()


c=int(input(("Enter a odd number : ")))
f=int(input("Enter the starting number : "))
o1=magicsquare(f,c)
if(c%2!=0):
    o1.msd()
else:
    print("invalid choice...")