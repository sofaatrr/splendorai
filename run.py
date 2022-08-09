from IPython.display import clear_output  
import math                               
import time
import random
import app_df                          
from tqdm import tqdm
#ฟังก์ชัน play สร้างเพื่อเรียกใช้ได้ง่ายๆ
def play(type_play="PVP"):

    sp = app_df.splender()
    sp.open_card_from_deck()
    turn = 1
    Round = 1

    while True:

        if Round%2 == 0 :
            turn = 2
        elif Round%2 == 1 :
            turn = 1
        print("\nRound :",math.ceil(Round/2))

        ###################################################################################################### เช็คคะแนน

        s1, s2 = sp.check_score()
        if s1 >= 10 :
            print("Player 1 is Win")
            break
        elif s2 >= 10 :
            print("Player 2 is Win")
            break

        ###################################################################################################### แจ้งตัวเลือก

        print("\nPlayer",turn)
        print("1 :\tหากต้องการเลือกเหรียญ")
        print("2 :\tหากต้องการซื้อการ์ด")
        # print("3 :\tสุ่มเหรียญ 2 เหรียญที่แตกต่าง")
        # print("4 :\tสุ่มเหรียญ 2 เหรียญที่เหมือนกัน")
        # print("5 :\tสุ่มซื้อ 1 การ์ด")

        ###################################################################################################### รับ Input

        while True :

            if type_play == "PVP" :
                ac = input("เลือกดำเนินการ (1/2) :\t")
              
            elif type_play == "bot" :
                ####################################################################### จุดแตกต่างจาก play ธรรมดา
                if turn == 1 :
                    ac = input("เลือกดำเนินการ (1/2) :\t") 
                elif turn == 2 :
                    for i in tqdm(range(3)) : #Fake thinking
                        time.sleep(1)
                    ac = random.choice(["3", "4", "5"])
                #######################################################################
            if ac in ["1" , "2", "3", "4", "5"] :
                break
            else :
                print("กรอกใหม่อีกครั้ง")

        ###################################################################################################### ดำเนินการตาม Input

        ####################################################################### กรณีเลือกดำเนินการเอง
        
        if ac == '1' :
            while True :
                color_1 = input("ระบุสีที่ 1 :\t")
                if color_1 in ["red", "green", "blue"] :
                    ac = [color_1]
                    break
                else :
                    print("กรอกใหม่อีกครั้ง")
            while True :
                color_2 = input("ระบุสีที่ 2 :\t")
                if color_2 in ["red", "green", "blue"] :
                    ac += [color_2]
                    break
                else :
                    print("กรอกใหม่อีกครั้ง")
            if ac[0] != ac[1] :
                if sp.action_1(turn, ac) == False :
                    continue
            elif ac[0] == ac[1] :
                if sp.action_2(turn, ac) == False :
                    continue
        elif ac == '2' :
            while True :
                input_level = input("ระบุ level :\t")
                if input_level in ["1", "2", "3", "4"] :
                    ac = [input_level]
                    break
                else :
                    print("กรอกใหม่อีกครั้ง")
            while True :
                input_card = input("ระบุลำดับ card :\t")
                if input_card in ["1", "2", "3", "4"] :
                    ac += [input_card]
                    break
                else :
                    print("กรอกใหม่อีกครั้ง")
            if sp.action_3(turn, level = ac[0], card = ac[1]) == False :
                continue

        ####################################################################### กรณีสุ่ม สำหรับ Bot

        if ac == '3' :
            if sp.action_1(turn, "random") == False :
                continue
        elif ac == '4' :
            if sp.action_2(turn, "random") == False :
                continue
        elif ac == '5' :
            if sp.action_3(turn, "random") == False :
                continue

        ######################################################################################################

        clear_output(wait=True)
        sp.show_field()

        Round += 1
play(type_play = "PVP")