import pygame
import numpy as np
from pygame.constants import KEYDOWN

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
    diag1=0
    diag2=0
    
    for i in range(n):
        diag1+=BOARD[i][i]
        diag2+=BOARD[n-i-1][i]
    
    arr1=BOARD.sum(axis=0)
    arr2=BOARD.sum(axis=1)
    for i in range (n):
        if(arr1[i]==n*player or arr2[i]==n*player or diag1==n*player or diag2==n*player):
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
                player=player*-1

        if event.type==KEYDOWN:
            if event.key==pygame.K_r:
                player=1
                count=0
                game_over=False
                BOARD=np.zeros((n,n))
                design_board()

    pygame.display.update()

