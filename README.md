# Automated-Data-Pipeline-and-Analysis-for-Indian-Small-Cardamom-Prices
Automating the collection, storage, and visualization of Indian small cardamom prices. It scrapes data from the Indian Spices Board, stores it in Google BigQuery, and uses Looker Studio for visualization. This helps farmers and traders analyze market trends easily

# Key Components:
## Data Collection:

Scraped daily price data from the Indian Spices Board website using Python, requests, and pandas.
## Data Storage:

Stored the scraped data in Google BigQuery for efficient querying and analysis.
## Automation:

Developed a Google Cloud Function to automate the data scraping process -> main.py and requirements.txt file .
Configured Google Cloud Scheduler to run the Cloud Function daily at 7 PM, ensuring consistent data collection every day.
## Data Transformation:

Processed and cleaned the raw data for accuracy and relevance.
Standardized data types and added timestamps for data collection.
## Data Visualization:

Created visualizations using Looker Studio.
These visualizations provide quick and easy access to market trends and insights.

## Impact:
This automated pipeline and visualization tool provide a valuable resource for farmers and traders in the cardamom industry which helps monitor price trends, compare auctioneer performance, and make data-driven decisions, contributing to a better understanding of the market and more strategic trading.

Live Visualization:
View the live Looker Studio report https://lookerstudio.google.com/reporting/cce693b0-7ba6-4271-baa3-9f2c920564b0.

