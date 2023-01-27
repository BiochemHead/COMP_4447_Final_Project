# Scraping www.hikingproject.com for trails in Colorado
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


df = pd.DataFrame(columns=['hike_id', 'hike_name', 'hike_region', 'total_distance'])

# open a web browser
driver = webdriver.Chrome()

# navigate to the page
driver.get('https://www.hikingproject.com/search?q=colorado')

# locate the elements that contain the hike name and region
hike_ids = driver.find_elements(By.XPATH, "//div[@class='sc-dPWrhe digRqT']/a[1]")
hike_names = driver.find_elements(By.XPATH, "//h3[contains(@class, 'sc-cjibBx cKMyqg')]")
hike_regions = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-gYbzsP hksFOR')]")
total_distances = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-cCjUiG gazdbj')]")

# iterate through the list of elements and extract the hike name and region
for i in range(min((len(hike_ids), len(hike_names), len(hike_regions), len(total_distances)))):
    hike_id = hike_ids[i].get_attribute("href").split("/")[4]
    hike_name = hike_names[i].text
    hike_region = hike_regions[i].text.split(">")[0]
    total_distance = total_distances[i].text
    # append the extracted information to the DataFrame
    df = pd.concat([df, pd.DataFrame({'hike_id': hike_id, 'hike_name': hike_name, 'hike_region': hike_region, 'total_distance': total_distance}, index=[len(df)])], ignore_index=False)
   
# print the DataFrame
#print(df)

# close the web browser
driver.quit()

# converting the dataframe object (df) to an HTML table
html_table = df.to_html()
with open('table.html', 'w') as f:
    f.write(html_table)
from IPython.display import display, HTML
display(HTML(df.to_html()))
