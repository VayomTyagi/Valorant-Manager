import cv2
import numpy as np
import pyautogui as pg
import time
i=0
while i<1:
    print("Valorant ID Manager")
    print(">> 1. VIEW")
    print(">> 2. ADD")
    print(">> 3. LOGIN")
    print(">> 4. AGENT LOCK")
    print(">> 5. CRF")
    print(">> 6. EXIT")
    a=int(input(""))
    if a==1:
        ID = open('id.txt','r')
        USE = open('Username.txt','r')
        PASS = open('pass.txt','r')
        with open(r'id.txt', 'r') as fp:
            noline = len(fp.readlines())
            print(noline)
        fp.close()
        for j in range(noline):
            temp1=ID.readline()
            temp2=USE.readline()
            temp3=PASS.readline()
            print("S.no ->",j+1,'\n',"ID ->",temp1,"Username = ",temp2,"PASS = ",temp3,)
        ID.close()
        USE.close()
        PASS.close()
        print("\n")
    elif a==2:
        ID = 'id.txt'
        USE = 'Username.txt'
        PASS = 'pass.txt'
        with open(ID, 'a+', encoding='utf-8') as ID:
            ID.write(input('Enter in game name --> ') + '\n')
        ID.close()
        with open(USE, 'a+', encoding='utf-8') as USE:
            USE.write(input('Enter Username --> ') + '\n')
        USE.close()
        with open(PASS, 'a+', encoding='utf-8') as PASS:
            PASS.write(input('Enter Pass --> ') + '\n')
        PASS.close()
        print("ID added successful")
        print("\n")
    elif a==3:
        ID = open('id.txt','r')
        USE = open('Username.txt','r')
        PASS = open('pass.txt','r')
        with open(r'id.txt', 'r') as fp:
            noline = len(fp.readlines())
        print(noline)
        fp.close()
        for k in range(noline):
            temp1=ID.readline()
            temp2=USE.readline()
            temp3=PASS.readline()
            print("S.no ->",k+1,'\n',"ID ->",temp1,"Username = ",temp2,"PASS = ",temp3,)
        ID.close()
        USE.close()
        PASS.close()
        ID = open('id.txt','r')
        USE = open('Username.txt','r')
        PASS = open('pass.txt','r')
        idn=int(input("Enter the s.no of id "))
        l=1
        while l<=idn:
            x=USE.readline()
            y=PASS.readline()
            l=l+1
        time.sleep(1)
        pg.press("win")
        time.sleep(1)
        pg.write("valorant")
        pg.press("enter")
        UN_image = cv2.imread('ima/un.png', cv2.IMREAD_COLOR)
        PW_image = cv2.imread('ima/pw.png', cv2.IMREAD_COLOR)

        while True:
            screen_pil = pg.screenshot()
            screen_np = np.array(screen_pil)
            screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

            result = cv2.matchTemplate(screen, UN_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            result2 = cv2.matchTemplate(screen, PW_image, cv2.TM_CCOEFF_NORMED)
            min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)

            threshold = 0.8
            if max_val >= threshold:
                un_x, un_y = max_loc
                pw_x,pw_y=max_loc2

                #print("Template found at:", match_x, match_y)
                pg.moveTo(un_x+41,un_y+32,0.00000000000001)
                pg.click(button='left')
                pg.write(x)
                pg.moveTo(pw_x+41,pw_y+32,0.00000000000001)
                pg.click(button='left')
                pg.write(y)
                pg.press("enter")
                break
        cv2.destroyAllWindows()
    elif a==4:
        print ("1 . Astra")
        print ("2 . Breach")
        print ("3 . Brimstone")
        print ("4 . Chamber")
        print ("5 . Cypher")
        print ("6 . Deadlock")
        print ("7 . Fade")
        print ("8 . Gekko")
        print ("9 . Harber")
        print ("10 . Jett ")
        print ("11 . Kay/O")
        print ("12 . Killjoy")
        print ("13 . Neon")
        print ("14 . Omen")
        print ("15 . Phoenix")
        print ("16 . Raze")
        print ("17 . Reyna")
        print ("18 . Sage")
        print ("19 . Skye ")
        print ("20 . Sova")
        print ("21 . Viper")
        print ("22 . Yoru")
        agn=int(input("Enter the number of agent --> "))
        if (agn == 1):
            #astra
            template_image = cv2.imread('ima/astra.png', cv2.IMREAD_COLOR)
        elif (agn == 2):
            #breach
            template_image = cv2.imread('ima/breach.png', cv2.IMREAD_COLOR)
        elif (agn == 3):
            #brimstone
            template_image = cv2.imread('ima/brimstone.png', cv2.IMREAD_COLOR)
        elif (agn == 4):
            #chamber
            template_image = cv2.imread('ima/chamber.png', cv2.IMREAD_COLOR)
        elif (agn == 5):
            #cypher
            template_image = cv2.imread('ima/cypher.png', cv2.IMREAD_COLOR)
        elif (agn == 6):
            #deadlock
            template_image = cv2.imread('ima/deadlock.png', cv2.IMREAD_COLOR)
        elif (agn == 7):
            #fade
            template_image = cv2.imread('ima/fade.png', cv2.IMREAD_COLOR)
        elif (agn == 8):
            #Gekko
            template_image = cv2.imread('ima/gekko.png', cv2.IMREAD_COLOR)
        elif (agn == 9):
            #harber
            template_image = cv2.imread('ima/harber.png', cv2.IMREAD_COLOR)
        elif (agn == 10):
            #Jett
            template_image = cv2.imread('ima/jett.png', cv2.IMREAD_COLOR)
        elif (agn == 11):
            #Kay/O
            template_image = cv2.imread('ima/kayo.png', cv2.IMREAD_COLOR)
        elif (agn == 12):
            #Killjoy
            template_image = cv2.imread('ima/killjoy.png', cv2.IMREAD_COLOR)
        elif (agn == 13):
            #neon
            template_image = cv2.imread('ima/neon.png', cv2.IMREAD_COLOR)
        elif (agn == 14):
            #omen
            template_image = cv2.imread('ima/omen.png', cv2.IMREAD_COLOR)
        elif (agn == 15):
            #phoenix
            template_image = cv2.imread('ima/phoenix.png', cv2.IMREAD_COLOR)
        elif (agn == 16):
            #raze
            template_image = cv2.imread('ima/raze.png', cv2.IMREAD_COLOR)
        elif (agn == 17):
            #reyna
            template_image = cv2.imread('ima/reyna.png', cv2.IMREAD_COLOR)
        elif (agn == 18):
            #Sage
            template_image = cv2.imread('ima/sage.png', cv2.IMREAD_COLOR)
        elif (agn == 19):
            #Skye
            template_image = cv2.imread('ima/skye.png', cv2.IMREAD_COLOR)
        elif (agn == 20):
            #Sova
            template_image = cv2.imread('ima/sova.png', cv2.IMREAD_COLOR)
        elif (agn == 21):
            #Viper
            template_image = cv2.imread('ima/viper.png', cv2.IMREAD_COLOR)
        elif (agn == 22):
            #Yoru
            template_image = cv2.imread('ima/yoru.png', cv2.IMREAD_COLOR)
        else :
            print("Invalid Input")
        while True:
            screen_pil = pg.screenshot()
            screen_np = np.array(screen_pil)
            screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

            result = cv2.matchTemplate(screen, template_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            threshold = 0.8
            if max_val >= threshold:
                match_x, match_y = max_loc
                #print("Template found at:", match_x, match_y)
                pg.moveTo(match_x+41,match_y+32,0.00000000000001)
                pg.click(button='left')
                pg.moveTo(955,806,0.00000000000001)
                pg.click(button='left')
                break
        cv2.destroyAllWindows()
    elif (a==5):
        pg.FAILSAFE = False
        try :
            print ("Press CTRL+C to close the script")
            while True:
                # for purple "if pyautogui.pixelMatchesColor(960, 540, (255, 0, 255),tolerance=90):"
                # for red "if pyautogui.pixelMatchesColor(960, 540, (255, 0, 0),tolerance=90):"
                    if pg.pixelMatchesColor(960, 540, (255, 0, 0),tolerance=90):
                        for i in range (2):
                            #pyautogui.click(button='left')
                            pg.press('k')
                            #time.sleep(0.1)
        except KeyboardInterrupt:
            print("Script closed")
    elif (a==6):
        break
    else :
        print("Invalid Input")