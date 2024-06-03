# Vinted Price Scraper

This tool allows you to scrape prices from Vinted based on a search query and calculate the average price of the items found. The tool provides a simple graphical user interface (GUI) for entering the search query and starting the scraping process.

## Features

- Fetch prices from Vinted based on a search query.
- Calculate the average price of the items found.
- Simple GUI for ease of use.

## Requirements

- Python 3.x
- `selenium`
- `webdriver-manager`
- `beautifulsoup4`
- `tkinter` (usually included with Python installations)

## Installation

1. Clone the repository or download the scripts.
    ```bash
    git clone https://github.com/louiseleibbrandt/Vinted-pricer.git
    cd vinted-pricer
    ```

2. Install the required dependencies.
    ```bash
    pip install selenium webdriver-manager beautifulsoup4
    ```

3. This tool is currently only compatible with Chrome, please ensure Chrome is donwloaded and set as default browser.

## Usage

1. Run the `main.py` script to launch the GUI application.
    ```bash
    python scripts/main.py
    ```

2. Enter the search query in the provided input field.

3. Click the "Start Scraping" button. If the number of items span multiple pages, each page containing items will be loaded and scraped sequentially.

4. The tool will display the average price of the items found based on your search query.


## Example

![Screenshot of the GUI](images/GUI_example.png)


