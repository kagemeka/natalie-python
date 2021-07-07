import typing
from datetime import (
  datetime,
  timedelta,
)
import dataclasses
import requests
import bs4
from \
  lib.natalie.scrape \
  .news \
import (
  ScrapeNews,
  News,
  Tag,
)

from lib.natalie.scrape import(
  Category,
)

@dataclasses.dataclass
class Condition():
  start_time: datetime = (
    datetime.today()
    - timedelta(days=1 << 5)
  )
  max_page: int = 1 << 3



class ScrapeMultipleNews():
  def __call__(
    self,
    category: Category,
    tag: Tag,
    condition: Condition,
  ) -> typing.Iterator[News]:
    self.__category = category
    self.__tag = tag
    self.__condition = (
      condition
    )
    self.__get_ids()
    return self.__scrape()
  

  def __ids_per_page(
    self,
    page: int,
  ) -> typing.Iterable[int]:
    url = self.__base_url
    url = f'{url}/{page}'
    response = requests.get(
      url,
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    ls = soup.find(
      class_='NA_card_wrapper',
    ).find_all(
      class_='NA_card',
    )
    ls = [
      elm.find_all(
        'a',
      )[-1].get('href').split(
        '/',
      )[-1]
      for elm in ls
    ]
    return map(int, ls)


  def __parse_category(
    self,
  ) -> str:
    category = self.__category
    s = category.name.lower()
    return s 


  def __get_ids(
    self,
  ) -> typing.Iterator[int]:
    c = self.__parse_category()
    tag = self.__tag
    self.__base_url = (
      'https://natalie.mu/'
      f'{c}/{tag.category}/'
      f'{tag.tag_id}/page'
    )
    c = self.__condition
    for i in range(c.max_page):
      ls = self.__ids_per_page(
        i + 1,
      )
      for id_ in ls: yield id_


  def __scrape(
    self,
  ) -> typing.Iterator[News]:
    ids = self.__get_ids()
    f = ScrapeNews(
      category=self.__category
    )
    c = self.__condition
    for i in self.__get_ids():
      news = f(i)
      meta = news.metadata
      dt = meta.datetime
      if dt < c.start_time:
        break
      yield news
  



def main():
  base_url = (
    'https://natalie.mu/comic/'
  )


  id_ = 433741
  id_ = 435656

  scrape = ScrapeNews(
    Category.COMIC,
  )
  res = scrape(id_)
  print(res)
  f = ScrapeMultipleNews()
  tag = Tag(
    name='新連載',
    category='tag',
    tag_id=43,
  )
  news = f(
    Category.COMIC,
    tag,
    Condition(
      max_page=100,
    ),
  )
  for x in news:
    print(x)

  



if __name__ == '__main__':
  main()