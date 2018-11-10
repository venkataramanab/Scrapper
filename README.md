**WebScrapper to fetch Naukri Recruiters**

>Installation

    pip install -r requirements.txt

>Simple usage: 

    python main.py
    
>Custom 

    scrapy crawl naukri -o <output-file-name>
    
>Advanced

>>Setting number of pages to crawl

    DEPTH_LIMIT = <number-of-pages-to-crawl>
    
Keep the above line in ```Scrapper/settings.py```