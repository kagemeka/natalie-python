import bs4 
import requests
import typing


import dataclasses
from datetime import (
  datetime,
)


@dataclasses.dataclass
class Metadata():
  title: str
  date: datetime
  score: int



class ScrapeMetadata():
  def __call__(
    self,
    section: bs4.element.Tag,
  ) -> Metadata:
    self.__section = section
    self.__scrape()
    return self.__meta
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    ...




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
    ...

  


    


@dataclasses.dataclass
class News():
  news_id: int
  metadata: Metadata




class ScrapeNews():
  def __call__(
    self,
    news_id: int,
  ) -> News:
    self.__id = news_id
    self.__make_soup()
    self.__scrape()
    return self.__news
  

  def __init__(
    self,
  ) -> typing.NoReturn:
    ... 
    self.__base_url: str



  def __make_soup(
    self,
  ) -> typing.NoReturn:
    url = self.__base_url
    id_ = self.__id
    response = requests.get(
      f'{url}{id_}',
    )
    soup = bs4.BeautifulSoup(
      response.content,
      'html.parser',
    )
    self.__soup = soup
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    ...
  





def main():
  base_url = (
    'https://natalie.mu/comic/'
  )


  id_ = 433741
  
  url = (
    f'{base_url}news/{id_}'
  )

  response = requests.get(
    url,
  )
  soup = bs4.BeautifulSoup(
    response.content,
    'html.parser',
  )
  section = soup.find(
    class_='NA_article',
  )
  print(section.prettify())



if __name__ == '__main__':
  main()