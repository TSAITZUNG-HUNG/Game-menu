def hello():
    import time
    kk=time.localtime()
    if(kk.tm_hour <12):
        print("good morning")
    elif(kk.tm_hour>=12 and kk.tm_hour <18):
        print("Good afternoon")
    else:
        print("Dear user : Good evening !")

def guessnumber():
    import random

# Generate a random number to be guessed
    number = random.randint(1, 100)

    print("Guess a magic number between 0 and 100")

    guess = -1
    while guess != number:
        
    # Prompt the user to guess the number
        guess = eval(input("Enter your guess: "))

        if guess == number:
            print("Yes, the number is", number)
        elif guess > number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
######################################################            
##################################
def bmi():
    weight=eval(input("pls enter your weight by Kg: "))
    height=eval(input("pls enter your height by cm: "))
    bmi= weight/ ((height/100)*(height/100))
    print("Your BMI is ", format(bmi,"5.2f"))
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")







def birthday():
    day = 0 # Day to be determined

    dates = [
      [[ 1,  3,  5,  7],
       [ 9, 11, 13, 15],
       [17, 19, 21, 23],
       [25, 27, 29, 31]],
      [[ 2,  3,  6,  7],
       [10, 11, 14, 15],
       [18, 19, 22, 23],
       [26, 27, 30, 31]],
      [[ 4,  5,  6,  7],
       [12, 13, 14, 15],
       [20, 21, 22, 23],
       [28, 29, 30, 31]],
      [[ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [24, 25, 26, 27],
       [28, 29, 30, 31]],
      [[16, 17, 18, 19],
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]]]
 

    for i in range(len(dates)):
        print(" Is your birthday in the set %2d"%(i+1))
        for j in range(len(dates[0])):
            for k in range(len(dates[0][0])):
                print(format(dates[i][j][k],'4d'), end=' ')
            print()
        ans=eval(input("Is in this set ? 0: no 1:yes  "))
        if ans==1:
            day+=dates[i][0][0]
    print("the final answer is : ", str(day))
  


#birthday() # Call the main function




def hello():
    import time
    time.time()
    time.time()
    time.localtime()
    aa=time.localtime
    aa=time.localtime()
    aa.tm_hour
    hr=aa.tm_hour
    if hr<6:
        	print("back to sleep!")
    elif hr>12 and hr<=18:
        	print("good afternoon")   




def 樂透():
    import random
    a=[]
    x=random.randint(1,20)
    a.append(x)
    while len(a)<6:
        x=random.randint(1,20)
        if x in a:
           print("這個數字重複了!!")
        else:
            a.append(x)

    ####
    b=[] #right answer #
    while len(b)<6:
        guess=eval(input("pls guess a number:"))
        if guess in b:
            print("已經猜過了")
            continue
        if guess in a:
            print("ok")
            b.append(guess)
        else:
            print("再接再厲")

    print("最後的答案是",b)


def 剪刀石頭布():     # scssior rock  paper
    import random
    cc=0   # cc for score
    time=0
    while cc < 2 and cc >-2 :
        ans=random.randint(0,2)
        guess=eval(input("guess a number  0 ~2  0:scissor 1:rock 2:paper"))
        if(ans==0 and guess==1) or (ans==1 and guess==2) or (ans==2 and guess==0) :
            print("you win")
            cc+=1
        elif(ans==0 and guess==0) or (ans==1 and guess==1) or (ans==2 and guess==2) :
            print("draw")
        else:
            print("you lose")
            cc-=1
        time+=1
        print("so far score is %3d"%(cc))

    ## end of while
        
    if(cc==2):
        print("Finaly !!   You win twice! \nYou played %5d times"%(time))    
    input("pls press \"Enter\" key to quit")
    
## end def srp()

#srp()


def 溫度轉換():
      celsius=eval(input("輸入一個攝氏溫度:"))
      f=celsius*(9/5)+32
      print("您所輸入的攝氏溫度換算成華氏溫標是%2d度"%(f))



def auto():   
    infile = open("me.txt", "r")
    print(infile.read())
    infile.close() # Close the input file    

#auto() # Call the main function






def ce():
    ce=eval(input("請輸入攝氏"))
    fa=eval(input("請輸入華氏"))
    fa=(9/5)*ce+32
    print(fa)
    ce=(5/9)*(fa-32)
    print(ce)
    
    print((9/5)*ce+32,(5/9)*(fa-32))








def checkpass():
    pass1=input("enter a password:")
    count=0
    for i in pass1:
        if i.isdigit():
            count+=1
    if len(pass1)>=8 and pass1.isalnum() and count>=2:
        return  True
    else:
        return False

    if count<2:
        return False

    
    if checkpass(pass1):
         print("valid password")
    else:
        print("invalid password")
    
       
    



def guessabc():
    import random
    guess=0
    ans=random.randint(65,90)
    y=chr(ans)
    while guess !=ans:
        guess=input("pls a A~Z charter :")
        
        if  guess < 'A' or guess >'Z':
            print("out of range")
            break
        if guess> y:
            print("too high")
        elif guess < y :
            print("too low")
        else:
            print("right answer")
            break



def countletter():
    count = 0
    s=input("enter a string")
    ch=input("enter a character")
    for letter in s:
        if letter == ch:
            count+=1
    print(s,ch)
    return count

    
def countletters():
          count=0
          for x in s:
              if x.isalpha():
                  count+=1
          return count

          s=input("enter a strang:")
          print(countletters(s))
   

#main()


def score():
    a2=[[1,2,3],[3,4,5,],[5,6,7]]
    for row in range(len(a2)):
        for col in range(len(a2[row])):
            print(a2[row][col],end="")
    print()

def score1():
    score=[[60,70,80,90], 
           [99,66,77,88],
           [77,88,67,97],
           [60,80,95,61]]
    for row in range(len(score[0])):
        totle=0
        for col in range(len(score[row])):
            totle=totle +score[row][col]
        print(totle)


def main():
    score_line=input("enter scores:")
    score_list=score_line.split()
    score=[int(s) for s in score_list]
    upper,avg=countupper(score)
    lower=len(score)-upper
    print("average:",round(avg,2))
    print("upper:",upper)
    print("lower:",lower)

    
def countupper(score):
    avg=sum(score)/len(score)
    count=0
    for s in score:
        if s >=avg:
            count+=1
    return count,avg




def shift(b):
	temp=b[0]
	for i in range(len(b)-1):
		b[i]=b[i+1]
	b[len(b)-1]=temp
	return b


def reve(b):
    low=0
    high=len(b)-1
    print(low,high)
    while low < high :
        b[low],b[high]= b[high],b[low]
        low=low+1
        high=high-1
    print(b)







