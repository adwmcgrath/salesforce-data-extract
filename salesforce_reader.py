import beatbox
import csv
import time


service = beatbox.PythonClient()  

#service.serverUrl = 'https://test.salesforce.com/services/Soap/u/20.0'
#use above code if querying a sandbox

service.login('username', 'password')  #add credentials

#add in SOQL queries as needed
query_result = service.query("select id from account")
sizer = query_result.size

query_result2 = service.query("select id from account")
sizer2 = query_result2.size

query_result3 = service.query("select id from contact")
sizer3 = query_result3.size

query_result4 = service.query("select id from contact")
sizer4 = query_result4.size

query_result5 = service.query("select id from opportunity")
sizer5 = query_result5.size

query_result6 = service.query("select id from opportunity")
sizer6 = query_result6.size

#print query results to terminal

dates = time.strftime("%d/%m/%Y")

print dates

print ('Total Accounts', sizer)

print ('Accounts in scope', sizer2)

print ('Total Contacts', sizer3)

print('Contacts in Scope', sizer4)

print('Total Optys', sizer5)

print('Optys in Scope',  sizer6)

#write to csv

with open('filepath', 'a') as csvfile:
      data = csv.writer(csvfile)
      data.writerow(['Date', dates])
      data.writerow(['Accounts', sizer])
      data.writerow(['Accounts in scope', sizer2])
      data.writerow(['Contacts', sizer3])
      data.writerow(['Contacts in scope', sizer4])
      data.writerow(['Optys', sizer5])
      data.writerow(['Optys in scope', sizer2])




