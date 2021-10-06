import re
import typing
import bs4 



def _scrape_keywords(
  section: bs4.element.Tag,
) -> typing.List[str]:
  s = section.find(class_='NA_article_body').find('p').text
  ptn = re.compile(r'「([^」]*)」')
  return re.findall(ptn, s)


# class ScrapeKeyword():
#   def __call__(
#     self,
#     section: bs4.element.Tag,
#   ) -> typing.List[str]:
#     self.__section = section
#     self.__scrape()
#     return self.__keywords
  

#   def __scrape(
#     self,
#   ) -> typing.NoReturn:
#     s = self.__section.find(
#       class_='NA_article_body',
#     ).find('p').text
#     ptn = re.compile(
#       r'「([^」]*)」',
#     )
#     ls = re.findall(ptn, s)
#     self.__keywords = ls