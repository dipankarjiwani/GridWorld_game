#Name:Dipankar JIwani
#Roll no:2019037
#Sec,group:A,1
import os
import random
import time
clear = lambda: os.system('cls')
def ispresent(a1,l):
    for i in range(len(l)):
        if a1.returnxy()==l[i].returnxy():
            return True
        else:
            pass
    return False
def checkstatus(x,y,grid):
    a=[]
    for i in range(1,10):
        a.append(i)
    if grid[x][y]=='G':
        return 12
    elif grid[x][y]=='#':
        return 11
    elif grid[x][y]=='.':
        return 0
    elif grid[x][y]=='S':
        return 0
    else:
        return int(grid[x][y])
def update(a,n,b):
    if b==0:
        pass
    elif b==11:
        a=a-(4*n)
    elif b==12:
        pass
    elif b in range(1,10):
        a=a+(b*n)
    else:
        pass
    return a
def find(a,l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j]==a:
                return (i,j)
            else:
                pass
    return (-1,-1)
def gameover():
    print("Game Over , You Lose , You're low on energy")
    b=input()
    exit()
    
        
class grid():
    def __init__(self,n):
        self.n=n
        a=[(0,0),(0,n-1),(n-1,0),(n-1,n-1)]#corners
        self.start=random.choice(a)
        a.remove(self.start)#to get reamining corners
        self.goal=random.choice(a)
        d=[]
        a1=[]#to get range for scores
        for i in range(n):
            a1.append(i+1)
            for j in range(n):
                d.append((i,j))
        if self.start in d:
            d.remove(self.start)
        if self.goal in d:
            d.remove(self.goal)#d now has available co-ordinates for obstacles,rewards
        b=n//2
        self.myobstacles=[]
        self.myrewards=[]
        for i in range(b):
            (x,y)=random.choice(d)
            self.myobstacles.append(obstacle(x,y))
            d.remove((x,y))
        for i in range(b):
            (x,y)=random.choice(d)
            self.myrewards.append(reward(x,y))
            d.remove((x,y))
        self.thisgrid=[]
        for i in range(n):
            self.thisgrid.append([i])
            for j in range(n-1):
                self.thisgrid[i].append('.')
                
        for i in range(n):
            for j in range(n):
                if ispresent(obstacle(i,j),self.myobstacles):
                    self.thisgrid[i][j]='#'
                elif ispresent(reward(i,j),self.myrewards):
                    a=random.randrange(1,10)
                    self.thisgrid[i][j]=a
                elif (i,j)==self.start:
                    self.thisgrid[i][j]='S'
                elif (i,j)==self.goal:
                    self.thisgrid[i][j]='G'
                else:
                    self.thisgrid[i][j]='.'
        self.showGrid(2*self.n)
    def showGrid(self,energy):
        clear()
        print('                                    ','PLAYER ENERGY=',energy)
        for i in range(self.n):
            for j in range(self.n):
                print(self.thisgrid[i][j],end='  ')
            print('\n')
        time.sleep(1)
        
    def rotateclockwise(self):
        a=[]
        b=[]
        e=self.goal
        for i in range(self.n):
            a.append(self.thisgrid[i])
        for i in range(self.n):
            b.append(a[-(i+1)])
        c=[]
        for i in range(self.n):
            c.append([])
            for j in range(self.n):
                c[i].append('')
        for i in range(self.n):
            for j in range(self.n):
                c[j][i]=b[i][j]
        d=obstacle(self.x,self.y)
        if c[self.x][self.y]=='#':
            print("GRID CANNOT BE ROTATED")
        else:
            f=find('G',c)# finding co-ordinates of g in new grid,swapping values of G with its new position,to keep G where it was
            t1=c[e[0]][e[1]]
            c[f[0]][f[1]]=t1
            c[e[0]][e[1]]='G'
            f=find('O',c)
            if f==(-1,-1):
                f=find('S',c)
            t1=c[self.x][self.y]
            c[f[0]][f[1]]=t1
            c[self.x][self.y]='O'
            self.thisgrid=c
            self.energy=(self.energy//3)
        self.showGrid(self.energy)
        if self.energy<1:
            gameover()
    def rotateanticlockwise(self):
        a=[]
        e=self.goal
        for i in range(self.n):
            a.append(self.thisgrid[i])
        for i in range(self.n):
            for j in range(self.n//2):
                t=a[i][j]
                a[i][j]=a[i][-(j+1)]
                a[i][-(j+1)]=t
        c=[]
        for i in range(self.n):
            c.append([])
            for j in range(self.n):
                c[i].append('')
        for i in range(self.n):
            for j in range(self.n):
                c[j][i]=a[i][j]
        d=obstacle(self.x,self.y)
        if c[self.x][self.y]=='#':
            print("GRID CANNOT BE ROTATED")
            time.sleep(2)
        else:
            f=find('G',c)
            t1=c[e[0]][e[1]]
            c[f[0]][f[1]]=t1
            c[e[0]][e[1]]='G'
            f=find('O',c)
            if f==(-1,-1):
                f=find('S',c)
            t1=c[self.x][self.y]
            c[f[0]][f[1]]=t1
            c[self.x][self.y]='O'
            self.thisgrid=c
            self.energy=(self.energy//3)
        self.showGrid(self.energy)
        if self.energy<1:
            gameover()
            
            
                
                
class player(grid):
    def __init__(self,n):
        super().__init__(n)
        self.x=self.start[0]
        self.y=self.start[1]
        self.energy=2*n
        self.t=self.thisgrid[self.x][self.y]
        
    def moveup(self,a):
        
        for i in range(a):
            self.thisgrid[self.x][self.y]=self.t
            self.energy-=1
            if self.x==0:
                self.x=(self.n-1)
                check=checkstatus(self.x,self.y,self.thisgrid)
                self.energy=update(self.energy,self.n,check)
            else:
                self.x-=1
                check=checkstatus(self.x,self.y,self.thisgrid)
                self.energy=update(self.energy,self.n,check)
            self.t=self.thisgrid[self.x][self.y]
            self.thisgrid[self.x][self.y]='O'
            self.showGrid(self.energy)
            if self.energy<1:
                gameover()
    def movedown(self,a):
        
        for i in range(a):
            self.thisgrid[self.x][self.y]=self.t
            self.energy-=1
            if self.x==((self.n)-1):
                self.x=0
                check=checkstatus(self.x,self.y,self.thisgrid)
                self.energy=update(self.energy,self.n,check)
            else:
                self.x+=1
                check=checkstatus(self.x,self.y,self.thisgrid)
                self.energy=update(self.energy,self.n,check)
            self.t=self.thisgrid[self.x][self.y]
            self.thisgrid[self.x][self.y]='O'
            self.showGrid(self.energy)
            if self.energy<1:
                gameover()
    def moveright(self,a):
        
        for i in range(a):
            self.thisgrid[self.x][self.y]=self.t
            self.energy-=1
            if self.y==((self.n)-1):
                self.y=0
                check=checkstatus(self.x,self.y,self.thisgrid)
                self.energy=update(self.energy,self.n,check)
            else:
                self.y+=1
                check=checkstatus(self.x,self.y,self.thisgrid)
                self.energy=update(self.energy,self.n,check)
            self.t=self.thisgrid[self.x][self.y]
            self.thisgrid[self.x][self.y]='O'
            self.showGrid(self.energy)
            if self.energy<1:
                gameover()
    def moveleft(self,a):
        
        for i in range(a):
            self.thisgrid[self.x][self.y]=self.t
            self.energy-=1
            if self.y==0:
                self.y=(self.n-1)
                check=checkstatus(self.x,self.y,self.thisgrid)
                self.energy=update(self.energy,self.n,check)
            else:
                self.y-=1
                check=checkstatus(self.x,self.y,self.thisgrid)
                self.energy=update(self.energy,self.n,check)
            self.t=self.thisgrid[self.x][self.y]
            self.thisgrid[self.x][self.y]='O'
            self.showGrid(self.energy)
            if self.energy<1:
                gameover()
        
            
        
        
                    
            
                
                
        


class obstacle():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def returnxy(self):
        return (self.x,self.y)

class reward():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def returnxy(self):
        return (self.x,self.y)
os.system('cls')
print("XXXXXXXXXXXXX-----------WELCOME TO THE GAME-----------XXXXXXXXXXXXX")
b=input("Size of the Grid should be")
b=int(b)
a=player(b)
def game():
    m=1
    while(a.energy>0):
        if m==1:
            print('S denotes the initial position of the player')
            c=input('Your Move,choose from U(up),D(down),L(left),R(right),A(anticlockwise),C(clockwise)')
        else:
            c=input('Your Move,choose from U(up),D(down),L(left),R(right),A(anticlockwise),C(clockwise)')
        for i in range(0,len(c),2):
            d1=c[i]
            d2=int(c[i+1:i+2])
            
        
            if d1=='R' or d1=='r':
                a.moveright(d2)
                if a.energy<=0:
                    return 0
                if (a.x,a.y)==a.goal:
                    return 1
            elif d1=='L' or d1=='l':
                a.moveleft(d2)
                if a.energy<=0:
                    return 0
                if (a.x,a.y)==a.goal:
                    return 1
            elif d1=='U' or d1=='u':
                a.moveup(d2)
                if a.energy<=0:
                    return 0
                if (a.x,a.y)==a.goal:
                    return 1
            elif d1=='D' or d1=='d':
                a.movedown(d2)
                if a.energy<=0:
                    return 0
                if (a.x,a.y)==a.goal:
                    return 1
            elif d1=='A'  or d1=='a':
                for i in range(d2):
                    a.rotateanticlockwise()
                    if a.energy<=0:
                        return 0
                    if (a.x,a.y)==a.goal:
                        return 1
            elif d1=='C' or d1=='c':
                for i in range(d2):
                    a.rotateclockwise()
                    if a.energy<=0:
                        return 0
                    if (a.x,a.y)==a.goal:
                        return 1
        m+=1
f=game()
if f==0:
    print("Game Over , You Lose")
if f==1:
    print("Game Over , You WIN!!!!")

        


