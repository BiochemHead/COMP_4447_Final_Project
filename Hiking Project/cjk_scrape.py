import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from IPython.display import display, HTML
from bs4 import BeautifulSoup as bsoup
import requests
import re

urls=[]

# GETS LIST OF TRAIL LINKS
driver = webdriver.Chrome()
driver.get('https://www.hikingproject.com/directory/8007418/colorado')
driver.implicitly_wait(30)
rows=driver.find_elements(By.CLASS_NAME, "text-black")

# REFINES TRAIL LINKS
for row in rows:
    test=row.get_attribute('href')
    if test != None:
        urls.append(test)

# Loop through rest of trails that would would normally be found by clicking open
# "Show More" but use idx number found from xhr info found from network section from
# Inspect Elements and incrementing to 408

for i in range(408):
    response = requests.get('https://www.hikingproject.com/ajax/area/8007418/trails?idx='+str(i+1))
    soup = bsoup(response.text, 'html.parser')
    for atag in soup.find_all('a'):
        url=atag.get('href')
        url=re.sub(r'["\\]','',url)
        urls.append(url)

# EXTRACTS NECESSARY DATA FROM EACH TRAIL PAGE

test_list = []
for link in urls:
    driver.get(link)
    name = driver.find_element(By.ID, "trail-title")
    difficulty = driver.find_elements(By.CLASS_NAME, 'trail-subheader')
    difficult = [d.text for d in difficulty]
    rating = driver.find_elements(By.CSS_SELECTOR, '#title-stars > span.small')
    site_rating = [r.text for r in rating]
    dogs = driver.find_elements(By.CSS_SELECTOR, '#trail-text > div:nth-child(2) > h3 > span')
    dog_feature = [d.text for d in dogs]
    description = driver.find_elements(By.CSS_SELECTOR, '#trail-text > div:nth-child(4)')
    stats = driver.find_elements(By.CLASS_NAME, 'stat-box')
    elev_up= driver.find_element(By.CSS_SELECTOR, "#trail-stats-bar > div:nth-child(3) > h3:nth-child(1) > span.imperial")
    elev_down= driver.find_element(By.CSS_SELECTOR, '#trail-stats-bar > div:nth-child(3) > h3:nth-child(3) > span.imperial')
    trail_length= driver.find_element(By.CSS_SELECTOR,'#trail-stats-bar > div.stat-block.ml-2.mr-1.mt-1 > span.imperial > h3')
    trail_type = driver.find_element(By.CSS_SELECTOR,'#trail-stats-bar > div.stat-block.ml-2.mr-1.mt-1 > h3')
    elev_high = driver.find_element(By.CSS_SELECTOR, '#trail-stats-bar > div:nth-child(2) > h3:nth-child(1) > span.imperial')
    elev_low = driver.find_element(By.CSS_SELECTOR, '#trail-stats-bar > div:nth-child(2) > h3:nth-child(3) > span.imperial')
    avg_grade = driver.find_element(By.CSS_SELECTOR, '#trail-stats-bar > div.stat-block.ml-1.mt-1 > h3:nth-child(1)')
    max_grade = driver.find_element(By.CSS_SELECTOR, '#trail-stats-bar > div.stat-block.ml-1.mt-1 > h3:nth-child(3)')
    test_list.append([name.text, difficult, site_rating, dog_feature, [stat.text for stat in stats], elev_up.text, elev_down.text, trail_length.text, trail_type.text, elev_high.text, elev_low.text, avg_grade.text, max_grade.text])
    print(link + ' complete')

# CONVERTS TO DATAFRAME

test_df = pd.DataFrame(data=test_list, columns=['Name','Site Diff Rating', 'Rating', 'Dogs and Features', 'Stats Breakdown', 'Elev_Up', 'Elev_Down', 'Trail Length', 'Trail Type', 'Highest Elevation', 'Lowest Elevation', 'Average Grade', 'Max Grade'])
test_df2 = test_df.replace('\n', ' ', regex=True)
display(HTML(test_df2.to_html()))            