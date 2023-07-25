import random as ran
from playsound import playsound
import time
import tkinter.messagebox as ksm

win = 1000

def ran_gen(new,list_que):
    r = ran.randint(0,len(list_que)-1)

    if(r not in new):
        new.append(r)
    else:
        r = ran.randint(0,4)
        while(r in new):
            r = ran.randint(0,4)

        new.append(r)

    return r


def check(ans,que,r,list_que,win):
    ans = ans.lower()
    if(ans==que.get(list_que[r])[4]):
        print("\n\t\t\t\t\t\t\tSAHI JAWAB!!!!!")
        file5 = "D:\code\KBC\Kbc_Correct.mp3"
        playsound(file5)
        win = win * 2
        print(f"\n\t\t\t\t\t\t\tCONGRATULATION YOU WON {win}/-")      
    else:
        print("\n\t\t\t\t\t\t\tGalat Jawab!!!")
  
        file3 = "D:\code\KBC\Kbc_Galat_Jawab.mp3"
        playsound(file3)

        print("\n\t\t\t\t\t\t\tBETTER LUCK NEXT TIME!!!!")
        exit()

    return win



list_que = []
new = []


print("\n\n\t\t\t**************************WELCOME TO KON BANEGA CROREPATI**************************\n\n")
file = "D:\code\KBC\intro_kbc.mp3"
playsound(file)
name = input("\t\t\t\t\t\t\tENTER YOUR NAME: ")
email = input("\t\t\t\t\t\t\tENTER YOUR EMAIL ID: ")

if("@gmail.com" not in email):
    while("@gmail.com" not in email):
        print("\t\t\t\t\t\t\tPlease Enter a Valid Email ID!!!!")
        email = input("\t\t\t\t\t\t\tENTER YOUR EMAIL ID: ")


print("\n\n**************************************************************************************************************************************************\n")
print("\t\t\t\t\t\t\tTHOH CHALIYE SHURU KARTE HAI ")
file2 = "D:\code\KBC\intro2_kbc.mp3"
playsound(file2)
que = {
    "Which type of Programming does Python support?" : ["object-oriented programming", "structured programming", "functional programming", "all of the mentioned","a"],
    "Is Python case sensitive when dealing with identifiers?": ["no","yes","machine dependent","None of the mention","b"],
    "College": ["ghrcem", "ghrce","ghrcacs","ghrceN","a"],
    "Which of the following is the correct extension of the Python file?" : [".python", ".pl", ".py", ".p", "c"],
    "Which keyword is used for function in Python language?" : ["Function", "def", "FUN", "Define", "b"]
}

for i in que:
    list_que.append(i)


for num,question in enumerate(list_que):

    r = ran_gen(new,list_que)

    print(f"\n\n\t\t\t\t\t\t\t{num+1}) {list_que[r]}")
    print(f"\n\t\t\t\t\t\ta) {que.get(list_que[r])[0]}\tb) {que.get(list_que[r])[1]}\n\n\t\t\t\t\t\tc) {que.get(list_que[r])[2]}\td) {que.get(list_que[r])[3]}")
    ans = input("\n\t\t\t\t\t\tAns: ")
    file4 = "D:\code\KBC\kbc_Clock.mp3"
    playsound(file4)

    win = check(ans,que,r,list_que,win)


ksm.showinfo("CONGRATULATION!!!", f'''AAP GHAR LE JA RAHE HO {win}\-
             KBC Khelne ka liye aap ka dhanyawad!!!''')

print(f"\n\t\t\t\t\t\tAAP GHAR LE JA RAHE HO {win}\-")