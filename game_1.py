import pygame
import numpy as np
from pygame.constants import KEYDOWN
from more_itertools import distinct_permutations
#variables
count=0
player=1

pygame.init()
fontall=pygame.font.Font('freesansbold.ttf',32)
n=int(input("enter the size :"))

BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
WHITE=(255,255,255)
BOXCLR=(255,255,0)
WIDTH=n*100
HEIGHT=n*100
BACKGROUND=(0,255,0)#rgb value
LNCOLOR=(0,0,0)
LNWIDTH=10
CRRADIUS=30
CRWIDTH=10
state_size=3139
action_size=9
state=np.empty(3193,dtype='int')
action=np.empty(9,dtype='int')

for i in range (action_size):
    action[i]=i


def state_to_number(seq):
    num=0
    for val in seq:
        num=num+(3**seq.index(val))*val
    return num


pos_state1=[0,0,0,0,0,0,0,1,2]
perm=list(distinct_permutations(pos_state1))
for i in range(72):
    state[i+1]=state_to_number(perm[i])

pos_state2=[0,0,0,0,0,1,1,2,2]
perm=list(distinct_permutations(pos_state2))
for i in range(756):
    state[i+73]=state_to_number(perm[i])

pos_state3=[0,0,0,1,1,1,2,2,2]
perm=list(distinct_permutations(pos_state3))
for i in range(1680):
    state[i+829]=state_to_number(perm[i])

pos_state4=[0,1,1,1,1,2,2,2,2]
perm=list(distinct_permutations(pos_state4))
for i in range(630):
    state[i+2509]=state_to_number(perm[i])


#probability transition function
p=np.zeros((3139,9,3139),dtype='int')

for i in range(3139):
    for j in range(9):
        if(1<=i<=72):
            for k in range(1,73):
                p[i][j][k]=1/72
        if(73<=i<=828):
            for k in range(73,829):
                p[i][j][k]=1/756
        if(829<=i<=2508):
            for k in range(829,2509):
                p[i][j][k]=1/1680
        if(2509<=i<=3138):
            for k in range(2509,3139):
                p[i][j][k]=1/630
        




screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC_TAC_TOE')
def design_board():
    screen.fill(BACKGROUND)
    for i in range (n+1):
        pygame.draw.line(screen,LNCOLOR,(i*100,0),(i*100,n*100),LNWIDTH)
        pygame.draw.line(screen,LNCOLOR,(0,i*100),(n*100,i*100),LNWIDTH)

design_board()
#BOARD
BOARD=np.zeros((n,n))

def mark_square(row,col,player):
    global count
    BOARD[row][col]=player
    if(player==1):
        pygame.draw.circle(screen,RED,(col*100+50,row*100+50),CRRADIUS,CRWIDTH)
    else:
        pygame.draw.line(screen,WHITE,(col*100+10,row*100+10),(col*100+90,row*100+90),LNWIDTH)
        pygame.draw.line(screen,WHITE,(col*100+10,row*100+90),(col*100+90,row*100+10),LNWIDTH)
    count +=1

def available_square(row,col):
    return BOARD[row][col]==0

def check_win(player):
    global game_over
    diag1=np.empty(n,dtype='int')
    diag2=np.empty(n,dtype='int')
    
    for i in range(n):
        diag1[i]=BOARD[i][i]
        diag2[i]=BOARD[n-i-1][i]
    dc1=np.count_nonzero(diag1==player)
    dc2=np.count_nonzero(diag2==player)
    
    for i in range(n):
        count=0
        count=np.count_nonzero(BOARD[i]==player)
        if(count==n):
            break
    if(count!=n):
        for i in range(n):
            count=0
            count=np.count_nonzero(BOARD[:,i]==player)
            if(count==n):
                break



    for i in range (n):
        if(dc1==n or dc2==n or count==n):
            end_text="PLAYER "+str(player)+"WIN"
            result=fontall.render(end_text,True,BLUE)
            screen.blit(result,((n-2)*50 ,100))
            end_text="HIT r TO RESTART"
            result=fontall.render(end_text,True,BLUE)
            screen.blit(result,((n-2)*50 ,200))
            game_over=True
        elif(count==n*n):
            end_text="MATCH DRAW"
            result=fontall.render(end_text,True,BLUE)
            screen.blit(result,((n-2)*50 ,100))
            end_text="HIT r TO RESTART"
            result=fontall.render(end_text,True,BLUE)
            screen.blit(result,((n-2)*50 ,200))
            game_over=True
        else:
            pass
            
game_over=False
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            cord_x=event.pos[0]
            cord_y=event.pos[1]
            clicked_row=(int(cord_y)//100)
            clicked_col=(int(cord_x)//100)
            if(available_square(clicked_row,clicked_col)):
                mark_square(clicked_row,clicked_col,player)
                check_win(player)
                if(player==1):
                    player=2
                else:
                    player=1

        if event.type==KEYDOWN:
            if event.key==pygame.K_r:
                player=1
                count=0
                game_over=False
                BOARD=np.zeros((n,n))
                design_board()

    pygame.display.update()

print(state)