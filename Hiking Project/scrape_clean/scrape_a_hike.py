# Scraping www.hikingproject.com for trails in Colorado
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

link_df = pd.DataFrame(columns=['hike_link']) 
df = pd.DataFrame(columns=['hike_name']) 

# open a web browser
driver = webdriver.Chrome()

# navigate to the page
driver.get('https://www.hikingproject.com/search?q=colorado')

# locate the "Load More" button
load_more_button = driver.find_element(By.XPATH, "//button[text()='Load More']")

# iterate 2 times and click the "Load More" button
for i in range(2):
    if load_more_button.is_displayed():
        load_more_button.click()

    # locate the elements that contain the hike name and region
    hike_links = driver.find_elements(By.XPATH, "//div[@class='sc-dPWrhe digRqT']/a")

    # iterate through the list of elements and extract the hike id
    for i in range(len(hike_links)):
        hike_link = hike_links[i].get_attribute("href")
        
        # append the extracted information to the DataFrame
        link_df = pd.concat([link_df, pd.DataFrame({'hike_link': hike_link}, index=[len(link_df)])], ignore_index=False)
     
 # iterate over the links in link_df
for i in range(len(link_df)):
    hike_link = link_df.iloc[i]["hike_link"]
    driver.get(hike_link)
    hike_names = driver.find_elements(By.XPATH, '//h1[@id="trail-title"]')
    if len(hike_names) == 0:
         # if there are no elements with an id of 'trail-title', continue to the next iteration
        continue
    hike_name = hike_names[0].text
    # create a new data frame with a single row containing the value of hike_name
    new_df = pd.DataFrame({'hike_name': [hike_name]})
    # concatenate the new data frame to the existing data frame hike_df
    df = pd.concat([df, new_df], ignore_index=True)
            
            
# close the web browser
driver.quit()

# print the DataFrame
#print(link_df)

# converting the dataframe object (df) to an HTML table
html_table = df.to_html()
with open('table.html', 'w') as f:
    f.write(html_table)
from IPython.display import display, HTML
display(HTML(df.to_html()))
