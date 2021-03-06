import os
import random
from time import sleep
score=0
wordno=1
i=7
corrword=0
difficulty=1
dname=['Error','Easy',"Hard"]
def start():
    clear = lambda: os.system('cls')
    clear()
    print("*********************************************************************************")
    print("\t\t\t\tWELCOME TO HANGMAN")
    print("*********************************************************************************")
    print("\t\t\t\tChoose your difficulty level")
    print("\t1:\tEasy\n\t2:\tHard\n\t3:EXIT")
    difficulty=int(input("ENTER:"))
    if(difficulty==3):
        print("*********************************************************************************")
        print("\t\t\t\t Thank you")
        print("*********************************************************************************")
        sleep(1)
        clear = lambda: os.system('cls')
        clear()
        exit(0)
    if(difficulty!=1 and difficulty!=2):
        print("Wrong choice")
        sleep(0.5)
        start()

    else:
        print("Difficulty CHOOSEN=",difficulty)
        sleep(0.5)
    return difficulty;
    
        
def display_hangman(i):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    print(stages[7-i])
def scorecard(score,corrword):
    clear = lambda: os.system('cls')
    clear()
    print("*********************************************************************************")
    print("\t\t\t\tGAME OVER")
    print("FINAL SCORE=",score)
    print("CORRECT WORDS=",corrword)
    print("*********************************************************************************")
    sleep(2)
    again()

def wordprint(k,meaning,score,i,wordno):
    print("*********************************************************************************")
    print("\t\t\t\tWELCOME TO HANGMAN")
    print("*********************************************************************************")
    print("Word number:",wordno,"\t\t\t\t\t\t SCORE:",score)
    print("difficulty=",dname[difficulty])
    print(k,":",meaning)
    print(i," CHANCES LEFT")
    display_hangman(i)

def again():
    score=0
    wordno=1
    i=7
    corrword=0
    difficulty=1
    difficulty=start()

   
    file = open('Easy.txt', 'r')

    if(difficulty==2):
        file=open('Hard.txt','r')
    for each in file:
        word,meaning=each.split(':')
        word=word.strip().lower()
        l=len(word)
        m1=random.randint(0,l-1);
        m2=random.randint(0,l-1);
        while m2==m1:
            m2=random.randint(0,l-1);
        m3=random.randint(0,l-1);
        while m3==m1 or m3==m2:
            m3=random.randint(0,l-1);
        k=""
        for a in range(len(word)):
            if(a == m1 or a == m2 or a == m3):
                k=k+"_"
            else:
                k=k+word[a]
        i=7
        lt=[]
        lt.append(m1)
        lt.append(m2)
        lt.append(m3)
        lt.sort()
        m1,m2,m3=lt
        while i>0:
            if(m1==-1 and m2 == -1 and m3==-1):
                break;
            clear = lambda: os.system('cls')
            clear()
            wordprint(k,meaning,score,i,wordno);
            print("availaible position :",end="")
            if(m1!=-1):
                print(m1+1," ",end='')
            if(m2!=-1):
                print(m2+1," ",end='')
            if(m3!=-1):
                print(m3+1,end='')
            a=int(input("\nPOSITION:").strip())-1
            ans="CORRECT ANSWER"
            if(a == m1 and m1 != -1 or a == m2 and m2 != -1 or a == m3 and m3 !=-1):
                b=input("ALPHABET:").lower()
                if(b == word[m1] and a == m1):
                    k=k[0:a]+b+k[a+1:]
                    m1=-1
                elif b == word[m2] and a == m2:
                    k=k[0:a]+b+k[a+1:]
                    m2=-1
                elif  b == word[m3] and a == m3:
                    k=k[0:a]+b+k[a+1:]
                    m3=-1
                else:
                    i=i-1;
                    ans=("WRONG ANSWER")
            else:
                print("WRONG POSITION")
                sleep(0.5)
                continue;
            sleep(0.5)
            print(ans)
            sleep(1)
        if(i==0):
            clear = lambda: os.system('cls')
            clear()
        
            print("*********************************************************************************")
            print("\t\t\t\tWELCOME TO HANGMAN")
            print("*********************************************************************************")
            print("Word number:",wordno,"\t\t\t\t\t\t SCORE:",score)
            print("**********************************")
            print("\t\t\t\tCHANCES OVER\n \t\t\t\ttry other words")
            print("**********************************")
            sleep(2)
        
        else:
            clear = lambda: os.system('cls')
            clear()
            score=score+10;
            corrword+=1
            print("*********************************************************************************")
            print("\t\t\t\tWELCOME TO HANGMAN")
            print("*********************************************************************************")
            print("Word number:",wordno,"\t\t\t\t\t\t SCORE:",score)
            print("**********************************")
            print("\t\t\t\tWELL DONE\n\t\t\t\tWORD=",word)
            print("**********************************")
            sleep(2)
        wordno=wordno+1
    scorecard(score,corrword)
again()