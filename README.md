# WikipediaScraper
Getting as much Wikipedia pages as we can

# Why
Good question, most Wikipedia dumps downloadable from Wikipedia's website need special software to be decompressed and viewed.\
With this tool you can scrape as much articles as you want with a PDF format, using only a web browser to view all the articles

# How
We use Wikidata's API because Wikidata Item IDs are ordered numerically, Wikipedia page IDs aren't, so we call Wikidata's API to get a Wikipedia title.\
Then we can use Wikipedia's API to convert a page to a PDF file with pictures, tables and text included.
