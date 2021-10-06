import dataclasses
import typing
import bs4
import requests
from .keyword import _scrape_keywords
from .tag import Tag, _scrape_tags
from .metadata import Metadata, _scrape_metadata
from lib.natalie.scrape.category import Category



@dataclasses.dataclass
class News():
  category: Category
  news_id: int
  metadata: Metadata
  keywords: typing.List[str]
  tags: typing.List[Tag]




def scrape_news(category: Category, news_id: int) -> News:
  base_url = f'https://natalie.mu/{category.name.lower()}/news'
  response = requests.get(f'{base_url}/{news_id}')
  soup = bs4.BeautifulSoup(response.content, 'html.parser')
  section = soup.find(class_='NA_article')
  return News(
    category,
    news_id,
    _scrape_metadata(section),
    _scrape_keywords(section),
    _scrape_tags(section),
  )
 


# class ScrapeNews():
#   def __call__(
#     self,
#     news_id: int,
#   ) -> News:
#     self.__id = news_id
#     self.__make_soup()
#     self.__find_section()
#     self.__scrape()
#     return self.__news
  

#   def __find_section(
#     self,
#   ) -> typing.NoReturn:
#     section = self.__soup.find(
#       class_='NA_article',
#     )
#     self.__section = section


#   def __init__(
#     self,
#     category: Category,
#   ) -> typing.NoReturn:
#     s = category.name.lower()
#     self.__category = s
#     self.__base_url = (
#       'https://natalie.mu/'
#       f'{s}/news'
#     )
    

#   def __make_soup(
#     self,
#   ) -> typing.NoReturn:
#     url = self.__base_url
#     id_ = self.__id
#     response = requests.get(
#       f'{url}/{id_}',
#     )
#     soup = bs4.BeautifulSoup(
#       response.content,
#       'html.parser',
#     )
#     self.__soup = soup
  

#   def __scrape(
#     self,
#   ) -> typing.NoReturn:
#     section = self.__section
#     scrapes = (
#       ScrapeMetadata(),
#       ScrapeKeyword(),
#       ScrapeTag(),
#     )
#     self.__news = News(
#       self.__category,
#       self.__id,
#       *(
#         f(section)
#         for f in scrapes
#       ),
#     )