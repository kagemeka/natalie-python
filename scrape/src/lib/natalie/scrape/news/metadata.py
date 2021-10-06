import bs4 
import typing
import dataclasses
import datetime



@dataclasses.dataclass
class Metadata():
  title: str
  datetime: datetime.datetime
  score: typing.Optional[int] = None


def _scrape_metadata(section: bs4.element.Tag) -> Metadata:
  def get_title() -> str:
    return section.find(class_='NA_article_title').text

  def get_date() -> datetime.datetime.date:
    s = section.find(class_='NA_article_date').text
    format = '%Y年%m月%d日 %H:%M'
    return datetime.datetime.strptime(s, format)

  def get_score() -> typing.NoReturn:
    s = section.find(class_='NA_article_score')
    return int(s.text) if s else None
  
  return Metadata(get_title(), get_date(), get_score())






# class ScrapeMetadata():
#   def __call__(
#     self,
#     section: bs4.element.Tag,
#   ) -> Metadata:
#     self.__section = section
#     self.__scrape()
#     return self.__meta


#   def __get_title(
#     self,
#   ) -> typing.NoReturn:
#     s = self.__section.find(
#       class_='NA_article_title'
#     ).text
#     self.__title = s


#   def __get_date(
#     self,
#   ) -> typing.NoReturn:
#     s = self.__section.find(
#       class_='NA_article_date',
#     ).text
#     f = '%Y年%m月%d日 %H:%M'
#     dt = datetime.datetime.strptime(s, f)
#     self.__dt = dt
    

#   def __get_score(
#     self,
#   ) -> typing.NoReturn:
#     s = self.__section.find(
#       class_='NA_article_score'
#     )
#     self.__score = (
#       int(s.text) if s
#       else None
#     )
    

#   def __scrape(
#     self,
#   ) -> typing.NoReturn:
#     self.__get_title()
#     self.__get_date()
#     self.__get_score()
#     self.__meta = Metadata(
#       self.__title,
#       self.__dt,
#       self.__score,
#     )