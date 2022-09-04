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
with open('qtablespen150new.json') as f:
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
        if(game.score_P1>=10):
                time.sleep(5)
                clear()
                clear_output(wait=True)
                print("Round : {}".format(math.ceil(Round/2)))
                print("-------------Score--------------")
                print("Score_P1 : {}".format(game.score_P1))
                print("Score_P2 : {}".format(game.score_P2))
                print("Player 1 is Win")
                break
        elif game.score_P2>=10:
                time.sleep(5)
                clear()
                clear_output(wait=True)
                print("Round : {}".format(math.ceil(Round/2)))
                print("-------------Score--------------")
                print("Score_P1 : {}".format(game.score_P1))
                print("Score_P2 : {}".format(game.score_P2))
                print("Player 2 is Win")
                break
        if type_play == 2 :
            if player == 1:
                print("Bot")
                listaction=[]
                listaction.append("GEM")
                list_buy_card=game.check_buy_card(player)
                #print(len(list_buy_card))
                legal_moves = legal_move(game.open_used)
                
                try:
                    print(q[str(game.open_used)])
                    cardbuy = np.argmax(new_q(q[str(game.open_used)], legal_moves))
                except KeyError:
                    if(len(list_buy_card)>0):
                        cardbuy=random.choice(list_buy_card)
                    else:
                        cardbuy=-1

                showpage()
                if(len(list_buy_card)>0):
                    listaction.append("BUY")
                else:
                    listaction.append("GEM")
                print(listaction)
                action=random.choices(population=listaction,weights=[0.01,0.99])
                if(action[0]=="BUY"):
                    game.action_buy(player,cardbuy)
                else:
                    game.action_gem(player,cardbuy,"bot")
                print("Player {} Action {} ".format(str(player),action[0]))
                time.sleep(1)
            elif player == 2:
                while(True):
                    showpage()
                    list_buy_card=game.check_buy_card(player)
                    if(len(list_buy_card)>0):
                        print("[0] : BUY")
                    print("[1] : GEM")
                    action_type = int(input("เลือก ACTION: "))
                    if(action_type==1 or action_type==0):
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