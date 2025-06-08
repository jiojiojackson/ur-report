# UR-Report

A tool for automatically collecting and analyzing UR housing property information in Japan, with a focus on commute times and rental prices.

## Features

- Automatically scrapes UR housing listings in the Kawasaki and Northern Yokohama areas
- Calculates commute times from each property to two preset locations (Shinjuku and Odaiba)
- Generates a beautiful HTML report with property information, including:
  - Property addresses
  - Rental prices (including maintenance fees)
  - Commute times to key locations
- Automatically publishes the report to GitHub Pages
- Sends a notification when the report is updated

## Requirements

- Python 3.6+
- Playwright
- Requests
- Pytz

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ur-report.git
   cd ur-report
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```
   playwright install
   ```

## Usage

Run the main script to collect data and generate a report:

```
python house.py
```

For English language support:

```
python house_en.py
```

The generated HTML report will be saved to `docs/index.html` and can be viewed in any web browser.

## How It Works

1. Uses Playwright to automate web scraping of the UR housing website
2. Filters properties in the Kawasaki and Northern Yokohama areas
3. For each property, calculates the commute time to two preset locations using Google Maps
4. Generates a visually appealing HTML report with all collected data
5. Publishes the report to GitHub Pages
6. Sends a notification when the report is updated

## Customization

You can customize the search locations by modifying the address variables in `house.py`:

```python
addressY = "Address 1"
addressZ = "Address 2"
```

## License

MIT 