import pygame
import copy
import solver as s
import pickle
import random
import os

pygame.init()
black=0,0,0
white=255,255,255
gery=240,240,240
red=255,0,0
green=0,255,0
blue=0,0,255
setup_mode=False
solve_mode=False
solve_skip=False
done=False
skip=False
save=True
speed=200
i=0
j=0

win = pygame.display.set_mode((500,370))
font = pygame.font.SysFont('comicsans', 30)
pygame.display.set_caption("Sudoku Solver")
run=True
setup_board=[[0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]

list_of_board=[]

clock = pygame.time.Clock()

def update_screen(x=-1,y=-1):

    background(x,y)
    if(setup_mode):
        pygame.draw.rect(win,blue, ((i*40)+5,(j*40)+5, 40, 40), 2)
    pygame.display.update()

def background(k,y):
    pygame.draw.rect(win, white, (0, 0, 500, 370))
    pygame.draw.rect(win, gery, (5, 5, 360, 360))
    pygame.draw.rect(win, black, (5, 5, 360, 360), 3)

    for x in range(5,360,40):
        if  (x-5)%(40*3) == 0:
            pygame.draw.line(win,black,(x,5),(x,365),2)
            pygame.draw.line(win,black,(5,x),(365,x),2)
        else:
            pygame.draw.line(win,black,(x,5),(x,365),1)
            pygame.draw.line(win,black,(5,x),(365,x),1)

    pygame.draw.rect(win, (102,205,205), (380,40, 100, 40))
    pygame.draw.rect(win, black, (380,40, 100, 40), 1)
    win.blit(font.render('Save', 1, (0,0,0)), (400, 50))

    pygame.draw.rect(win, (255,153,51), (380,90, 100, 40))
    pygame.draw.rect(win, black, (380,90, 100, 40), 1)
    win.blit(font.render('Reset', 1, (0,0,0)), (400, 100))
    
    
    pygame.draw.rect(win, (255,51,51), (380,140, 100, 40))
    pygame.draw.rect(win, black, (380,140, 100, 40), 1)
    if(setup_mode):
        win.blit(font.render('Ok', 1, (0,0,0)), (400, 150))
    else:
        win.blit(font.render('Setup', 1, (0,0,0)), (400, 150))
    
    pygame.draw.rect(win,(51,255,255), (380,190, 100, 40))
    pygame.draw.rect(win, black, (380,190, 100, 40), 1)
    win.blit(font.render('Solve', 1, (0,0,0)), (400, 200))

    pygame.draw.rect(win,green, (380,240, 100, 40))
    pygame.draw.rect(win, black, (380,240, 100, 40), 1)
    win.blit(font.render('D - Solve', 1, (0,0,0)), (390, 250))

    # pygame.draw.rect(win,(255,0,127), (380,290, 100, 40))
    # pygame.draw.rect(win, black, (380,290, 100, 40), 1)
    win.blit(font.render('Next', 1, (0,0,0)), (400, 300))
        
    print_board(k,y)
   
def print_board(x,y):
    
    pos_X=20
    
    for i in range(9):
        pos_y=20
        for j in range(9):
            
            if(setup_mode and setup_board[j][i] != 0):
                
                win.blit(font.render(str(setup_board[j][i]), 1, (255,0,0)), (pos_X, pos_y))
                
                
            elif(s.board[j][i] != 0 and not setup_mode):
                
                if(setup_board[j][i]!=0):
                    win.blit(font.render(str(s.board[j][i]), 1, blue), (pos_X, pos_y))

                else:
                    win.blit(font.render(str(s.board[j][i]), 1, (0,0,0)), (pos_X, pos_y))

            if(x!=-1 and y!=-1): 
                # print(x,y)
                pygame.draw.rect(win,red, ((y*40)+5,(x*40)+5, 40, 40), 3) 
                
                
            pos_y+=40
        
        pos_X+=40

    

    if(done):
        win.blit(font.render('Done!!!!', 1, (0,0,0)), (400, 350))

def display_board(x=-1,y=-1):
    
    if(not skip):
        update_screen(x,y)
        clock.tick(speed)

s.display_board=display_board
try:
    with open(os.getcwd()+"\\list_of_boards.txt", "rb") as fp:   # Unpickling
        list_of_board=pickle.load(fp)
        setup_mode=True
except FileNotFoundError:
    print("File Not Found")
except Exception:
    print('Empty File')
else:
    setup_board=list_of_board[random.randint(0,len(list_of_board)-1)]

while run:
    # if not solve_mode:
    clock.tick(60)
    key=-1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()

            if pos[0]>380 and pos[0]<480 and pos[1]>40  and pos[1]<80 : #save
                # print("save")
                list_of_board.append(setup_board)
                with open(os.getcwd()+"\\list_of_boards.txt", "wb") as fp:   #Pickling
                    pickle.dump(list_of_board, fp)

            if pos[0]>380 and pos[0]<480 and pos[1]>90 and pos[1]<130 :  #reset
                
                setup_mode=False
                solve_mode=False
                
                done=False
                if(s.board!=setup_board):
                    s.board=copy.deepcopy(setup_board)
                else:
                    setup_board=[[0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0,0]]
            
            if pos[0]>380 and pos[0]<480 and pos[1]>140 and pos[1]<180 : #setup
                done=False
                if(setup_mode):
                    setup_mode=False
                    s.board=copy.deepcopy(setup_board)
                else:
                    setup_mode=True
                    setup_board=copy.copy(s.board)
                
            if pos[0]>380 and pos[0]<480 and pos[1]>190 and pos[1]<230 : #solve by sowing steps
                if(setup_mode):
                    setup_mode=False
                    s.board=copy.deepcopy(setup_board)
                solve_mode=True
                
                done=s.find_the_val(0,0)
                      
            if pos[0]>380 and pos[0]<480 and pos[1]>240  and pos[1]<280 : # solve in one go
                if(setup_mode):
                    setup_mode=False
                    s.board=copy.deepcopy(setup_board)
                # print("skip")
                skip=True
                done=s.find_the_val(0,0)
                skip=False
            
            if pos[0]>380 and pos[0]<480 and pos[1]>290  and pos[1]<330 : #next
                done=False
                setup_mode=True
                # print("change")
                setup_board=list_of_board[random.randint(0,len(list_of_board)-1)]

        if event.type == pygame.KEYDOWN and setup_mode:
            if event.key == pygame.K_LEFT and i>0:
                i-=1
            if event.key == pygame.K_RIGHT and i<8:
                i+=1
            if event.key == pygame.K_UP and j>0:
                j-=1
            if event.key == pygame.K_DOWN and j<8:
                j+=1
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                key = 1
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                key = 2
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                key = 3
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                key = 4
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                key = 5
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                key = 6
            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                key = 7
            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                key = 8
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                key = 9
            if event.key == pygame.K_DELETE:
                setup_board[j][i]=0   
            if key!=-1:
                setup_board[j][i]=key
            
    
    # keys = pygame.key.get_pressed()
        
    update_screen()
    
pygame.quit()