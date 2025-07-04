# Alibaba RFQ Scraper

A dynamic web scraping project that extracts RFQ (Request for Quotation) listings from Alibaba's UAE sourcing page using Python and Selenium.

## 🔧 Features

- Scrapes RFQ Titles and URLs from all listing pages
- Handles JavaScript-rendered content using scroll automation
- Navigates across multiple pages (pagination)
- Exports clean data to CSV
- Includes error handling and dynamic loading support

## 📦 Tech Stack

- Python 3.x
- Selenium WebDriver
- Pandas
- WebDriver Manager

## 📁 Output

Output saved in: `alibaba_rfq_output.csv`  
Includes 200+ RFQ titles and their respective links.

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install selenium pandas webdriver-manager
