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
  score: typing.Optional[
    int
  ] = None



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
    )
    self.__score = (
      int(s.text) if s
      else None
    )
    

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