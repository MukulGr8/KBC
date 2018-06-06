from random import *


class hmm:
	def __init__(self):
		self.count=-1
		
		
	def chec(self):
		qst = " Q) "
		with open('tran.log') as f:
		   for line in f:
			   if qst in line:
				   self.count=self.count+1
		self.count=self.count+1
		print(self.count)
		
	def one(self):
		f = open("tran.log","a")
		que = input("Enter Questions")
		self.count = self.count+1
		puts = " Q) "+ str(self.count)+" "+ que
		f.write(puts+"\n")
		opt1 = input("a)")
		f.write(opt1+"\n")
		opt2 = input("b)")
		f.write(opt2+"\n")
		opt3 = input("c)")
		f.write(opt3+"\n")
		opt4 = input("d)")
		f.write(opt4+"\n")
		ans = input("choice:")
		f.write(ans+"\n")
		f.close()
		print("Question Added")
		
		
	def two(self):
		f = open("tran.log","r")
		rano = randint(1, self.count)
		print(rano)
		while True:
			fin = ""
			fin = f.readline()
			qst = " Q) "+str(rano)
			if qst in fin:
				for i in range(1,6):
					print(fin)
					fin = f.readline()
				answ = fin
				ansu = input("Enter Your Answer No: ")
				if ansu in answ:
					print("Bingo")
					self.two()
				else:
					print("Sorry Wrong Answer")
					self.cond()
					f.close()
		

	def cond(self):
		while True:
			print("1) Enter Database")
			print("2) Play Game")
			cho = eval(input())
			if cho==1:
				self.one()
				
			elif cho==2:
				self.two()

if __name__=='__main__':
	ok = hmm()
	ok.chec()
	ok.cond()
	
