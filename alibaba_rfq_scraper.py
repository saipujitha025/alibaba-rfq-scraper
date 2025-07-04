from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup Chrome
options = Options()
# options.add_argument("--headless")  # Show browser for debugging
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the Alibaba RFQ UAE page
driver.get("https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y")
time.sleep(6)

# Accept cookie popup if shown
try:
    cookie_btn = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookie_btn.click()
    print("✅ Accepted cookies.")
    time.sleep(2)
except:
    pass

data = []

# Loop through all pages
page_number = 1
MAX_PAGES = 10
while page_number <= MAX_PAGES:

    print(f"📄 Scraping Page {page_number}...")

    # Scroll to load dynamic content
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Extract titles and URLs
    titles = driver.find_elements(By.CLASS_NAME, "brh-rfq-item__subject-link")

    print("🔎 Found:", len(titles), "titles")

    for t in titles:
        try:
            title = t.text.strip()
            url = t.get_attribute("href")
        except:
            title = ""
            url = ""
        data.append({
            "Title": title,
            "RFQ URL": url
        })

    # Try to click the “Next” button
    try:
        next_button = driver.find_element(By.CLASS_NAME, "next")
        if "disabled" in next_button.get_attribute("class"):
            print("⛔ Reached last page.")
            break
        next_button.click()
        page_number += 1
        time.sleep(4)
    except Exception as e:
        print("⚠️ Could not find next button:", e)
        break

driver.quit()

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("alibaba_rfq_output.csv", index=False, encoding='utf-8-sig')
print(f"✅ Done! Scraped {len(df)} RFQs from {page_number} pages.")
