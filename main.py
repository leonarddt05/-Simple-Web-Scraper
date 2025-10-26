import requests
from bs4 import BeautifulSoup

def get_hacker_news_headlines():
    """
    Scrapes the headlines from the Hacker News homepage.
    """
    url = 'https://news.ycombinator.com/'
    
    print("Fetching headlines from Hacker News...")

    try:
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        headlines = []
        # Find all 'span' tags with the class 'titleline'
        for item in soup.find_all('span', class_='titleline'):
            # The headline text is within an 'a' tag inside the span
            link = item.find('a')
            if link:
                headlines.append(link.get_text())

        if not headlines:
            print("Could not find any headlines. The website structure may have changed.")
            return

        print("\n===== Top Hacker News Headlines =====\n")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to run the web scraper.
    """
    get_hacker_news_headlines()


if __name__ == "__main__":
    main()
