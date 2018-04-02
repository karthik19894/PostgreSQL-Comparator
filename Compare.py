import psycopg2

class Compare():
	def __init__(self,issueWriter):
		self.issueWriter=issueWriter

	def connectToDB(self,hostip,db,username,passwd,port):
		conn = psycopg2.connect(database=db, user = username, password = passwd, host = hostip, port = port)
		curs=conn.cursor()
		return curs

	def convertResultToString(self,result):
		if(len(result)>0):
			return str(result[0])

	def getTables(self,schema,curs):
		curs.execute("Select table_name from information_schema.tables where table_schema='%s'"%(schema))
		tnames=curs.fetchall()
		return tnames

	def checkTable(self,curs,schema,tname):
		curs.execute("Select table_name from information_schema.tables where table_schema='%s' and table_name='%s'"%(schema,tname))
		t_check=curs.fetchone()
		if(t_check is None):
			return False
		else:
			return True

	def getAllSchemas(self,curs,schemaType):
		if(str(schemaType[0])=="_multi"):
			curs.execute("Select schema_name from information_schema.schemata where schema_name not like 'pg%' and schema_name not like'information_schema'")
			schemas=curs.fetchall()
			return schemas
		else:
			return schemaType

	def getSchema(self,curs,schema):
		curs.execute("Select schema_name from information_schema.schemata where schema_name='%s'"%(schema))
		schema=curs.fetchone()
		return schema

	def checkColumnCount(self,curs1,curs2,schema,tname):
		curs1.execute("Select count(distinct column_name) from information_schema.columns where table_name='%s' and table_schema='%s'"%(tname,schema))
		col_count1=curs1.fetchone()
		curs2.execute("Select count(distinct column_name) from information_schema.columns where table_name='%s'and table_schema='%s'"%(tname,schema))
		col_count2=curs2.fetchone()
		if(col_count1==col_count2):
			return True
		else:
			self.issueWriter.writeNegativeColumnCount(tname,col_count1,col_count2)
			return False

	def getColumns(self,curs,schema,tname):
		curs.execute("Select distinct column_name from information_schema.columns where table_name='%s' and table_schema='%s'"%(tname,schema))
		cnames=curs.fetchall()
		return cnames

	def checkColumn(self,curs,schema,tname,cname):
		curs.execute("Select column_name from information_schema.columns where table_name='%s' and table_schema='%s' and column_name='%s'"%(tname,schema,cname))
		ccheck=curs.fetchone()
		if(ccheck is None):
			return False
		else:
			return True


	def checkDataType(self,curs1,curs2,schema,tname,cname):
		curs1.execute("select data_type from information_schema.columns where table_name='%s' and column_name='%s' and table_schema='%s'"%(tname,cname,schema))
		db_dt1=curs1.fetchone()
		db_dt1=self.convertResultToString(db_dt1)

		curs2.execute("select data_type from information_schema.columns where table_name='%s' and column_name='%s' and table_schema='%s'"%(tname,cname,schema))
		db_dt2=curs2.fetchone()
		db_dt2=self.convertResultToString(db_dt2)
	

		if(db_dt1==db_dt2):
			return True
		else:
			self.issueWriter.writeDataTypesNotMatching(cname,db_dt1,db_dt2)
			return False

	def checkNullable(self,curs1,curs2,schema,tname,cname):
		curs1.execute("select is_nullable from information_schema.columns where table_name='%s' and column_name='%s' and table_schema='%s'"%(tname,cname,schema))
		db_nullable1=curs1.fetchone()
					
		if(db_nullable1 is not None):
			db_nullable1=self.convertResultToString(db_nullable1)
			curs2.execute("select is_nullable from information_schema.columns where table_name='%s' and column_name='%s' and table_schema='%s'"%(tname,cname,schema))
			db_nullable2=curs2.fetchone()
		if(db_nullable2 is not None):
			db_nullable2=self.convertResultToString(db_nullable2)

		if(db_nullable1==db_nullable2):
			return True
		else:
			self.issueWriter.writeNullablesNotMatching(cname,db_nullable1,db_nullable2)
			return False




	def checkPrimaryKey(self,curs1,curs2,schema,tname,cname):
		curs1.execute("SELECT constraint_name FROM information_schema.key_column_usage WHERE table_name = '%s' AND column_name='%s' AND table_schema='%s' AND constraint_name like '%%pk%%'"%(tname,cname,schema));
		pkey=curs1.fetchone()
				
		if(pkey is not None):
			pkey=self.convertResultToString(pkey)
			curs2.execute("SELECT constraint_name FROM information_schema.key_column_usage WHERE table_name = '%s' AND column_name='%s' AND table_schema='%s' AND constraint_name like '%%pk%%'"%(tname,cname,schema));
			pkey2=curs2.fetchone()
				
			if(pkey2 is not None):
				pkey2=self.convertResultToString(pkey2)
				if(pkey==pkey2):
					return True
				else:
					self.issueWriter.writePrimaryKeysNotMatching(cname,pkey,pkey2)
					return False
			else:
				return False
		else:
			return True
		




	def checkForiegnKey(self,curs1,curs2,schema,tname,cname):
		curs1.execute("SELECT constraint_name FROM information_schema.key_column_usage WHERE table_name = '%s' AND column_name='%s' AND table_schema='%s' AND constraint_name like '%%fk%%'"%(tname,cname,schema));
		fkey=curs1.fetchone()
				
		if(fkey is not None):
			fkey=self.convertResultToString(fkey)
			curs2.execute("SELECT constraint_name FROM information_schema.key_column_usage WHERE table_name = '%s' AND column_name='%s' AND table_schema='%s' AND constraint_name like '%%fk%%'"%(tname,cname,schema));
			fkey2=curs2.fetchone()
			
			if(fkey2 is not None):
				fkey2=self.convertResultToString(fkey2)
				if(fkey==fkey2):
					return True
				else:
					self.issueWriter.writeForeignKeysNotMatching(cname,fkey,fkey2)
					return False
				
			else:
				return False
		else:
			return True

				 
							
	  

										
	def checkUniqueKey(self,curs1,curs2,schema,tname,cname):
		curs1.execute("SELECT constraint_name FROM information_schema.constraint_column_usage WHERE table_name='%s' AND column_name='%s' AND table_schema='%s' AND constraint_name like '%%uk%%'"%(tname,cname,schema));
		ukey=curs1.fetchone()
		if(ukey is not None):
			ukey=self.convertResultToString(ukey)
			curs2.execute("SELECT constraint_name FROM information_schema.constraint_column_usage WHERE table_name='%s' AND column_name='%s' AND table_schema='%s' AND constraint_name like '%%uk%%'"%(tname,cname,schema));
			ukey2=curs2.fetchone()

			if(ukey2 is not None):
				ukey2=self.convertResultToString(ukey2)
				if(ukey==ukey2):
					return True
				else:
					self.issueWriter.writeUniqueKeysNotMatching(cname)
					return False
			else:
				self.issueWriter.writeUniqueKeyNotDefined(cname)
				return False
		else:
			return True

	def comparisonInfo(self,host1,host2,db1,db2):
		self.issueWriter.describeComparison(host1,host2,db1,db2)

	def compareTables(self,schemas,curs1,curs2,pr):
		for schema in schemas:
			if(len(schemas)>1):
				schema=self.convertResultToString(schema)
			schema2=self.getSchema(curs2,schema)
			self.issueWriter.describeSchema(schema)
			if(schema2 is not None):
				schema2=self.convertResultToString(schema2)
			if(schema2==schema):
				tnames=self.getTables(schema,curs1)
				for tname in tnames:
					tname=self.convertResultToString(tname)
					issue_count=0
					# print(tname,issue_count)
					tableFound=self.checkTable(curs2,schema,tname)
					self.issueWriter.describeTable(tname)
					
					if(not tableFound):
						issue_count+=1
						# print("table not found issue",issue_count,tname)
						self.issueWriter.writeTableIssue(schema,tname)
						continue
					else:
						if(self.checkColumnCount(curs1,curs2,schema,tname)):
							if(pr==True):
								self.issueWriter.writePositiveColumnCount(tname)

						else:
							issue_count+=1

						cnames=self.getColumns(curs1,schema,tname)
						for cname in cnames:
							if(cname is not None):
								cname=self.convertResultToString(cname)
							   
							if(not self.checkColumn(curs2,schema,tname,cname)):
								issue_count+=1
								# print("column not found issue",issue_count,tname)
								self.issueWriter.writeColumnNotFound(cname)
								continue

							else:
								'''Checking For Data Types'''
								if(not self.checkDataType(curs1,curs2,schema,tname,cname)):
									issue_count+=1
									# print("data type issue",issue_count,tname,cname)

								else:
									if(pr==True):
										self.issueWriter.writeDataTypesMatching(cname)


								
								'''Checking For Nullable Constraints'''
								if(not self.checkNullable(curs1,curs2,schema,tname,cname)):
								   	issue_count+=1
								   	# print("nullable issue",issue_count,tname,cname)

								else:
									if(pr==True):
										self.issueWriter.writeNullablesMatching(cname)


						   
								'''Checking For Primary Key Constraint'''
								
								if(not self.checkPrimaryKey(curs1,curs2,schema,tname,cname)):
									issue_count+=1
									# print("primary key issue",issue_count,tname,cname)
								else:
									if(pr==True):
										self.issueWriter.writePrimaryKeysMatching(cname)
					  
									
		
								'''Checking For Foreign Key Constraint'''
								if(not self.checkPrimaryKey(curs1,curs2,schema,tname,cname)):
									issue_count+=1
									# print("foreign key issue",issue_count,tname,cname)

								else:
									if(pr==True):
										self.issueWriter.writeForeignKeysMatching(cname)
								
			 
								''''Checking For Unique Constraint'''
								if(not self.checkUniqueKey(curs1,curs2,schema,tname,cname)):
									issue_count+=1
									# print("unique key issue",issue_count,tname,cname)

								else:
									if(pr==True):
										self.issueWriter.writeUniqueKeysMatching(cname)
										

					if(issue_count==0):
						self.issueWriter.writeNoIssue()
					else:
						self.issueWriter.writeIssues(issue_count)

						
			else:
				self.issueWriter.writeSchemaNotFound(schema)