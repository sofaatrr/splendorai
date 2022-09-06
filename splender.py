import numpy as np
import random
from collections import defaultdict
import time
import json
import csv
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
class splender :
    def __init__(self):
        def csv_to_dict(filename):
            result_list=[]
            with open(filename) as file_obj:
                reader = csv.DictReader(file_obj)
                for row in reader:
                    result_list.append(dict(row))
            return result_list
        self.gem=[4,4,4] #red,blue,green
        self.card = csv_to_dict('card.csv')
        self.old_open_used = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.old_card_P1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.old_card_P2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.open_used = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.open_card = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.card_p1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.card_p2 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.score_tran_P1 = 0
        self.score_tran_P2 = 0
        self.score_P1 = 0
        self.score_P2 = 0
        self.gem_P1=[0,0,0]
        self.gem_P2=[0,0,0]
        self.gem_bonus_P1=[0,0,0] #red,blue,green
        self.gem_bonus_P2=[0,0,0] #red,blue,green
    
    def show_field(self):
        def check_free(red,blue,green):
            if red == "1":
                return "RED"
            elif blue =="1":
                return "BLUE"
            elif green =="1":
                return "GREEN"
            else:
                return "NULL"
        print("-----------GEM-------------")
        print("GEM RED[0] = {} BLUE[1] = {} GREEN[2] = {}".format(self.gem[0],self.gem[1],self.gem[2]))
        print("-----------CARD-------------")
        print("Level 1 : ")
        for i in range(len(self.open_card)):
            if self.open_card[i] == 1:
                if self.card[i]["level"] == "1":
                    freegem=check_free(self.card[i]["red_free"],self.card[i]["blue_free"],self.card[i]["green_free"])
                    print("ID [{}] || CARD {} || PAY red = {} blue = {} green = {} || Bonus = {}  || Score = {}".format(self.card[i]["id"],self.card[i]["namecard"],self.card[i]["red_buy"],self.card[i]["blue_buy"],self.card[i]["green_buy"],freegem,self.card[i]["score"]))
        print("------------------------------")
        print("Level 2 : ")
        for i in range(len(self.open_card)):
            if self.open_card[i] == 1:
                if self.card[i]["level"] == "2":
                    freegem=check_free(self.card[i]["red_free"],self.card[i]["blue_free"],self.card[i]["green_free"])
                    print("ID [{}] || CARD {} || PAY red = {} blue = {} green = {} || Bonus = {}  || Score = {}".format(self.card[i]["id"],self.card[i]["namecard"],self.card[i]["red_buy"],self.card[i]["blue_buy"],self.card[i]["green_buy"],freegem,self.card[i]["score"]))
        print("------------------------------")
        print("Level 3 : ")
        for i in range(len(self.open_card)):
            if self.open_card[i] == 1:
                if self.card[i]["level"] == "3":
                    freegem=check_free(self.card[i]["red_free"],self.card[i]["blue_free"],self.card[i]["green_free"])
                    print("ID [{}] || CARD {} || PAY red = {} blue = {} green = {} || Bonus = {}  || Score = {}".format(self.card[i]["id"],self.card[i]["namecard"],self.card[i]["red_buy"],self.card[i]["blue_buy"],self.card[i]["green_buy"],freegem,self.card[i]["score"]))
        
        #print("score of the 1st player : ",self.score_P1)
        #print("score of the 2st player : ",self.score_P2)
        #print("USED CARD : {}".format(self.open_used))
        #print("OPEN CARD : {}".format(self.open_card))
        print("------------- 1st player--------------")
        print("GEM:: RED = {} BLUE = {} GREEN = {}".format(str(self.gem_P1[0]),str(self.gem_P1[1]),str(self.gem_P1[2])))
        print("GEM BONUS :: RED = {} BLUE = {} GREEN = {}".format(str(self.gem_bonus_P1[0]),str(self.gem_bonus_P1[1]),str(self.gem_bonus_P1[2])))
        print("GEM ALL :: RED = {} BLUE = {} GREEN = {}".format(str(self.gem_P1[0]+self.gem_bonus_P1[0]),str(self.gem_P1[1]+self.gem_bonus_P1[1]),str(self.gem_P1[2]+self.gem_bonus_P1[2])))
        #print("CARD {}".format(self.card_p1))
        print("------------- 2st player--------------")
        print("GEM:: RED = {} BLUE = {} GREEN = {}".format(str(self.gem_P2[0]),str(self.gem_P2[1]),str(self.gem_P2[2])))
        print("GEM BONUS :: RED = {} BLUE = {} GREEN = {}".format(str(self.gem_bonus_P2[0]),str(self.gem_bonus_P2[1]),str(self.gem_bonus_P2[2])))
        print("GEM ALL :: RED = {} BLUE = {} GREEN = {}".format(str(self.gem_P2[0]+self.gem_bonus_P2[0]),str(self.gem_P2[1]+self.gem_bonus_P2[1]),str(self.gem_P2[2]+self.gem_bonus_P2[2])))
        #print("CARD {}".format(self.card_p2))
        print("-------------------------------------")
    def action_gem(self, player, choose,player_type):
        if player==2 and player_type!="bot":
            if self.gem[choose]-1>=0:
                self.gem_P2[choose]+=1
                self.gem[choose]=self.gem[choose]-1
                print("เลือก GEM {}".format(choose))
            else:
                return False
        
        def getmaxgem(idcard,player):
            def getgem_playe(player):
                gem_player=[0,0,0]
                if player==1:
                    gem_player[0]=self.gem_P1[0]+self.gem_bonus_P1[0]
                    gem_player[1]=self.gem_P1[1]+self.gem_bonus_P1[1]
                    gem_player[2]=self.gem_P1[2]+self.gem_bonus_P1[2]
                elif player==2:
                    gem_player[0]=self.gem_P2[0]+self.gem_bonus_P2[0]
                    gem_player[1]=self.gem_P2[1]+self.gem_bonus_P2[1]
                    gem_player[2]=self.gem_P2[2]+self.gem_bonus_P2[2]
                return gem_player
            gemboard=[0,0,0]
            gemweight=[0,0,0]
            gem_player=getgem_playe(player)
            #print(gem_player)
            if idcard==-1:
                pay_gem=np.array([1,1,1])
            else:
                pay_gem=np.array([int(self.card[idcard]["red_buy"]),int(self.card[idcard]["blue_buy"]),int(self.card[idcard]["green_buy"])])
                #print(pay_gem)
                pay_gem[0]=pay_gem[0]-gem_player[0]
                pay_gem[1]=pay_gem[1]-gem_player[1]
                pay_gem[2]=pay_gem[2]-gem_player[2]
                filtered = filter(lambda score: score <= 0, pay_gem)
                if len(list(filtered))==0:
                    pay_gem[pay_gem <= 0] = 1
                else:
                    pay_gem[pay_gem <= 0] = 0.1
                #print(pay_gem)
            for i in range(len(self.open_card)):
                if self.open_card[i] == 1:
                    gemboard[0]+=int(self.card[i]["red_buy"])
                    gemboard[1]+=int(self.card[i]["blue_buy"])
                    gemboard[2]+=int(self.card[i]["green_buy"])
            total = np.sum(gemboard)
            #print(gemboard)
            if idcard != "random" and idcard !=-1:
                gemboard[0]+=(pay_gem[0]*total)
                gemboard[1]+=(pay_gem[1]*total)
                gemboard[2]+=(pay_gem[2]*total)
            #print(gemboard)
            gemweight[0]=gemboard[0]/total
            gemweight[1]=gemboard[1]/total
            gemweight[2]=gemboard[2]/total
            #print("WIGHT RED {} BLUE {} GREEN {}".format(gemweight[0],gemweight[1],gemweight[2]))

            if idcard!=-1:
                pickgem=[np.argmax(gemweight)]
                #print(pickgem)
                if self.gem[pickgem[0]]-1>=0:
                    return pickgem
                else:
                    gemweight[np.argmax(gemweight)]=0
                    pickgem=[np.argmax(gemweight)]
                    #print(pickgem)
                    if self.gem[pickgem[0]]-1>=0:
                        return pickgem
                    else :
                        gemweight[np.argmax(gemweight)]=0
                        pickgem=[np.argmax(gemweight)]
                        if self.gem[pickgem[0]]-1>=0:
                            return pickgem
                        else:
                            print("RAMDOM GEM")
                            time.sleep(30)
                            return random.choices(population=[0,1,2],weights=gemweight)
                            
                        
            else:
                return random.choices(population=[0,1,2],weights=gemweight)
        def getmingem(idcard,player):
            def getgem_playe(player):
                gem_player=[0,0,0]
                if player==1:
                    gem_player[0]=self.gem_P1[0]+self.gem_bonus_P1[0]
                    gem_player[1]=self.gem_P1[1]+self.gem_bonus_P1[1]
                    gem_player[2]=self.gem_P1[2]+self.gem_bonus_P1[2]
                elif player==2:
                    gem_player[0]=self.gem_P2[0]+self.gem_bonus_P2[0]
                    gem_player[1]=self.gem_P2[1]+self.gem_bonus_P2[1]
                    gem_player[2]=self.gem_P2[2]+self.gem_bonus_P2[2]
                return gem_player
            def getgem_playe_only(player):
                gem_player=[0,0,0]
                if player==1:
                    gem_player[0]=self.gem_P1[0]
                    gem_player[1]=self.gem_P1[1]
                    gem_player[2]=self.gem_P1[2]
                elif player==2:
                    gem_player[0]=self.gem_P2[0]
                    gem_player[1]=self.gem_P2[1]
                    gem_player[2]=self.gem_P2[2]
                return gem_player
            gemboard=[0,0,0]
            gemweight=[0,0,0]
            gem_player=getgem_playe(player)
            gem_player_only=getgem_playe_only(player)
            #print(gem_player)
            if idcard==-1:
                pay_gem=np.array([1,1,1])
            else:
                pay_gem=np.array([int(self.card[idcard]["red_buy"]),int(self.card[idcard]["blue_buy"]),int(self.card[idcard]["green_buy"])])
                pay_gem[0]=pay_gem[0]-gem_player[0]
                pay_gem[1]=pay_gem[1]-gem_player[1]
                pay_gem[2]=pay_gem[2]-gem_player[2]
                
                filtered = filter(lambda score: score <= 0, pay_gem)
                
                if len(list(filtered))==0:
                    pay_gem[pay_gem <= 0] = 1
                else:
                    pay_gem[pay_gem <= 0] = 0.1
                

            for i in range(len(self.open_card)):
                if self.open_card[i] == 1:
                    gemboard[0]+=int(self.card[i]["red_buy"])
                    gemboard[1]+=int(self.card[i]["blue_buy"])
                    gemboard[2]+=int(self.card[i]["green_buy"])
            total = np.sum(gemboard)

            if idcard != "random" and idcard !=-1:
                gemboard[0]+=(pay_gem[0]*total)
                gemboard[1]+=(pay_gem[1]*total)
                gemboard[2]+=(pay_gem[2]*total)
                total = np.sum(gemboard)
            
            gemweight[0]=total-(gemboard[0]/total)
            gemweight[1]=total-(gemboard[1]/total)
            gemweight[2]=total-(gemboard[2]/total)
            #print("WIGHT RED {} BLUE {} GREEN {}".format(gemweight[0],gemweight[1],gemweight[2]))

            if idcard!=-1: #ผิดตรงนี้
                pickgem=[np.argmax(gemweight)]
                #print("L1")
                #print(pickgem)
                #print(gem_player_only[pickgem[0]])
                if gem_player_only[pickgem[0]]-1>=0:
                    #print("WIGHT RED {} BLUE {} GREEN {}".format(gemweight[0],gemweight[1],gemweight[2]))
                    return pickgem
                else:
                    gemweight[pickgem[0]]=0
                    pickgem=[np.argmax(gemweight)]
                    #print("L2")
                    #print(pickgem)
                    if gem_player_only[pickgem[0]]-1>=0:
                        
                        #print("WIGHT RED {} BLUE {} GREEN {}".format(gemweight[0],gemweight[1],gemweight[2]))
                        return pickgem
                    else:
                        gemweight[pickgem[0]]=0 
                        pickgem=[np.argmax(gemweight)]
                        #print("L3")
                        #print(pickgem)
                        #print("WIGHT RED {} BLUE {} GREEN {}".format(gemweight[0],gemweight[1],gemweight[2]))
                        return pickgem
            else:
                return random.choices(population=[0,1,2],weights=gemweight)
        def action_del(idcard,player):
            if player==1 and np.sum(self.gem_P1)>=5 and player_type=="bot":
                i=0
                while i <= 1:
                    pickgem=getmingem(idcard,player)
                    if self.gem_P1[pickgem[0]]-1>=0: 
                        self.gem_P1[pickgem[0]]=self.gem_P1[pickgem[0]]-1
                        self.gem[pickgem[0]]=self.gem[pickgem[0]]+1
                        i=i+1
                        print("DEL GEM {}".format(pickgem[0]))
                        
            elif player==2 and np.sum(self.gem_P2)>=5 and player_type=="bot":
                i=0
                while i <= 1:
                    pickgem=getmingem(idcard,player)
                    if self.gem_P2[pickgem[0]]-1>=0:
                        self.gem_P2[pickgem[0]]=self.gem_P2[pickgem[0]]-1
                        self.gem[pickgem[0]]=self.gem[pickgem[0]]+1
                        i=i+1
                        print("DEL GEM {}".format(pickgem[0]))
        
        if (np.sum(self.gem)<2) :
            print("Not enough gems")
            action_del(choose,player)
            return False
        #------------------------------------- ทิ้ง gem
        action_del(choose,player)      
        #------------------------------------- เลือก gem
        if player==1 and player_type=="bot":
            i=0
            while i <= 1:
                pickgem=getmaxgem(choose,player)
                if self.gem[pickgem[0]]-1>=0:
                    self.gem_P1[pickgem[0]]+=1
                    self.gem[pickgem[0]]-=1
                    i=i+1
                    print("PICK GEM {}".format(pickgem[0]))
                        
        elif player==2 and player_type=="bot":
            i=0
            while i <= 1:
                pickgem=getmaxgem(choose,player)
                if self.gem[pickgem[0]]-1>=0:
                    self.gem_P2[pickgem[0]]+=1
                    self.gem[pickgem[0]]-=1
                    i=i+1
                    print("PICK GEM {}".format(pickgem[0]))
                        
    def action_buy(self, player, choose):
        gem_player=[0,0,0]
        if player==1:
            gem_player[0]=self.gem_P1[0]+self.gem_bonus_P1[0]
            gem_player[1]=self.gem_P1[1]+self.gem_bonus_P1[1]
            gem_player[2]=self.gem_P1[2]+self.gem_bonus_P1[2]
        elif player==2:
            gem_player[0]=self.gem_P2[0]+self.gem_bonus_P2[0]
            gem_player[1]=self.gem_P2[1]+self.gem_bonus_P2[1]
            gem_player[2]=self.gem_P2[2]+self.gem_bonus_P2[2]
        
        if self.open_used[choose]==0 and self.open_card[choose]==1:
            pay_gem=[int(self.card[choose]["red_buy"]),int(self.card[choose]["blue_buy"]),int(self.card[choose]["green_buy"])]
            
            pay_gem[0]=pay_gem[0]-gem_player[0]
            pay_gem[1]=pay_gem[1]-gem_player[1]
            pay_gem[2]=pay_gem[2]-gem_player[2]

            if pay_gem[0]<=0 and pay_gem[1] <=0 and pay_gem[2] <=0:
                self.open_card[choose]=0
                self.old_open_used=self.open_used.copy()
                self.old_card_P1=self.card_p1.copy()
                self.old_card_P2=self.card_p2.copy()
                self.open_used[choose]=1
                if player==1:
                    self.card_p1[choose]=1
                    difgem=[0,0,0]
                    difgem[0]=self.gem_bonus_P1[0]-int(self.card[choose]["red_buy"])
                    1-2
                    if difgem[0]<0:
                        self.gem_P1[0]=self.gem_P1[0]+difgem[0]
                        self.gem[0]-=difgem[0]

                    difgem[1]=self.gem_bonus_P1[1]-int(self.card[choose]["blue_buy"])
                    if difgem[1]<0:
                        self.gem_P1[1]=self.gem_P1[1]+difgem[1]
                        self.gem[1]-=difgem[1]

                    difgem[2]=self.gem_bonus_P1[2]-int(self.card[choose]["green_buy"])
                    if difgem[2]<0:
                        self.gem_P1[2]=self.gem_P1[2]+difgem[2]
                        self.gem[2]-=difgem[2]

                    self.gem_bonus_P1[0]+=int(self.card[choose]["red_free"])
                    self.gem_bonus_P1[1]+=int(self.card[choose]["blue_free"])
                    self.gem_bonus_P1[2]+=int(self.card[choose]["green_free"])

                    self.score_P1+=int(self.card[choose]["score"])
                    print("BUY {}".format(self.card[choose]["namecard"]))
                elif player==2:
                    self.card_p2[choose]=1
                    difgem=[0,0,0]

                    difgem[0]=self.gem_bonus_P2[0]-int(self.card[choose]["red_buy"])
                    if difgem[0]<0:
                        self.gem_P2[0]=self.gem_P2[0]+difgem[0]
                        self.gem[0]-=difgem[0]

                    difgem[1]=self.gem_bonus_P2[1]-int(self.card[choose]["blue_buy"])
                    if difgem[1]<0:
                        self.gem_P2[1]=self.gem_P2[1]+difgem[1]
                        self.gem[1]-=difgem[1]

                    difgem[2]=self.gem_bonus_P2[2]-int(self.card[choose]["green_buy"])
                    if difgem[2]<0:
                        self.gem_P2[2]=self.gem_P2[2]+difgem[2]
                        self.gem[2]-=difgem[2]

                    self.gem_bonus_P2[0]+=int(self.card[choose]["red_free"])
                    self.gem_bonus_P2[1]+=int(self.card[choose]["blue_free"])
                    self.gem_bonus_P2[2]+=int(self.card[choose]["green_free"])
                    self.score_P2+=int(self.card[choose]["score"])
                    print("BUY {}".format(self.card[choose]["namecard"]))
            else:
                return False
        else:
            return False
    def open_card_buy(self):
        l1=0
        l2=0
        l3=0
        filtter_usercard_l1=[]
        filtter_usercard_l2=[]
        filtter_usercard_l3=[]
        for i in range(len(self.open_card)):
            if self.open_card[i]==1:
                if self.card[i]["level"] == "1":
                    l1+=1
                elif self.card[i]["level"] == "2":
                    l2+=1
                elif self.card[i]["level"] == "3":
                    l3+=1
            else:
                if self.card[i]["level"] == "1":
                    if self.open_used[i] ==0:
                        filtter_usercard_l1.append(i) 
                elif self.card[i]["level"] == "2":
                    if self.open_used[i] ==0:
                        filtter_usercard_l2.append(i)
                elif self.card[i]["level"] == "3":
                    if self.open_used[i] ==0:
                        filtter_usercard_l3.append(i)    
        while l1 < 4:
            if(len(filtter_usercard_l1)>0):
                x = random.choice(filtter_usercard_l1)
                self.open_card[x]=1
                l1+=1
            else:
                break
        while l2 < 4:
            if(len(filtter_usercard_l2)>0):
                x = random.choice(filtter_usercard_l2)
                self.open_card[x]=1
                l2+=1
            else:
                break
        while l3 < 4:
            if(len(filtter_usercard_l3)>0):
                x = random.choice(filtter_usercard_l3)
                self.open_card[x]=1
                l3+=1
            else:
                break
    def check_buy_card(self, player):
        list_card_buy=[]
        gem_player=[0,0,0]
        if player==1:
            gem_player[0]+=self.gem_P1[0]+self.gem_bonus_P1[0]
            gem_player[1]+=self.gem_P1[1]+self.gem_bonus_P1[1]
            gem_player[2]+=self.gem_P1[2]+self.gem_bonus_P1[2]
        elif player==2:
            gem_player[0]+=self.gem_P2[0]+self.gem_bonus_P2[0]
            gem_player[1]+=self.gem_P2[1]+self.gem_bonus_P2[1]
            gem_player[2]+=self.gem_P2[2]+self.gem_bonus_P2[2]
        for i in range(len(self.open_card)):
            if self.open_card[i] == 1:
                pay_gem=[int(self.card[i]["red_buy"]),int(self.card[i]["blue_buy"]),int(self.card[i]["green_buy"])]
                pay_gem[0]=pay_gem[0]-gem_player[0]
                pay_gem[1]=pay_gem[1]-gem_player[1]
                pay_gem[2]=pay_gem[2]-gem_player[2]
                if pay_gem[0]<=0 and pay_gem[1] <=0 and pay_gem[2] <=0:
                    list_card_buy.append(i)
        #print(list_card_buy)
        return list_card_buy