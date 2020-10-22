from bs4 import BeautifulSoup   
import urllib.request           
import csv
tennisPlayerBaseURL = "http://www.asapsports.com/show_player.php?category=7&letter="
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
playerInterviewList = []
for i in alphabet:
    linkopen = urllib.request.Request(tennisPlayerBaseURL + i)
    try: 
        linkopen = urllib.request.urlopen(linkopen)       
    except urllib.error.URLError as e: 
        print(e.reason)
        continue
    if linkopen:
        soup = BeautifulSoup(linkopen, "html.parser")
        results = soup.select("b > a") 
        for j in results: 
            playerInterviewList.append([j['href']])
for i in range(len(playerInterviewList)): 
    linkopen = urllib.request.Request(playerInterviewList[i][0])
    print("Opening Name Number: " + str(i))
    try: 
        linkopen = urllib.request.urlopen(linkopen)       
    except urllib.error.URLError as e: 
        print(e.reason)
        continue
    if linkopen:
        soup = BeautifulSoup(linkopen, "html.parser")
        results = soup.select('h1') 
        for j in results: 
            playerInterviewList[i].append(j.contents[0])   
        results = soup.select('b > a') 
        for k in results: 
            playerInterviewList[i].append(k['href'])
with open('TennisData.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(playerInterviewList)
print("You did it!")
