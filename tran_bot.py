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
        rewards = np.array([])
        games = [splender() for i in range(5000)]
        #     Hyperparameters
        epsilon = 1
        epsilon_min = 0.05
        epsilon_decay = 0.999997
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
        for game in games:
                Round = 1
                player=0
                game.open_card_buy()
                while(True):

                        clear_output(wait=True)
                        clear()
                        if Round%2 == 0 :
                                player = 2
                        elif Round%2 == 1 :
                                player = 1
                        print("Round : {} || Player : {}".format(math.ceil(Round/2),player))
                        print("Score_P1 : {}".format(game.score_P1))
                        print("Score_P2 : {}".format(game.score_P2))
                        game.open_card_buy()
                        if(game.score_P1>=10):
                                time.sleep(5)
                                clear()
                                clear_output(wait=True)
                                print("Round : {}".format(math.ceil(Round/2)))
                                print("Score_P1 : {}".format(game.score_P1))
                                print("Score_P2 : {}".format(game.score_P2))
                                print("Player 1 is Win")
                                break
                        elif game.score_P2>=10:
                                time.sleep(5)
                                clear()
                                clear_output(wait=True)
                                print("Round : {}".format(math.ceil(Round/2)))
                                print("Score_P1 : {}".format(game.score_P1))
                                print("Score_P2 : {}".format(game.score_P2))
                                print("Player 2 is Win")
                                break
                        if type_play == 1 :
                                print("Bot")
                                listaction=[]
                                listaction.append("GEM")
                                list_buy_card=game.check_buy_card(player)
                                print(len(list_buy_card))
                                #game.show_field()
                                if(len(list_buy_card)>0):
                                        listaction.append("BUY")
                                else:
                                        listaction.append("GEM")
                                print(listaction)
                                action=random.choices(population=listaction,weights=[0.2,0.8])
                                if(action[0]=="BUY"):
                                        id_buy=random.choice(list_buy_card)
                                        game.action_buy(player,id_buy)
                                        if not(np.array_equal(game.old_open_used, game.open_used)):
                                                if player==1:
                                                        updateQ(game.old_open_used, id_buy, game.open_used, game.score_P1)
                                                elif player==2:
                                                        updateQ(game.old_open_used, id_buy, game.open_used, game.score_P1)
                                        #sp.show_field()
                                else:
                                        game.action_gem(player,"random")
                                #print("Player {} Action {} ".format(str(player),action[0]))
                                Round+=1
                                #time.sleep(5)
                                #clear_output(wait=True)
                                #print("Round : {} Player : {} || ".format(math.ceil(Round/2),player))
                                #print("Player {} Last Action {} ".format(str(player),action[0]))
                                #sp.show_field()
                                time.sleep(1)
        fo = open("qtablespen5000.json", "w")
        json.dump(q, fo)
        fo.close()
        return q
random_play()