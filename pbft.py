from view import *
from message import *
from shortest_path import *
import random
from cryptography.fernet import Fernet
from get_plot import *
import matplotlib.pyplot as plt

class pbft:
	def __init__(self,graph,path,GPLOT,SPLOT,src,dest,F):
		self.src = src
		self.dest = dest
		self.GRAPH = graph
		self.VIEW = view(1,random.randint(0,self.GRAPH.N))
		self.SP = path
		self.GPLOT = GPLOT
		self.SPLOT = SPLOT

		self.key = Fernet.generate_key()
		self.F = F 

		self.FaultyNode = []
		self.FaultyLeader = []
		for i in range(self.F):
			self.FaultyNode.append(random.randint(0,self.GRAPH.N))
		# print("Faulty Nodes:{}".format(self.FaultyNode))

	def controller(self):
		#to-do: change this message to shortest path message
		
		path,weight = self.SP.get_path()
		MSG = "Shortest path: "+str(path)+"\nWeight: "+str(weight)
		# print(MSG)
		netState = "start"
		while netState!="end":
			print("FaultyNode: ",self.FaultyNode)
			print("Faultyleaders: ",self.FaultyLeader)
			self.PhaseI(MSG)
			
			#initiate the view change beacuse of faulty leader
			if self.VIEW.leader in self.FaultyNode:
				self.FaultyLeader.append(self.VIEW.leader)
				newLeader,newViewNo = random.randint(0,self.GRAPH.N),self.VIEW.viewNo+1
				self.VIEW =view(newViewNo,newLeader)
				continue
			self.PhaseII()
			self.PhaseIII()
			self.FinalCommit()
			netState = "end"

	def encrypt(self,message):
		cipher_suite = Fernet(self.key)
		encoded_text = cipher_suite.encrypt(message.encode("ASCII"))
		decoded_text = cipher_suite.decrypt(encoded_text)
		return encoded_text
	def valid(self,message):
		cipher_suite = Fernet(self.key)
		decoded_text = cipher_suite.decrypt(message.digest)
		if decoded_text.decode('ASCII')==message.message:
			return True
		return False


	def PhaseI(self,leadermsg):
		print("LEADER: ",self.VIEW.leader)
		print("phaseI started .................................")
		for i in range(self.GRAPH.N+1):
			if i==self.VIEW.leader or i in self.FaultyLeader:
				continue
			else:
				msg = message("Preprepare",self.VIEW.viewNo,leadermsg,self.encrypt(leadermsg),self.key)
				self.VIEW.backups.append([i,msg])
		
		# for obj in self.VIEW.backups:
		# 	print(obj[0],obj[1].state,obj[1].viewNo,obj[1].message,obj[1].digest,obj[1].Prk)
		# print(self.VIEW.backups)
	def PhaseII(self):
		print("PhaseII started .................................")
		for i in range(len(self.VIEW.backups)):
			curObj = self.VIEW.backups[i]
			if self.VIEW.viewNo==curObj[1].viewNo and self.valid(curObj[1]):
				
				for j in range(len(self.VIEW.backups)):
					if curObj[0]==self.VIEW.backups[j][0]:
						continue
					else:
						mess = curObj[1].message
						if curObj[0] in self.FaultyNode:
							mess = "error_mssg"
						msg = message("Prepare",self.VIEW.viewNo,mess,curObj[1].digest)
						self.VIEW.backups[j].append(msg)
		# for obj in self.VIEW.backups:
		# 	print(len(obj))
		# from sys import stdout

		# for i in range(len(self.VIEW.backups)):
		# 	curobj = self.VIEW.backups[i]
		# 	for j in range(1,len(curobj)):
		# 		stdout.write("{} ".format( curobj[j].message ))
		# 	print()
		# print(self.VIEW.backups)
	

	def PhaseIII(self):
		print("phaseIII started .................................")
		for i in range(len(self.VIEW.backups)):
			currobj = self.VIEW.backups[i]
			COUNT = 0
			for j in range(1,len(currobj)):
				if currobj[j].state=="Prepare":
					COUNT+=1

			if COUNT>=(2*self.F)+1:
				for j in range(len(self.VIEW.backups)):
					nextobj = self.VIEW.backups[j]
					if currobj==nextobj:
						continue
					else:
						msg = message("Commit",self.VIEW.viewNo,self.VIEW.backups[j][1].message,currobj[1].digest)
						self.VIEW.backups[j].append(msg)

	def FinalCommit(self):
		print("FinalCommit started .................................")
		d = {}
		for i in range(len(self.VIEW.backups)):
			currobj = self.VIEW.backups[i]
			COUNT =0
			for j in range(1,len(currobj)):
				if currobj[j].state=="Commit":
					COUNT+=1
			if COUNT>=2*self.F:
				if currobj[1].message in d:
					d[currobj[1].message]+=1
				else:
					d[currobj[1].message] = 1

		m = 0
		mess =""
		for i in d:
			if d[i]>m:
				m = d[i]
				mess = i
		# print(d)
		if len(mess)==0:
			mess= "unable to reach consensus due to more faulty nodes"
			print("Final Message ",mess)
		else:
			print("Final Message ",mess)
			self.GPLOT.show("Network")
			self.SPLOT.show("Shortest_Path")
			plt.show()


		






		




		



		


	


