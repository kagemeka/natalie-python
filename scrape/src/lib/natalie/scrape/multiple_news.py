import typing
import dataclasses
import datetime
import requests
import bs4
import  tqdm 
from .news import (
  News,
  Tag,
  scrape_news,
)
from .category import Category



@dataclasses.dataclass
class Config():
  start_time: datetime.datetime = (
    datetime.datetime.today() 
    - datetime.timedelta(days=1 << 5)
  )
  max_page: int = 1 << 3



class ScrapeMultipleNews():
  def __init__(self, cfg: Config) -> typing.NoReturn:
    self.__cfg = cfg  


  def __call__(
    self,
    category: Category,
    tag: Tag,
  ) -> typing.Iterator[News]:
    self.__category = category
    self.__tag = tag
    for i in self.__get_news_ids():
      news = scrape_news(category=self.__category, news_id=i)
      if news.metadata.dt < self.__cfg.start_time: return 
      yield news


  def __category_str(self) -> str:
    return self.__category.name.lower()


  def __get_news_ids(self) -> typing.Iterator[int]:
    tag = self.__tag
    self.__base_url = (
      f'https://natalie.mu/{self.__category_str()}/'
      f'{tag.category}/{tag.tag_id}/page'
    )
    for i in tqdm.trange(self.__cfg.max_page):
      for id_ in self.__ids_per_page(i + 1): yield id_


  def __ids_per_page(self, page: int) -> typing.List[int]:
    url = f'{self.__base_url}/{page}'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    ls = soup.find(class_='NA_card_wrapper').find_all(
      class_='NA_card',
    )
    return [
      int(elm.find_all('a')[-1].get('href').split('/')[-1])
      for elm in ls
    ]




