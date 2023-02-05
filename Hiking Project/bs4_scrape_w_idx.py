from bs4 import BeautifulSoup as bsoup
import requests

# idx ranges from 1 to 409 after first get to main url
# there are only 4901 trails if you click through all of the show more buttons
# Title says 5855 trails, but not all are shown/acceccable
# From areas section that lists all states (https://www.hikingproject.com/directory/areas),
# site say colorado has 5855. but from home page under Trail Directory
# it says colorado has 6329 trails. Clearly some discrepancy.
# Used network section of inspect elelments to find XHR section/traffic for ajax URL

urls=[]

for i in range(409):
    response = requests.get('https://www.hikingproject.com/ajax/area/8007418/trails?idx='+str(i+1))
    #print(response.status_code)
    soup = bsoup(response.text, 'lxml')
    if soup.tr== None:
        print ('all done')
    else:
        for trtag in soup.find_all('tr'):
            urls.append(trtag['data-href'])
            #print(trtag['data-href'])
    
# response2 = requests.get('https://www.hikingproject.com/trail/7038057/mf-ranch-creek-road-142')
# print(response2.status_code)
# response.text
# soup2 = bsoup(response2.text, 'lxml')
# soup2.find_all('div',