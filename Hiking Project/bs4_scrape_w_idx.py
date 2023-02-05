from bs4 import BeautifulSoup as bsoup
import requests

response = requests.get('https://www.hikingproject.com/ajax/area/8007418/trails?idx=408')
# idx ranges from 1 to 408 after first get to main url

print(response.status_code)
#response.text
soup = bsoup(response.text, 'lxml')

if soup.tr== None:
    print ('all done')
else:
    for trtag in soup.find_all('tr'):
        print(trtag['data-href'])
    
response = requests.get('https://www.hikingproject.com/trail/7038057/mf-ranch-creek-road-142')
print(response.status_code)
#response.text
soup = bsoup(response.text, 'lxml')

#soup.find_all('div',