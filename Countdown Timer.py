num=int(input("Enter The Number Of Seconds for Countdown:"))
while(num!=0):
    from time import sleep
    print("Time remaining:",num,"seconds")
    sleep(1)
    num-=1
else:
    print("Time's Up!")
