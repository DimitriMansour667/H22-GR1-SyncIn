from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import urllib
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# client = pymongo.MongoClient("mongodb+srv://testuser:testuser@syncin.znpw2.mongodb.net/accounts?retryWrites=true&w=majority")
# db = client.test
# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+ urllib.parse.quote("é"))
print(html)