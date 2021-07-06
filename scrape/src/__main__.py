import bs4 
import requests
import typing
from pprint import (
  pprint,
)

import dataclasses
from datetime import (
  datetime,
)


@dataclasses.dataclass
class Metadata():
  title: str
  datetime: datetime
  score: int



class ScrapeMetadata():
  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> Metadata:
    self.__section = section
    self.__scrape()
    return self.__meta


  def __get_title(
    self,
  ) -> typing.NoReturn:
    s = self.__section.find(
      class_='NA_article_title'
    ).text
    self.__title = s


  def __get_date(
    self,
  ) -> typing.NoReturn:
    s = self.__section.find(
      class_='NA_article_date',
    ).text
    f = '%Y年%m月%d日 %H:%M'
    dt = datetime.strptime(
      s,
      f,
    )
    self.__dt = dt
    

  def __get_score(
    self,
  ) -> typing.NoReturn:
    s = self.__section.find(
      class_='NA_article_score'
    ).text 
    self.__score = int(s)
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    self.__get_title()
    self.__get_date()
    self.__get_score()
    self.__meta = Metadata(
      self.__title,
      self.__dt,
      self.__score,
    )



@dataclasses.dataclass
class Tag():
  name: str
  category: str
  tag_id: int




class ScrapeTag():
  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> typing.List[Tag]:
    self.__section = section
    self.__scrape()
    return self.__tags
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    ls = self.__section.find(
      class_='NA_taglist',
    ).find_all('a')
    tags = []
    for elm in ls:
      name = elm.text
      url = elm.get('href')
      categ, id_ = url.split(
        '/',
      )[-2:]
      tags.append(Tag(
        name,
        categ,
        int(id_),
      ))
    self.__tags = tags
      


  

import re

class ScrapeKeyword():
  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> typing.List[str]:
    self.__section = section
    self.__scrape()
    return self.__keywords
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    s = self.__section.find(
      class_='NA_article_body',
    ).find('p').text
    ptn = re.compile(
      r'「([^」]*)」',
    )
    ls = re.findall(ptn, s)
    self.__keywords = ls
    

    


@dataclasses.dataclass
class News():
  news_id: int
  metadata: Metadata
  keywords: typing.List[str]
  tags: typing.List[Tag]




class ScrapeNews():
  def __call__(
    self,
    news_id: int,
  ) -> News:
    self.__id = news_id
    self.__make_soup()
    self.__find_section()
    self.__scrape()
    return self.__news
  

  def __find_section(
    self,
  ) -> typing.NoReturn:
    section = self.__soup.find(
      class_='NA_article',
    )
    self.__section = section


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__base_url = (
      'https://natalie.mu/'
      'comic/news'
    )
    

  def __make_soup(
    self,
  ) -> typing.NoReturn:
    url = self.__base_url
    id_ = self.__id
    response = requests.get(
      f'{url}/{id_}',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    section = self.__section
    f = ScrapeMetadata()
    res = f(section)
    pprint(res)
    f = ScrapeKeyword()
    res = f(section)
    pprint(res)
    f = ScrapeTag()
    res = f(section)
    pprint(res)
    self.__news = None
  





def main():
  base_url = (
    'https://natalie.mu/comic/'
  )


  id_ = 433741
  id_ = 435656

  scrape = ScrapeNews()
  scrape(id_)
  



if __name__ == '__main__':
  main()