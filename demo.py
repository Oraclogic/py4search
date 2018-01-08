# import rhinoscriptsyntax as rs
import json


# prompt the user for a file to import
# filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
# filename = rs.OpenFileName("sqlmap.json", filter)

filename = "/Users/zhoufeng/Documents/OneDrive/GitHub-Oraclogic/py4search/sqlmap.json"

# Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        json_contenst = f.read()
        print json_contenst

datastore = json.loads(json_contenst)
print(datastore)


# Use the new datastore datastructure
# print datastore
