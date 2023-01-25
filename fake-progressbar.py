import os

def progressBar(current, total):
    
    percent = current/(total/100)
    print("["+"█"*int(percent)+"░"*(100-int(percent))+f"] {round(percent,2)}% {current}/{total}")
    
    if(current == total):
        input()

    os.system('cls' if os.name == 'nt' else 'clear')
    

