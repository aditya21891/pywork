# program for head and tails 
import random 
head,tail=0,0
def flip(num):
	head=random.randrange(2)
	tail=random.randrange(2)
if head ==0 :
	print("Heads")
else:
	print("Tails")
	
flip(10)