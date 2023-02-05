from bs4 import BeautifulSoup as bsoup
import requests

urls=[]
# idx ranges from 1 to 408 after first get to main url
for i in range(408):
    response = requests.get('https://www.hikingproject.com/ajax/area/8007418/trails?idx='+str(i+1))
    #print(response.status_code)
    soup = bsoup(response.text, 'lxml')
    if soup.tr== None:
        print ('all done')
    else:
        for trtag in soup.find_all('tr'):
            urls.append([response.status_code,trtag['data-href']])
            #print(trtag['data-href'])
    
""" response2 = requests.get('https://www.hikingproject.com/trail/7038057/mf-ranch-creek-road-142')
print(response2.status_code)
#response.text
soup2 = bsoup(response2.text, 'lxml') """

#soup.find_all('div',