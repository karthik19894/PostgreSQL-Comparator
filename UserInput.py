import easygui as eg
import itertools
import threading
import time
import sys

class UserInput:

	@classmethod
	def welcomeScreen(self):
		ch1=eg.msgbox(msg=" Welcome to Postgres Database Comparison, Click Start to Start The Comparison of Database and Data Model ",title="Welcome",ok_button="Start")
		if (ch1=='Start'):
			pass
		else:
			sys.exit(0)

	@classmethod
	def getDbDetails(self,hostid):
		host_v=eg.enterbox(msg='Enter the IP Address of Host '+hostid, title='Host '+hostid)

		self.checkNone(host_v)

		db=eg.enterbox(msg='Enter the Database Name of Host '+hostid, title='Database Name ')
		self.checkNone(db)

		usr=eg.enterbox(msg='Enter the Username For Host '+hostid, title='User Name ')
		self.checkNone(usr)

		pwd=eg.passwordbox(msg='Please Enter the Password For Host '+hostid, title='Password')

		self.checkNone(pwd)

		return host_v,db,usr,pwd

	@classmethod
	def getOutputFile(self):
		file_path=eg.fileopenbox(msg="Select the Output File Where the Results has to be Written",title="Open Output File",filetypes='.txt')
		file=open(file_path,'w')
		return file

	@classmethod
	def storePositive(self):
		pr=eg.ynbox(msg='Do you want to Store the Positive Results During Comparison')
		self.checkNone(pr)
		return pr
		

	@classmethod
	def closeOutputFile(self,file):
		file.close()


	@classmethod
	def getSchemaType(self):
		choice=eg.ynbox('Do You Want to Compare All the Schemas','Schema Comparison',('Yes','No'))
		if(choice==False):
			schema=eg.enterbox(msg='Enter the Schema Name to be Compared', title='Schema Name ')
			self.checkNone(schema)
			schemas=schema.split()
			return schemas
		else:
			return ["_multi"]

	def checkNone(var):
		if var is None:
			sys.exit(0)
		else:
			pass

	@classmethod
	def loadingScreen(self):
		for c in itertools.cycle(['|', '/', '-', '\\']):
			sys.stdout.write('\rLOADING ' + c)
			sys.stdout.flush()
			time.sleep(0.1)
		sys.stdout.write('\rDone :)     ')
