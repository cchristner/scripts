import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import json

def scrape_agfunder_articles():
    """
    Scrapes article titles and URLs from AgFunder News pages
    Returns a list of dictionaries with 'title' and 'url' keys
    """
    base_urls = [
        "https://agfundernews.com/",
        "https://agfundernews.com/page/2",
        "https://agfundernews.com/page/3"
    ]
    
    articles = []
    
    # Headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for url in base_urls:
        try:
            print(f"Scraping: {url}")
            
            # Make the request
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            
            # Parse the HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all elements with class "article-title"
            article_elements = soup.find_all(class_="article-title")
            
            for element in article_elements:
                # Find the <a> tag within the article-title element
                link = element.find('a')
                
                if link:
                    # Extract the href and text
                    href = link.get('href')
                    title_text = link.get_text(strip=True)
                    
                    # Convert relative URLs to absolute URLs
                    if href:
                        absolute_url = urljoin(url, href)
                        
                        articles.append({
                            'title': title_text,
                            'url': absolute_url
                        })
            
            print(f"Found {len([e for e in soup.find_all(class_='article-title')])} articles on this page")
            
            # Be respectful to the server - add a small delay between requests
            time.sleep(1)
            
        except requests.RequestException as e:
            print(f"Error scraping {url}: {e}")
        except Exception as e:
            print(f"Unexpected error scraping {url}: {e}")
    
    return articles

def save_articles_to_json(articles, filename="agfunder_articles.json"):
    """Save articles to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)
    print(f"Articles saved to {filename}")

def print_articles(articles):
    """Print articles in a readable format"""
    print(f"\n{'='*80}")
    print(f"FOUND {len(articles)} ARTICLES")
    print(f"{'='*80}")
    
    for i, article in enumerate(articles, 1):
        print(f"\n{i}. {article['title']}")
        print(f"   URL: {article['url']}")

if __name__ == "__main__":
    # Scrape the articles
    articles = scrape_agfunder_articles()
    
    # Print results
    print_articles(articles)
    
    # Save to JSON file
    save_articles_to_json(articles)
    
    # Print summary
    print(f"\nScraping complete! Found {len(articles)} total articles.")
    print("Articles have been saved to 'agfunder_articles.json'")