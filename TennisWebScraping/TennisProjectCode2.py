from bs4 import BeautifulSoup   
import urllib.request           
import csv
csvfile = open(("C:\\Users\\eliza\\OneDrive\\Code\\TennisData.csv"), newline='', encoding='utf-8')   #Replace C:\\...with the location of your csv file from the first code snippet.           
filecontent = csv.reader(csvfile)
filecontent = list(filecontent)
for i in range(len(filecontent)): 
    for j in range(len(filecontent[i])):
        workingInfo = []
        if j > 1:
            linkopen = urllib.request.Request(filecontent[i][j])
            try: 
                linkopen = urllib.request.urlopen(linkopen)       
            except urllib.error.URLError as e: 
                print(e.reason)
                continue
            if linkopen:
                soup = BeautifulSoup(linkopen, "html.parser")
                results = soup.select("b") 
                if results == None or len(results)==0: 
                    results = soup.select("B") 
                    for k in results: 
                        workingInfo.append(k.contents)
                else: 
                    for k in results: 
                        workingInfo.append(k.contents)
            newFileName = "C:\\Users\\eliza\\Desktop\\TennisInterviews\\" + str(filecontent[i][1]) + str(filecontent[i][j][-2:]) + ".txt"
            newFile = open(newFileName,"w", encoding="utf-8")
            newFile.write(str(workingInfo))  
            newFile.close() 