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
        #with open('splender.json') as f:
                #q = json.load(f)
        rewards = np.array([])
        games = [splender() for i in range(150)]
        #     Hyperparameters
        epsilon = 1
        epsilon_min = 0.05
        epsilon_decay = 0.96
        ep=0
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
        
        for game in games:
                ep+=1
                Round = 1
                player=0
                game.open_card_buy()
                def showpage():
                        clear_output(wait=True)
                        clear()
                        print("Epsilon : {}".format(ep))
                        print("Round : {} || Player : {}".format(math.ceil(Round/2),player))
                        print("AI Score_P1 : {}".format(game.score_P1))
                        print("Random Score_P2 : {}".format(game.score_P2))
                        game.show_field()
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
                                time.sleep(2)
                                break
                        elif game.score_P2>=10:
                                
                                clear()
                                clear_output(wait=True)
                                print("Round : {}".format(math.ceil(Round/2)))
                                print("Score_P1 : {}".format(game.score_P1))
                                print("Score_P2 : {}".format(game.score_P2))
                                print("Player 2 is Win")
                                time.sleep(2)
                                break
                        if type_play == 1 :
                                print("Bot")
                                listaction=[]
                                listaction.append("GEM")
                                list_buy_card=game.check_buy_card(player)
                                #print(len(list_buy_card))
                                #game.show_field()
                                print(new_q(q[str(game.open_used)], list_buy_card))
                                if(len(list_buy_card)>0):

                                        listaction.append("BUY")
                                        if player ==1:
                                                if (random.uniform(0, 1) > epsilon):
                                                        id_buy = np.argmax(new_q(q[str(game.open_used)], list_buy_card))
                                                else:
                                                        id_buy=random.choice(list_buy_card)
                                        elif player ==2:
                                                id_buy=random.choice(list_buy_card)
                                else:
                                        listaction.append("GEM")
                                        if player ==1:
                                                if (random.uniform(0, 1) > epsilon):
                                                        id_buy = np.argmax(new_q(q[str(game.open_used)], game.open_card))
                                                else:
                                                        id_buy=-1
                                        elif player ==2:
                                                id_buy=-1
                                print(listaction)
                                action=random.choices(population=listaction,weights=[0.2,0.8])
                                                
                                if(action[0]=="BUY"):
                                        game.action_buy(player,id_buy)
                                        if not(np.array_equal(game.old_open_used, game.open_used)):
                                                if player==1:
                                                        updateQ(game.old_open_used, id_buy, game.open_used, check_reward(id_buy,player,ep))
                                                elif player==2:
                                                        updateQ(game.old_open_used, id_buy, game.open_used, check_reward(id_buy,player,ep))
                                        #sp.show_field()
                                else:
                                        game.action_gem(player,id_buy,"bot")
                                #print("Player {} Action {} ".format(str(player),action[0]))
                                Round+=1
                                #time.sleep(5)
                                #clear_output(wait=True)
                                #print("Round : {} Player : {} || ".format(math.ceil(Round/2),player))
                                #print("Player {} Last Action {} ".format(str(player),action[0]))
                                time.sleep(1)
                                showpage()
                                if (epsilon > epsilon_min):
                                        epsilon *= epsilon_decay
        fo = open("qtablespen150gem.json", "w")
        json.dump(q, fo)
        fo.close()
        return q
random_play()