from bs4 import BeautifulSoup
import requests

data = requests.get("https://spotthestation.nasa.gov/trajectory_data.cfm").text
soup = BeautifulSoup(data,'lxml')
soup.prettify()
p = soup.find_all('p')
def remove_p(data):
    #data = str(data)
    data.replace("<p>", "")
    data.replace("</p>", "")
    return data

text = ""
for item in p:
    if item.id == None:
        #print(item)
        text  = text + remove_p(item.text) +"\n \n"
        
print(text)

#print(remove_p(p[2].text) +"\n \n" + remove_p(p[3].text) + "\n \n" + remove_p(p[4].text))
#print(p)
