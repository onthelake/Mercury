import requests
from bs4 import BeautifulSoup


def create_emotion_txt(emotion):
    filename = ("emotions/{}.txt").format(emotion)
    with open(filename, 'wb') as f:
        try:
            for i in range(1, 101):
                print(i)
                quotes_page = requests.get(
                    ("https://www.goodreads.com/quotes/tag/{}?page={}").format(emotion, i)).text
                soup = BeautifulSoup(
                    quotes_page,
                    "html.parser")

                for notNeeded in soup(["script", "style", "span", "a"]):
                    # remove unnecessary html elements
                    notNeeded.extract()

                quotes = [
                    quote for quote in soup.find_all(
                        'div',
                        attrs={'class': 'quoteText'})]

                for q in quotes:
                    text = q.find_all(text=True)
                    for line in text:
                        if line.strip() == "―" or line.strip() == ",":
                            # remove quote attributions
                            continue
                        f.write(line.strip().encode('utf-8'))
                        f.write('\n'.encode('utf-8'))
        except:
            pass
