import os
from IPython.display import clear_output
import time 
import math
import numpy as np
import random
from collections import defaultdict
import json
import csv
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from splender import splender
clear = lambda: os.system('cls')
game = splender()
Round = 0
player=0
type_play=2
with open('qtable-trainv5-ep1-2000-1200.json') as f:
    q = json.load(f)
def legal_move(board):
    #print(type(board))
    #print(board)
    listdata=np.asarray(np.where(np.array(board) == 0)).flatten()
    #print(listdata)
    return listdata
def new_q(q, moves):
    new_q = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(q)):
        if i not in moves:
            new_q[i] = -200
        else:
            new_q[i] = q[i]
    return new_q
def check_select_card(player):
    def getgem_playe(player):
        gem_player=[0,0,0]
        if player==1:
            gem_player[0]+=game.gem_P1[0]+game.gem_bonus_P1[0]
            gem_player[1]+=game.gem_P1[1]+game.gem_bonus_P1[1]
            gem_player[2]+=game.gem_P1[2]+game.gem_bonus_P1[2]
        elif player==2:
            gem_player[0]+=game.gem_P2[0]+game.gem_bonus_P2[0]
            gem_player[1]+=game.gem_P2[1]+game.gem_bonus_P2[1]
            gem_player[2]+=game.gem_P2[2]+game.gem_bonus_P2[2]
        return gem_player
    list_card=[]
    for i in range(len(game.open_card)):
        if game.open_card[i] == 1:
            gem_player=getgem_playe(player)
            pay_gem=np.array([int(game.card[i]["red_buy"]),int(game.card[i]["blue_buy"]),int(game.card[i]["green_buy"])])
            pay_gem[0]=pay_gem[0]-gem_player[0]
            pay_gem[1]=pay_gem[1]-gem_player[1]
            pay_gem[2]=pay_gem[2]-gem_player[2]

            pay_gem[pay_gem < 0] = 0
            if np.sum(pay_gem)<=4:
                list_card.append(i)
    return list_card
def check_opencard(opencard):
    list_card=[]
    for i in range(len(opencard)):
        if opencard[i]==1:
            list_card.append(i)
    return list_card
select_gem_p1=1
needid_buy_p1=-1
while(True):
        Round+=1
        clear_output(wait=True)
        if Round%2 == 0 :
                player = 2
        elif Round%2 == 1 :
                player = 1
        print("Round : {} Player : {} || ".format(math.ceil(Round/2),player))
        game.open_card_buy()
        def showpage():
            clear_output(wait=True)
            clear()
            print("Round : {} || Player : {}".format(math.ceil(Round/2),player))
            print("-------------Score--------------")
            print("AI Score_P1 : {}".format(game.score_P1))
            print("Hulman Score_P2 : {}".format(game.score_P2))
            game.show_field()
        showpage()
        
        if type_play == 2 :
            if player == 1:
                print("Bot")
                listaction=[]
                listaction.append("GEM")
                id_buy=-1
                if select_gem_p1 >=5:
                    select_gem_p1=5
                    needid_buy_p1=-1
                list_buy_card=game.check_buy_card(player)
                card_open_ck=check_opencard(game.open_card)
                list_select_card=check_select_card(player)
                id_buy = np.argmax(new_q(q[str(game.card_p1)], list_select_card))
                if needid_buy_p1>=0 and needid_buy_p1 in card_open_ck:
                    if needid_buy_p1 in list_buy_card:
                        listaction.append("BUY")
                        id_buy=needid_buy_p1
                        print("Need BUY {}".format(game.card[id_buy]["namecard"])) 
                        needid_buy_p1=-1        
                    else:
                        listaction.append("GEM")
                        id_buy=needid_buy_p1
                        print("Need BUY {}".format(game.card[id_buy]["namecard"]))             
                else:
                                                        
                    if len(list_buy_card)>0:
                        id_buy = np.argmax(new_q(q[str(game.card_p1)], list_buy_card))
                    else:
                        id_buy = np.argmax(new_q(q[str(game.card_p1)], list_select_card))                                            
                        if id_buy in list_buy_card:
                            print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                            listaction.append("BUY")
                            needid_buy_p1=-1
                        else:
                            if id_buy in list_buy_card:
                                print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                listaction.append("BUY")
                                needid_buy_p1=-1
                            else:
                                needid_buy_p1=id_buy
                                print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                listaction.append("GEM")
                action=[listaction[len(listaction)-1]]
                if(action[0]=="BUY"):
                    print("BUY")
                    game.action_buy(player,id_buy)
                else:    
                    print("GEM")
                    print("ID BUY {}".format(id_buy))
                    game.action_gem(player,id_buy,"bot")
                time.sleep(1)
            elif player == 2:
                showpage()
                while(True):
                    showpage()
                    list_buy_card=game.check_buy_card(player)
                    if(len(list_buy_card)>0):
                        print("[0] : BUY")
                    
                    if(np.sum(game.gem)>=2):
                        print("[1] : GEM")
                    elif(np.sum(game.gem)<2) and (len(list_buy_card)<=0):
                        print("Pass ::")
                        time.sleep(10)
                        break
                    action_type = int(input("เลือก ACTION: "))
                    if(action_type==1):
                        break
                    elif(action_type==0 and len(list_buy_card)>0):
                        break
                    else:
                        clear_output(wait=True)
                if action_type ==0:
                    while(True):
                        showpage()
                        buy_id = int(input("เลือก ID: "))
                        re_turn=game.action_buy(player,buy_id)
                        if re_turn != False:
                            break
                elif action_type ==1:
                    i=0
                    while(True):
                        if i==2:
                            break
                        else:
                            showpage()
                            gem_id = int(input("เลือก GEM: "))
                            if gem_id == 0 or gem_id == 1 or gem_id==2:
                                re_turn1=game.action_gem(player,gem_id,type_play)
                                if re_turn1!=False:
                                    i+=1
            if(game.score_P1>=10 and Round%2 == 0 and game.score_P1>game.score_P2):
                                
                clear()
                clear_output(wait=True)
                print("Round : {}".format(math.ceil(Round/2)))
                print("Score_P1 : {}".format(game.score_P1))
                print("Score_P2 : {}".format(game.score_P2))
                print("Player 1 is Win")
                time.sleep(20)
                break
             
            elif (game.score_P2>=10 and Round%2 == 0 and game.score_P2>game.score_P1):
                                
                clear()
                clear_output(wait=True)
                print("Round : {}".format(math.ceil(Round/2)))
                print("Score_P1 : {}".format(game.score_P1))
                print("Score_P2 : {}".format(game.score_P2))
                print("Player 2 is Win")
                time.sleep(20)
                break
            elif (game.score_P1>=10 and game.score_P2>=10 and Round%2 == 0 and game.score_P2 == game.score_P1 and np.sum(game.card_p2)<np.sum(game.card_p1)):
                clear()
                clear_output(wait=True)
                print("Round : {}".format(math.ceil(Round/2)))
                print("Score_P1 : {}".format(game.score_P1))
                print("Score_P2 : {}".format(game.score_P2))
                print("Player 2 is Win")
                time.sleep(20)
                break
            elif (game.score_P1>=10 and game.score_P2>=10 and Round%2 == 0 and game.score_P2 == game.score_P1 and np.sum(game.card_p1)<np.sum(game.card_p2)):
                clear()
                clear_output(wait=True)
                print("Round : {}".format(math.ceil(Round/2)))
                print("Score_P1 : {}".format(game.score_P1))
                print("Score_P2 : {}".format(game.score_P2))
                print("Player 1 is Win")
                time.sleep(20)
                break
            elif (game.score_P1>=10 and game.score_P2>=10 and Round%2 == 0 and game.score_P2 == game.score_P1 and np.sum(game.card_p2)==np.sum(game.card_p1)):
                clear()
                clear_output(wait=True)
                print("Round : {}".format(math.ceil(Round/2)))
                print("Score_P1 : {}".format(game.score_P1))
                print("Score_P2 : {}".format(game.score_P2))
                print("Player 1 = Player 2")
                time.sleep(20)
                break