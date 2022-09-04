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
type_play=1

def random_play():
        q = defaultdict(lambda: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        #with open('qtable-trainv3-ep1-200.json') as f:
        #        q_ai = json.load(f)
        #q.update(q_ai)
        rewards = np.array([])
        games = [splender() for i in range(400)]
        #     Hyperparameters
        epsilon = 1
        epsilon_min = 0.05
        epsilon_decay = 0.9
        timesleep=1
        timelook=10
        ep=0
        winp1=0
        winp2=0
        gamma = 0.9
        alpha = 0.1
        def updateQ(s, a, new_s, r):
                q_value = q[str(s)].copy()
                q_value_a=q_value[a]
                #print("q_value_a : {}".format(q_value_a))
                max_q=max(q[str(new_s)])
                #print("max_q : {}".format(max_q))
                #print("r : {}".format(r))
                q_value[a] = ((1 - alpha) * q_value_a) + (alpha * (r + (gamma * max_q)))
                #print("q_value : {}".format(q_value[a]))
                q[str(s)] = q_value
        def check_reward(id_buy,player,ep):
                score=int(game.card[id_buy]["score"])
                if player == 1:
                        if game.score_P1+score>=10:
                                return ((game.score_P1+score)/ep)+100
                        else:
                                return ((game.score_P1+score)/ep)
                elif player == 2:
                        if game.score_P2+score>=10:
                                return ((game.score_P2+score)/ep)+100
                        else:
                                return ((game.score_P2+score)/ep)
        def new_q(q, moves):
            new_q = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for i in range(len(q)):
                if i not in moves:
                    new_q[i] = -200
                else:
                    new_q[i] = q[i]
            return new_q
        def check_opencard(opencard):
                list_card=[]
                for i in range(len(opencard)):
                        if opencard[i]==1:
                                list_card.append(i)
                return list_card

        for game in games:
                ep+=1
                Round = 1
                player=0
                select_gem_p1=1
                select_gem_p2=1
                game.open_card_buy()
                def showpage():
                        clear_output(wait=True)
                        clear()
                        print("Epsilon : {}".format(ep))
                        print("Round : {} || Player : {}".format(math.ceil(Round/2),player))
                        print("AI Win_P1 : {}/{}".format(winp1,ep-1))
                        print("Random Win_P2 : {}/{}".format(winp2,ep-1))
                        print("")
                        print("-------------Score--------------")
                        print("AI Score_P1 : {}".format(game.score_P1))
                        print("Random Score_P2 : {}".format(game.score_P2))
                        game.show_field()
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
                while(True):
                        if Round%2 == 0 :
                                player = 2
                        elif Round%2 == 1 :
                                player = 1
                        game.open_card_buy()
                        showpage()
                        if(game.score_P1>=10):
                                
                                clear()
                                clear_output(wait=True)
                                print("Round : {}".format(math.ceil(Round/2)))
                                print("Score_P1 : {}".format(game.score_P1))
                                print("Score_P2 : {}".format(game.score_P2))
                                print("Player 1 is Win")
                                winp1+=1
                                time.sleep(timesleep)
                                break
                        elif game.score_P2>=10:
                                
                                clear()
                                clear_output(wait=True)
                                print("Round : {}".format(math.ceil(Round/2)))
                                print("Score_P1 : {}".format(game.score_P1))
                                print("Score_P2 : {}".format(game.score_P2))
                                print("Player 2 is Win")
                                winp2+=1
                                time.sleep(timesleep)
                                break
                        if type_play == 1 :
                                print("Player {}".format(player))
                                listaction=[]
                                listaction.append("GEM")
                                list_buy_card=game.check_buy_card(player)
                                #print(len(list_buy_card))
                                #game.show_field()
                                if player ==1:
                                        
                                        randomeps=random.uniform(0, 1)
                                        #print("Random {} / epsilon {}".format(randomeps,epsilon))
                                        card_open_ck=check_opencard(game.open_card)
                                        print(new_q(q[str(game.card_p1)], card_open_ck))
                                        if (randomeps > epsilon):
                                                print(card_open_ck)
                                                id_buy = np.argmax(new_q(q[str(game.card_p1)], card_open_ck))
                                                print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                if id_buy not in list_buy_card:
                                                        if(len(list_buy_card)>0):
                                                                gem_player=getgem_playe(player)
                                                                pay_gem=np.array([int(game.card[id_buy]["red_buy"]),int(game.card[id_buy]["blue_buy"]),int(game.card[id_buy]["green_buy"])])
                                                                pay_gem[0]=pay_gem[0]-gem_player[0]
                                                                pay_gem[1]=pay_gem[1]-gem_player[1]
                                                                pay_gem[2]=pay_gem[2]-gem_player[2]
                                                                pay_gem[pay_gem < 0] = 0
                                                                gemcheck=pay_gem[0]+pay_gem[1]+pay_gem[2]
                                                                if gemcheck<=2:
                                                                        listaction.append("GEM")
                                                                else:
                                                                        listaction.append("BUY")
                                                                        id_buy=random.choice(list_buy_card)
                                                        else:
                                                                listaction.append("GEM")
                                                else:
                                                        listaction.append("BUY")  
                                        else:
                                                if(len(list_buy_card)>0):
                                                        listaction.append("BUY")
                                                        id_buy=random.choice(list_buy_card)
                                                else:
                                                        listaction.append("GEM")
                                                        id_buy=-1
                                elif player ==2:
                                        if(len(list_buy_card)>0):
                                                listaction.append("BUY")
                                                id_buy=random.choice(list_buy_card)
                                        else:
                                                listaction.append("GEM")
                                                id_buy=-1
                                print(listaction)
                                action=random.choices(population=listaction,weights=[0.001,0.999])
                                                
                                if(action[0]=="BUY"):
                                        print("BUY")
                                        game.action_buy(player,id_buy)
                                        if player==1:
                                                
                                                if not(np.array_equal(game.old_card_P1, game.card_p1)):
                                                        updateQ(game.old_card_P1, id_buy, game.card_p1, check_reward(id_buy,player,select_gem_p1))
                                                select_gem_p1=1
                                        elif player==2:
                                                
                                                if not(np.array_equal(game.old_card_P2, game.card_p2)):
                                                        updateQ(game.old_card_P2, id_buy, game.card_p2, check_reward(id_buy,player,select_gem_p2))
                                                select_gem_p2=1
                                        #sp.show_field()
                                else:
                                        print("GEM")
                                        game.action_gem(player,id_buy,"bot")
                                        if player ==1:
                                                select_gem_p1+=1
                                                if (randomeps > epsilon):
                                                        time.sleep(timelook)
                                        elif player==2:
                                                select_gem_p2+=1                

                                #print("Player {} Action {} ".format(str(player),action[0]))
                                Round+=1
                                #time.sleep(5)
                                #clear_output(wait=True)
                                #print("Round : {} Player : {} || ".format(math.ceil(Round/2),player))
                                #print("Player {} Last Action {} ".format(str(player),action[0]))
                                time.sleep(timesleep)
                                showpage()
                if (epsilon > epsilon_min):
                        epsilon *= epsilon_decay
        fo = open("qtable-trainv3-ep4-400.json", "w")
        json.dump(q, fo)
        fo.close()
        return q
random_play()