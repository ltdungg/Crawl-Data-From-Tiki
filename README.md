# Crawl-Data-From-Tiki

## Technique
- Python 3
- Library: Scrapy, Selenium
- Database: MySQL, PostgresSQL (update soon)
## How to Setup

Step 1: Clone
```
git clone https://github.com/ltdungg/Crawl-Data-From-Tiki.git
```
Step 2: Go to work directory
```
cd Crawl-Data-From-Tiki\TikiCrawler
```
Step 3: Install requirements
```
pip install requirements.txt
```
Step 4: Create vitural environment
```
python -m venv venv
```
Step 5: Activate vitural environment
```
venv/Scripts/activate
```
Step 6: Crawling

-O: overwrite

-o: append
```
python -m scrapy crawl main -O output.csv
```
