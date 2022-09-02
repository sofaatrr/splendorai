
import random                             
  
class splender :

    def __init__(self): #กำหนดสิ่งต่างๆในสถานะเริ่มต้น

        self.gem = ["blue", "blue", "blue", "blue",
                    "green", "green", "green", "green",
                    "red", "red", "red", "red"]

        #["ทรัพยากรบนการ์ด, [ทรัพยากรที่ใช้แลก], คะแนน]
        self.card_lv_1 = {
            1 : ["red", ["green", "blue"], 0],
            2 : ["red", ["green", "green", "blue"], 0],
            3 : ["red", ["green", "green"], 1],
            4 : ["red", ["green", "blue", "blue", "blue"], 0],
            5 : ["green", ["red", "blue"], 0],
            6 : ["green", ["red", "blue", "blue"], 0],
            7 : ["green", ["blue", "blue"], 1],
            8 : ["green", ["red", "red", "red", "blue"], 0],
            9 : ["blue", ["red", "green"], 0],
            10 : ["blue", ["red", "red", "green"], 0],
            11 : ["blue", ["red", "red"], 1],
            12 : ["blue", ["red", "green", "green", "green"], 0]
        }

        self.card_lv_2 = {
            1 : ["red", ["green", "green", "blue", "blue", "blue"], 1],
            2 : ["red", ["green", "green", "green"], 2],
            3 : ["red", ["green", "green", "green", "green"], 3],
            4 : ["green", ["red", "red", "red", "blue", "blue"], 1],
            5 : ["green", ["blue", "blue", "blue"], 2],
            6 : ["green", ["blue", "blue", "blue", "blue"], 3],
            7 : ["blue", ["red", "red", "green", "green", "green"], 1],
            8 : ["blue", ["red", "red", "red"], 2],
            9 : ["blue", ["red", "red", "red", "red"], 3]
        }

        self.card_lv_3 = {
            1 : ["red", ["green", "green", "green", "blue", "blue", "blue", "blue", "blue"], 3],
            2 : ["red", ["green", "green", "green", "green", "green"], 4],
            3 : ["green", ["red", "red", "red", "red", "red", "blue", "blue", "blue"], 3],
            4 : ["green", ["blue", "blue", "blue", "blue", "blue"], 4],
            5 : ["blue", ["red", "red", "red", "green", "green", "green", "green", "green"], 3],
            6 : ["blue", ["red", "red", "red", "red", "red"], 4]
        }

        self.open_card_lv_1 = []
        self.open_card_lv_2 = []
        self.open_card_lv_3 = []

        self.card_lv_1_P1 = []
        self.card_lv_2_P1 = []
        self.card_lv_3_P1 = []
        self.gem_P1 = []
        self.gem_bonus_P1 = []
        self.score_P1 = 0

        self.card_lv_1_P2 = []
        self.card_lv_2_P2 = []
        self.card_lv_3_P2 = []
        self.gem_P2 = []
        self.gem_bonus_P2 = []
        self.score_P2 = 0

    def show_field(self): #เอาไว้แสดงผลทั้งหมดบนสนาม

        ####################################################################### gem บนสนามที่เหลืออยู่

        print("\nthe remaining gems : ",self.gem)

        ####################################################################### card บนสนาม

        print("\nCards on the field")
        print("Level 1 : ")
        for i in range(len(self.open_card_lv_1)):
            print("\t", self.card_lv_1[self.open_card_lv_1[i]])
        print("Level 2 : ")
        for i in range(len(self.open_card_lv_2)):
            print("\t", self.card_lv_2[self.open_card_lv_2[i]])
        print("Level 3 : ")
        for i in range(len(self.open_card_lv_3)):
            print("\t", self.card_lv_3[self.open_card_lv_3[i]])

        print("\n","-"*50)

        ####################################################################### สิ่งที่ Player 1 มี

        print("\nCard in Player 1's hand")
        print("Level 1 : ")
        for i in range(len(self.card_lv_1_P1)):
            print("\t", self.card_lv_1[self.card_lv_1_P1[i]])
        print("Level 2 : ")
        for i in range(len(self.card_lv_2_P1)):
            print("\t", self.card_lv_2[self.card_lv_2_P1[i]])
        print("Level 3 : ")
        for i in range(len(self.card_lv_3_P1)):
            print("\t", self.card_lv_3[self.card_lv_3_P1[i]])
        sum_gem = self.gem_P1 + self.gem_bonus_P1
        print("1st player's Gem : ",self.gem_P1,"\tGem Bonus : ",self.gem_bonus_P1)
        print("( red : ",sum_gem.count("red"),"\tgreen : ",sum_gem.count("green"),"\tblue : ",sum_gem.count("blue"),")")
        print("score of the 1st player : ",self.score_P1)

        print("\n","-"*50)

        ####################################################################### สิ่งที่ Player 2 มี

        print("\nCard in Player 2's hand")
        print("Level 1 : ")
        for i in range(len(self.card_lv_1_P2)):
            print("\t", self.card_lv_1[self.card_lv_1_P2[i]])
        print("Level 2 : ")
        for i in range(len(self.card_lv_2_P2)):
            print("\t", self.card_lv_2[self.card_lv_2_P2[i]])
        print("Level 3 : ")
        for i in range(len(self.card_lv_3_P2)):
            print("\t", self.card_lv_3[self.card_lv_3_P2[i]])
        sum_gem = self.gem_P2 + self.gem_bonus_P2
        print("2nd Player's Gem : ",self.gem_P2,"\tGem Bonus : ",self.gem_bonus_P2)
        print("( red : ",sum_gem.count("red"),"\tgreen : ",sum_gem.count("green"),"\tblue : ",sum_gem.count("blue"),")")
        print("score of the 2nd player : ",self.score_P2)

        print("\n","-"*50)

    def action_1(self, player, choose): #การดำเนินการโดยเลือกเหรียญ 2 เหรียญที่มีสีต่างกัน

        if (self.gem.count("red") == 0 and self.gem.count("green") == 0) or (self.gem.count("red") == 0 and self.gem.count("blue") == 0) or (self.gem.count("green") == 0 and self.gem.count("blue") == 0) :
            print("Not enough gems")
            return False

        if choose == "random" :
            # สุ่ม 3 gem ที่ต่างกัน
            gem_choose = []
            while True :
                gem_random = self.gem[random.randint(0, len(self.gem)-1)]
                if gem_random not in gem_choose :
                    gem_choose += [gem_random]
                    self.gem.remove(gem_random)
                if len(gem_choose) == 2 :
                    break
        else :
            gem_choose = choose
            self.gem.remove(choose[0])
            self.gem.remove(choose[1])

        if player == 1 :
            self.gem_P1 += gem_choose
            print("Player 1 choose : ",gem_choose)
        elif player == 2 :
            self.gem_P2 += gem_choose
            print("Player 2 choose : ",gem_choose)
        self.show_field()

    def action_2(self, player ,choose): #การดำเนินการโดยเลือกเหรียญ 2 เหรียญที่มีสีเหมือนกัน

        if (self.gem.count("red") < 2 and self.gem.count("green") < 2 and self.gem.count("blue") < 2) or (choose != "random" and self.gem.count(choose[0]) < 2) :
            print("Not enough gems")
            return False

        if choose == "random" :
            # สุ่ม 2 gem ที่สีเหมือนกัน
            fail = 0
            while True :
                gem_random = self.gem[random.randint(0, len(self.gem)-1)]
                if self.gem.count(gem_random) > 1 :
                    gem_choose = [gem_random, gem_random]
                    self.gem.remove(gem_random)
                    self.gem.remove(gem_random)
                    break
                else :
                  fail += 1
                if fail == 10 :
                    return False
        else :
            gem_choose = choose
            self.gem.remove(choose[0])
            self.gem.remove(choose[1])

        if player == 1 :
            self.gem_P1 += gem_choose
            print("Player 1 choose : ",gem_choose)
        elif player == 2 :
            self.gem_P2 += gem_choose
            print("Player 2 choose : ",gem_choose)
        self.show_field()

    def action_3(self, player, choose = "manual", level = False, card = False): #การดำเนินการโดยเลือกซื้อการ์ด 1 ใบ (สามารถลดรูปโค้ดได้ แต่ยุ่งยากนิดหน่อยเลยปล่อยไว้แบบนี้)
        if player == 1 :
            gem = self.gem_P1 + self.gem_bonus_P1
        else :
            gem = self.gem_P2 + self.gem_bonus_P2


        fail = 0
        while True :
            if choose == "random" :
                random_level = random.randint(1, 3)
                if random_level == 1 :
                    random_card = random.choice(self.open_card_lv_1)
                elif random_level == 2 :
                    random_card = random.choice(self.open_card_lv_2)
                elif random_level == 3 :
                    random_card = random.choice(self.open_card_lv_3)
            elif choose == "manual" :
                random_level = int(level)
                card = int(card)
                if random_level == 1 :
                    random_card = self.open_card_lv_1[card-1]
                elif random_level == 2 :
                    random_card = self.open_card_lv_2[card-1]
                elif random_level == 3 :
                    random_card = self.open_card_lv_3[card-1]

            if random_level == 1 :
                if self.card_lv_1[random_card][1].count("red") <= gem.count("red") and self.card_lv_1[random_card][1].count("green") <= gem.count("green") and self.card_lv_1[random_card][1].count("blue") <= gem.count("blue") :
                    cost = self.card_lv_1[random_card][1][:]
                    if player == 1 :
                        self.card_lv_1_P1 += [random_card]
                        #ใช้ bonus ลด cost
                        for i in range(len(self.gem_bonus_P1)):
                            try :
                                cost.remove(self.gem_bonus_P1[i])
                            except :
                                True
                        for i in range(len(cost)):
                            self.gem_P1.remove(cost[i])
                            self.gem += [cost[i]]
                        self.gem_bonus_P1 += [self.card_lv_1[random_card][0]]
                        self.score_P1 += self.card_lv_1[random_card][2]
                    else :
                        self.card_lv_1_P2 += [random_card]
                        #ใช้ bonus ลด cost
                        for i in range(len(self.gem_bonus_P2)):
                            try :
                                cost.remove(self.gem_bonus_P2[i])
                            except :
                                True
                        for i in range(len(cost)):
                            self.gem_P2.remove(cost[i])
                            self.gem += [cost[i]]
                        self.gem_bonus_P2 += [self.card_lv_1[random_card][0]]
                        self.score_P2 += self.card_lv_1[random_card][2]
                    self.open_card_lv_1.remove(random_card)
                    self.open_card_from_deck()
                    break
            elif random_level == 2 :
                random_card = random.choice(self.open_card_lv_2)
                if self.card_lv_2[random_card][1].count("red") <= gem.count("red") and self.card_lv_2[random_card][1].count("green") <= gem.count("green") and self.card_lv_2[random_card][1].count("blue") <= gem.count("blue") :
                    cost = self.card_lv_2[random_card][1][:]
                    if player == 1 :
                        self.card_lv_2_P1 += [random_card]
                        #ใช้ bonus ลด cost
                        for i in range(len(self.gem_bonus_P1)):
                            try :
                                cost.remove(self.gem_bonus_P1[i])
                            except :
                                True
                        for i in range(len(cost)):
                            self.gem_P1.remove(cost[i])
                            self.gem += [cost[i]]
                        self.gem_bonus_P1 += [self.card_lv_2[random_card][0]]
                        self.score_P1 += self.card_lv_2[random_card][2]
                    else :
                        self.card_lv_2_P2 += [random_card]
                        #ใช้ bonus ลด cost
                        for i in range(len(self.gem_bonus_P2)):
                            try :
                                cost.remove(self.gem_bonus_P2[i])
                            except :
                                True
                        for i in range(len(cost)):
                            self.gem_P2.remove(cost[i])
                            self.gem += [cost[i]]
                        self.gem_bonus_P2 += [self.card_lv_2[random_card][0]]
                        self.score_P2 += self.card_lv_2[random_card][2]
                    self.open_card_lv_2.remove(random_card)
                    self.open_card_from_deck()
                    break
            elif random_level == 3 :
                random_card = random.choice(self.open_card_lv_3)
                if self.card_lv_3[random_card][1].count("red") <= gem.count("red") and self.card_lv_3[random_card][1].count("green") <= gem.count("green") and self.card_lv_3[random_card][1].count("blue") <= gem.count("blue") :
                    cost = self.card_lv_3[random_card][1][:]
                    if player == 1 :
                        self.card_lv_3_P1 += [random_card]
                        #ใช้ bonus ลด cost
                        for i in range(len(self.gem_bonus_P1)):
                            try :
                                cost.remove(self.gem_bonus_P1[i])
                            except :
                                True
                        for i in range(len(cost)):
                            self.gem_P1.remove(cost[i])
                            self.gem += [cost[i]]
                        self.gem_bonus_P1 += [self.card_lv_3[random_card][0]]
                        self.score_P1 += self.card_lv_3[random_card][2]
                    else :
                        self.card_lv_3_P2 += [random_card]
                        #ใช้ bonus ลด cost
                        for i in range(len(self.gem_bonus_P1)):
                            try :
                                cost.remove(self.gem_bonus_P1[i])
                            except :
                                True
                        for i in range(len(cost)):
                            self.gem_P2.remove(cost[i])
                            self.gem += [cost[i]]
                        self.gem_bonus_P2 += [self.card_lv_3[random_card][0]]
                        self.score_P2 += self.card_lv_3[random_card][2]
                    self.open_card_lv_3.remove(random_card)
                    self.open_card_from_deck()
                    break
  
            fail += 1
            if fail == 300 :
                print("cannot buy")
                return(False)


    def open_card_from_deck(self): #เอาไว้เปิดการ์ดลงกระดานให้ครบ 4 ใบ
        while True :
            if len(self.open_card_lv_1) == 4 or (len(self.open_card_lv_1) + len(self.card_lv_1_P1) + len(self.card_lv_1_P2) == len(self.card_lv_1)) :
                break
            random_card = random.randint(1, len(self.card_lv_1))
            if random_card not in self.open_card_lv_1 and random_card not in self.card_lv_1_P1 and random_card not in self.card_lv_1_P2 :
                self.open_card_lv_1 += [random_card]

        while True :
            if len(self.open_card_lv_2) == 4 or (len(self.open_card_lv_2) + len(self.card_lv_2_P1) + len(self.card_lv_2_P2) == len(self.card_lv_2)) :
                break
            random_card = random.randint(1, len(self.card_lv_2))
            if random_card not in self.open_card_lv_2 and random_card not in self.card_lv_2_P1 and random_card not in self.card_lv_2_P2 :
                self.open_card_lv_2 += [random_card]

        while True :
            if len(self.open_card_lv_3) == 4 or (len(self.open_card_lv_3) + len(self.card_lv_3_P1) + len(self.card_lv_3_P2) == len(self.card_lv_3)) :
                break
            random_card = random.randint(1, len(self.card_lv_3))
            if random_card not in self.open_card_lv_3 and random_card not in self.card_lv_3_P1 and random_card not in self.card_lv_3_P2 :
                self.open_card_lv_3 += [random_card]

        self.show_field()

    def check_score(self): #เอาไว้ส่งค่าคะแนนไปเช็ค
        return self.score_P1, self.score_P2