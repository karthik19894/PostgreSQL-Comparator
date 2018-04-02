class IssueWriter:
	def __init__(self,file):
		self.file=file

	def writeTableIssue(self,schema,tname):
		self.file.write("Table %s is Not Found in Database 2 under the schema %s But it is Found in Database 1"%(tname,schema))
		self.file.write('\n')

	def writePositiveColumnCount(self,tname):
		self.file.write("Column Count Matching For Table %s"%(tname))
		self.file.write('\n')

	def writeNegativeColumnCount(self,tname,col_count1,col_count2):
		self.file.write("Column Count Not Matching in Table %s"%(tname))
		self.file.write('\n')
		self.file.write("Column Count of Table %s In DB 1 is %s"%(tname,col_count1))
		self.file.write('\n')
		self.file.write("Column Count of Table %s In DB 2 is %s"%(tname,col_count2))
		self.file.write('\n')

	def writeColumnNotFound(self,cname):
		self.file.write('\n')
		self.file.write('Column %s Not Found in DB 2 But It is present in DB 1'%(cname))
		self.file.write('\n')

	def writeDataTypesMatching(self,cname):
		self.file.write('Datatypes are Matching For the Column %s' %(cname))
		self.file.write('\n')

	def writeDataTypesNotMatching(self,cname,db_dt1,db_dt2):
		self.file.write('Datatypes are Not Matching For the Column %s'%(cname))
		self.file.write('\n')
		self.file.write('Datatype in DB 1 is %s'%(db_dt1))
		self.file.write('\n')
		self.file.write('Datatype in DB 2 is %s'%(db_dt2))
		self.file.write('\n')


	def writeNullablesMatching(self,cname):
		self.file.write('\n')
		self.file.write('Nullable Conditions are Matching For the Column %s' %(cname))
		self.file.write('\n')

	def writeNullablesNotMatching(self,cname,db_nullable1,db_nullable2):
		self.file.write('Nullable Conditions are Not Matching For the Column %s' %(cname))
		self.file.write('\n')
		self.file.write('Nullable in DB 1 is  %s' %(db_nullable1))
		self.file.write('\n')
		self.file.write('Nullable in DB 2 is  %s' %(db_nullable2))
		self.file.write('\n')

	def writePrimaryKeysMatching(self,cname):
		self.file.write("Primary Key Constraint Names are matching For the Column %s" %(cname))
		self.file.write('\n')

	def writePrimaryKeysNotMatching(self,cname,pkey,pkey2):
		self.file.write("Primary Key Names are Not Matching For the Column %s" %(cname))
		self.file.write('\n')
		self.file.write("Primary Key Name in DB 1 is %s"%(pkey))
		self.file.write('\n')
		self.file.write("Primary Key Name in DB 2 is %s"%(pkey2))
		self.file.write('\n')

	def writePrimaryKeyNotDefined(self,cname):
		self.file.write("Primary Key Constraint is not defined For the Column %s in DB 2 as DB 1" %(cname))
		self.file.write('\n')

	def writeForeignKeysMatching(self,cname):
		self.file.write("Foreign Key Constraints are defined For the Column %s in DB 2 as DB 1" %(cname))
		self.file.write('\n')

	def writeForeignKeysNotMatching(self,cname,fkey,fkey2):
		self.file.write("Foreign Key Names are Not Matching For the Column %s" %(cname))	
		self.file.write('\n')
		self.file.write("Foreign Key Name in DB 1 is %s"%(fkey))
		self.file.write('\n')
		self.file.write("Foreign Key Name in DB 2 is %s"%(fkey2))
		self.file.write('\n')

	def writeForeignKeyNotDefined(self,cname):
		self.file.write("Foreign Key Constraint is not defined For the Column %s in DB 2 as DB 1" %(cname))
		self.file.write('\n')

	def writeUniqueKeysMatching(self,cname):
		self.file.write("Unique Key Constraints are defined For the Column %s in DB 2 as DB 1" %(cname))
		self.file.write('\n')



	def writeUniqueKeysNotMatching(self,c_name,fkey,fkey2):
		self.file.write("Unique Key Names are Not Matching For the Column %s" %(cname))
		self.file.write('\n')
		self.file.write("Unique Key Name in DB 1 is %s"%(fkey))
		self.file.write('\n')
		self.file.write("Unique Key Name in DB 2 is %s"%(fkey2))
		self.file.write('\n')


	def writeUniqueKeyNotDefined(self,cname):
		self.file.write("Unique Constraint is not defined For the Column %s in DB 2 as DB 1" %(cname))
		self.file.write('\n')

	def writeSchemaNotFound(self,schema):
		self.file.write("Schema %s Not Found in DB 2"%(schema))
		self.file.write('\n')


	def writeNoIssue(self):
		self.file.write("No Issues Found in the table :) ")
		self.file.write('\n')

	def writeIssues(self,issue_count):
		self.file.write("Total Number of Issues in the Table: "+str(issue_count))
		self.file.write('\n')

	def describeSchema(self,schema):
		self.file.write("---------------------------------------------------------------------------------------------------------------------------------")
		self.file.write('\n')
		self.file.write("Comparison Results of Schema: %s"%(schema))
		self.file.write('\n')

	def describeTable(self,table):
		self.file.write('\n')
		self.file.write('__________________________________________________________________________________________________________________________')
		self.file.write('\n')
		self.file.write('Comparison Results of Table: %s'%(table))
		self.file.write('\n')

	def describeComparison(self,host1,host2,db1,db2):
		self.file.write('********************************************************************************************')
		self.file.write('\n')
		self.file.write("-------------------------------Details of Comparison----------------------------------------")
		self.file.write('\n')
		self.file.write("IP Address of Server 1(Source): %s"%host1)
		self.file.write('\n')
		self.file.write("IP Address of Server 2 : %s"%host2)
		self.file.write('\n')
		self.file.write("Database Name of Server 1 : %s"%db1)
		self.file.write('\n')
		self.file.write("Database Name of Server 2 : %s"%db2)
		self.file.write('\n')
		self.file.write('********************************************************************************************')





