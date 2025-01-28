from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--mute-audio')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-infobars')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--no-sandbox')
options.add_argument('--no-zygote')
options.add_argument('--log-level=3')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--disable-breakpad')
# Set desired capabilities to ignore SSL stuffs

# desired_capabilities['acceptSslCerts'] = True

driver = webdriver.Chrome(
    options=options)

driver.implicitly_wait(10)


# Navigate to the webpage
url = "https://br.advfn.com/bolsa-de-valores/bmf/WING25/cotacao"
driver.get(url)

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Create a directory to store the downloaded files
if not os.path.exists("downloaded_files"):
    os.makedirs("downloaded_files")

# Save the HTML content
with open("downloaded_files/page.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# Find and download all script files
script_tags = driver.find_elements(By.TAG_NAME, "script")
for i, script in enumerate(script_tags):
    src = script.get_attribute("src")
    if src:
        try:
            response = requests.get(src)
            if response.status_code == 200:
                with open(f"downloaded_files/script_{i}.js", "wb") as f:
                    f.write(response.content)
        except:
            print(f"Failed to download script: {src}")

# Find and download all CSS files
link_tags = driver.find_elements(By.TAG_NAME, "link")
for i, link in enumerate(link_tags):
    href = link.get_attribute("href")
    if href and href.endswith(".css"):
        try:
            response = requests.get(href)
            if response.status_code == 200:
                with open(f"downloaded_files/style_{i}.css", "wb") as f:
                    f.write(response.content)
        except:
            print(f"Failed to download CSS: {href}")

# Find and download all images
img_tags = driver.find_elements(By.TAG_NAME, "img")
for i, img in enumerate(img_tags):
    src = img.get_attribute("src")
    if src:
        try:
            response = requests.get(src)
            if response.status_code == 200:
                with open(f"downloaded_files/image_{i}.{src.split('.')[-1]}", "wb") as f:
                    f.write(response.content)
        except:
            print(f"Failed to download image: {src}")

# Close the browser
driver.quit()

print("Download completed. Files saved in 'downloaded_files' directory.")
