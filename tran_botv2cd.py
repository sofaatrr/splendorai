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
import pandas as pd
clear = lambda: os.system('cls')
type_play=1

def random_play():
        q = defaultdict(lambda: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        sheet_history = pd.read_excel('histrory.xlsx',sheet_name='Sheet1',index_col=[0])
        
        with open('qtable-trainv4-ep1-2000-200.json') as f:
                q_ai = json.load(f)
        q.update(q_ai)
        rewards = np.array([])
        games = [splender() for i in range(3)]
        ep=0
        #     Hyperparameters
        epsilon = 1
        epsilon_min = 0.05
        epsilon_decay = 0.999  
        timesleep=0
        timelook=0
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
                                return (score-ep)+100
                        else:
                                return (score-ep)
                elif player == 2:
                        if game.score_P2+score>=10:
                                return (score-ep)+100
                        else:
                                return (score-ep)
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
                Turn_P1=1
                Turn_P2=1
                player=0
                select_gem_p1=1
                select_gem_p2=1
                needid_buy_p1=-1
                needid_buy_p2=-1
                
                count_buy_p1=0
                count_buy_p2=0
                #randomeps=random.uniform(0, 1)
                randomeps=1
                
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
                row_history_p1={}
                row_history_p2={}
                while(True):
                        
                        if Round%2 == 0 :
                                player = 2
                                row_history_p2['Turn']=Turn_P2
                                row_history_p2['Player']=player
                                row_history_p2['Round']=Round
                                row_history_p2['EP']=ep
                                Turn_P2+=1
                        elif Round%2 == 1 :
                                player = 1
                                row_history_p1['Turn']=Turn_P1
                                row_history_p1['Player']=player
                                row_history_p1['Round']=Round
                                row_history_p1['EP']=ep
                                Turn_P1+=1
                        
                        game.open_card_buy()
                        showpage()
                        #print(len(game.open_card))
                        
                               
                        if type_play == 1 :
                                print("Player {}".format(player))
                                listaction=[]
                                listaction.append("GEM")
                                id_buy=-1
                                if player==1:
                                        if select_gem_p1 >=10:
                                                select_gem_p1=1
                                                needid_buy_p1=-1
                                        list_buy_card=game.check_buy_card(player)
                                        card_open_ck=check_opencard(game.open_card)
                                        #print(new_q(q[str(game.card_p1)], card_open_ck))
                                        if (randomeps > epsilon):
                                                row_history_p1['Type']="Q-Table"
                                                #print(card_open_ck)
                                                id_buy = np.argmax(new_q(q[str(game.card_p1)], card_open_ck))
                                                
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
                                                        if(len(list_buy_card)>0):
                                                                if id_buy in list_buy_card:
                                                                        listaction.append("BUY")
                                                                        print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                                        needid_buy_p1=-1
                                                                else:
                                                                        listaction.append("GEM")
                                                                        needid_buy_p1=id_buy
                                                                        print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                        else:
                                                                list_select_card=check_select_card(player)
                                                                id_buy=random.choice(list_select_card)
                                                                if id_buy in list_buy_card:
                                                                        print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                                        listaction.append("BUY")
                                                                        needid_buy_p1=-1
                                                                else:
                                                                        needid_buy_p1=id_buy
                                                                        print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                                        listaction.append("GEM")

                                        else:
                                                row_history_p1['Type']="Random"
                                                card_open_ck=check_opencard(game.open_card)
                                                if needid_buy_p1>=0 and needid_buy_p1 in card_open_ck:
                                                        if needid_buy_p1 in list_buy_card:
                                                                listaction.append("BUY")
                                                                id_buy=needid_buy_p1 
                                                                print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                                needid_buy_p1=-1
                                                        else:
                                                                id_buy=needid_buy_p1
                                                                print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                                listaction.append("GEM")
                                                else:
                                                        list_select_card=check_select_card(player)
                                                        id_buy=random.choice(list_select_card)
                                                        if id_buy in list_buy_card:
                                                                print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                                listaction.append("BUY")
                                                                needid_buy_p1=-1
                                                        else:
                                                                needid_buy_p1=id_buy
                                                                print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                                listaction.append("GEM")
                                elif player==2:
                                        if select_gem_p2 >=10:
                                                select_gem_p2=1
                                                needid_buy_p2=-1
                                        list_buy_card=game.check_buy_card(player)
                                        row_history_p2['Type']="Random"
                                        card_open_ck=check_opencard(game.open_card)
                                        #print(card_open_ck)
                                        #print(id_buy)
                                        #print(needid_buy_p2)
                                        if needid_buy_p2>=0 and needid_buy_p2 in card_open_ck:
                                                        if needid_buy_p2 in list_buy_card:
                                                                listaction.append("BUY")
                                                                id_buy=needid_buy_p2
                                                                print("Need BUY {}".format(game.card[id_buy]["namecard"])) 
                                                                needid_buy_p2=-1
                                                        else:
                                                                id_buy=needid_buy_p2
                                                                print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                                listaction.append("GEM")
                                        else:
                                                list_select_card=check_select_card(player)
                                                id_buy=random.choice(list_select_card)
                                                if id_buy in list_buy_card:
                                                        print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                        listaction.append("BUY")
                                                        needid_buy_p1=-1
                                                else:
                                                        needid_buy_p2=id_buy
                                                        print("Need BUY {}".format(game.card[id_buy]["namecard"]))
                                                        listaction.append("GEM")
                                                
                                        #print(id_buy)
                                        #print(needid_buy_p2)
                                                
                                #print(listaction)
                                #action=random.choices(population=listaction,weights=[0.001,0.999])
                                #print(listaction)
                                action=[listaction[len(listaction)-1]]
                                #print(action)              
                                if(action[0]=="BUY"):
                                        print("BUY")
                                        game.action_buy(player,id_buy)
                                        
                                        if player==1:
                                                count_buy_p1+=1
                                                row_history_p1['Card '+str(count_buy_p1)]=game.card[id_buy]["namecard"]
                                                row_history_p1['Score']=game.score_P1
                                                if not(np.array_equal(game.old_card_P1, game.card_p1)):
                                                        updateQ(game.old_card_P1, id_buy, game.card_p1, check_reward(id_buy,player,select_gem_p1))
                                                select_gem_p1=1
                                        elif player==2:
                                                count_buy_p2+=1
                                                row_history_p2['Card '+str(count_buy_p2)]=game.card[id_buy]["namecard"]
                                                row_history_p2['Score']=game.score_P2
                                                if not(np.array_equal(game.old_card_P2, game.card_p2)):
                                                        updateQ(game.old_card_P2, id_buy, game.card_p2, check_reward(id_buy,player,select_gem_p2))
                                                select_gem_p2=1 
                                else:
                                        print("GEM")
                                        print("ID BUY {}".format(id_buy))
                                        game.action_gem(player,id_buy,"bot")
                                        if player ==1:
                                                select_gem_p1+=1
                                                if (randomeps > epsilon):
                                                        time.sleep(timelook)
                                        elif player==2:
                                                select_gem_p2+=1
                                
                                
                                time.sleep(timesleep)
                                if(game.score_P1>=10):
                                        row_history_p1['Win']=1
                                elif game.score_P2>=10:
                                        row_history_p2['Win']=1
                                if player==1:
                                        df_dictionary = pd.DataFrame([row_history_p1])
                                        sheet_history = pd.concat([sheet_history, df_dictionary], ignore_index=True)
                                        row_history_p1.clear()
                                else:
                                        df_dictionary = pd.DataFrame([row_history_p2])
                                        sheet_history = pd.concat([sheet_history, df_dictionary], ignore_index=True)
                                        #sheet_history = sheet_history.append(row_history_p2, ignore_index=True)
                                        row_history_p2.clear()
                                showpage()
                                if(game.score_P1>=10 and Round%2 == 0 and (game.score_P1>=game.score_P2 or np.sum(game.card_p1)>np.sum(game.card_p2))):
                                
                                        clear()
                                        clear_output(wait=True)
                                        print("Round : {}".format(math.ceil(Round/2)))
                                        print("Score_P1 : {}".format(game.score_P1))
                                        print("Score_P2 : {}".format(game.score_P2))
                                        print("Player 1 is Win")
                                        winp1+=1
                                        time.sleep(timesleep)
                                        break
                                elif (game.score_P2>=10 and Round%2 == 0 and (game.score_P2>game.score_P1 or np.sum(game.card_p2)>np.sum(game.card_p1))):
                                
                                        clear()
                                        clear_output(wait=True)
                                        print("Round : {}".format(math.ceil(Round/2)))
                                        print("Score_P1 : {}".format(game.score_P1))
                                        print("Score_P2 : {}".format(game.score_P2))
                                        print("Player 2 is Win")
                                        winp2+=1
                                        time.sleep(timesleep)
                                        break
                                elif (game.score_P1>=10 and game.score_P2>=10 and Round%2 == 0 and game.score_P2 == game.score_P1 and np.sum(game.card_p2)==np.sum(game.card_p1)):
                                        clear()
                                        clear_output(wait=True)
                                        print("Round : {}".format(math.ceil(Round/2)))
                                        print("Score_P1 : {}".format(game.score_P1))
                                        print("Score_P2 : {}".format(game.score_P2))
                                        print("Player 1 = Player 2")
                                        time.sleep(timesleep)
                                        break
                                elif len(check_opencard(game.open_card))<=0:
                                        clear()
                                        clear_output(wait=True)
                                        print("Round : {}".format(math.ceil(Round/2)))
                                        print("Score_P1 : {}".format(game.score_P1))
                                        print("Score_P2 : {}".format(game.score_P2))
                                        print("Player 1 = Player 2")
                                        time.sleep(timesleep)
                                        break
                                elif Round>100:
                                        print("Round : {}".format(math.ceil(Round/2)))
                                        print("Score_P1 : {}".format(game.score_P1))
                                        print("Score_P2 : {}".format(game.score_P2))
                                        print("Player 1 = Player 2")
                                        break
                                Round+=1
                if (epsilon > epsilon_min):
                        epsilon *= epsilon_decay
                if ep%200 == 0 :
                        namef="qtable-trainv4-ep1-2000-"+str(ep)+".json"
                        fo = open(namef, "w")
                        json.dump(q, fo)
                        fo.close()
        sheet_history.to_excel('histrory.xlsx')
        return q
random_play()