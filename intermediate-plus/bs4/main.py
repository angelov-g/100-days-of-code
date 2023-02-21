from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article_tag = soup.find(name="span", class_="titleline")
# The line above doesn't work because the website have changed their HTML structure

articles = soup.select(selector="td span.titleline a")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

article_texts = article_texts[::2]
article_links = article_links[::2]

# Had to delete 1 result as it was an advert
article_texts.pop(6)
article_links.pop(6)

# print(article_texts)
# print(article_links)
# print(article_upvotes)

most_upvotes = max(article_upvotes)
largest_index = article_upvotes.index(most_upvotes)

print(article_texts[largest_index])
print(article_links[largest_index])




# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
