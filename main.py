from UserInput import UserInput
from IssueWriter import IssueWriter
from Compare import Compare
import threading

UI = UserInput()
done = False
UserInput.welcomeScreen()
file = UserInput.getOutputFile()
issueWriter = IssueWriter(file)
comparison = Compare(issueWriter)
host1, db1, user1, passwd1 = UserInput.getDbDetails('1')
curs1 = comparison.connectToDB(host1, db1, user1, passwd1, '5432')
host2, db2, user2, passwd2 = UserInput.getDbDetails('2')
curs2 = comparison.connectToDB(host2, db2, user2, passwd2, '5432')
schema_type = UserInput.getSchemaType()
schemas = comparison.getAllSchemas(curs1, schema_type)
positiveResults = UserInput.storePositive()
comparison.comparisonInfo(host1, host2, db1, db2)
print("Now Writing Comparison Results... Please Wait")
comparison.compareTables(schemas, curs1, curs2, positiveResults)
UserInput.closeOutputFile(file)
# t = threading.Thread(target=UserInput.loadingScreen())
# t.start()
# time.sleep(10)
print("Comparison is Now done :)")
