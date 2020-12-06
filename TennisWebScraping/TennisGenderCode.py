import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


csvfile = open(("C:\\Users\\eliza\\OneDrive\\Code\\TennisDataGenderEdits.csv"), newline='', encoding='utf-8')
filecontent = csv.reader(csvfile)
filecontent = list(filecontent)
for i in range(len(filecontent)):
    filecontent[i][1] = filecontent[i][1].lower()

nameList = []
csvfile = open(("C:\\Users\\eliza\\OneDrive\\Code\\Names.csv"), newline='', encoding='utf-8')
filecontentNames = csv.reader(csvfile)
filecontentNames = list(filecontentNames)
for i in range(len(filecontentNames)):
    filecontentNames[i][0] = filecontentNames[i][0].lower()
for i in range(len(filecontentNames)):
    nameList.append(filecontentNames[i][0])

for i in range(len(filecontent)): 
    if len(filecontent[i]) < 3:
        filecontent[i] = filecontent[i] + process.extract(filecontent[i][1],nameList,limit=1)
        print(i)
with open("C:\\Users\\eliza\\OneDrive\\Code\\TennisDataGender.csv", 'w', newline='', encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(filecontent)

print("You did it!")