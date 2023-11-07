import requests
from bs4 import BeautifulSoup as bs


def doraemon_crawler(url: str) -> None:
    """
    Crawl the transcript of Doraemon from https://chinesedora.com/database/1.html
    :param url: the url of the transcript
    :return: None
    """
    # Get the html of the url
    response = requests.get(url)
    # Parse the html
    soup = bs(response.text, "lxml")
    # Get the transcript
    transcript = soup.find("div", class_="content").text


if __name__ == "__main__":
    url = "https://chinesedora.com/database/1.html"

    response = doraemon_crawler(url)
