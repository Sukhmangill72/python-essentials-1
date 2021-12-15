Hh=int(input("Give me the start time (hour): "))
Mm=int(input("Give me the start time (minute): "))
Dd=int(input("Give me the duration in minutes: "))
Rr=(Hh*60)+Mm+Dd
print("The finish time is: ",end="")
print(Rr//60,Rr%60,sep=":")
      
