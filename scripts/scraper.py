from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

condition_map = {
    "All": 0,
    "New with tags": 6,
    "New without tags": 1,
    "Very good": 2,
    "Good": 3,
    "Satisfactory": 4
}

def fetch_search_results(query, condition, page=1):
    # Set up Selenium with Chrome
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    condition_number = condition_map[condition]
    # Construct URL
    if (condition_number == 0):
        url = f"https://www.vinted.nl/catalog?search_text={query}&page={page}"
    else:
        url = f"https://www.vinted.nl/catalog?search_text={query}&status_ids[]={condition_number}&page={page}"
    driver.get(url)
    time.sleep(5)  # Wait for the page to load completely

    html_content = driver.page_source
    driver.quit()
    return html_content

def extract_prices(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    prices = []
    for price_tag in soup.find_all('p', class_='web_ui__Text__text web_ui__Text__caption web_ui__Text__left web_ui__Text__muted'):
        # Strip text, remove euro sign and convert comma decimal to full-stop 
        price = price_tag.get_text(strip=True).replace('€', '').replace(',', '.').strip()
        if price:
            try:
                prices.append(float(price))
            except ValueError:
                continue
    return prices

def calculate_average(prices):
    if not prices:
        return 0.0
    return sum(prices) / len(prices)

def scrape_and_calculate(query, condition):
    page = 1
    all_prices = []

    while True:
        html_content = fetch_search_results(query, condition, page)
        prices = extract_prices(html_content)
        if not prices:
            break
        all_prices.extend(prices)
        # If less than 100 items listed, break loop
        if len(prices) < 100:
            break
        page += 1

    if all_prices:
        average_price = calculate_average(all_prices)
        return f"Average price for '{query}' with item condition '{condition}' is: €{average_price:.2f}"
    else:
        return "No items found."