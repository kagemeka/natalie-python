import dataclasses
import typing
import bs4 



@dataclasses.dataclass
class Tag():
  name: str
  category: str
  tag_id: int




def _scrape_tags(section: bs4.element.Tag) -> typing.List[Tag]:
  ls = section.find(class_='NA_taglist').find_all('a')
  tags = []
  for elm in ls:
    name = elm.text
    url = elm.get('href')
    category, id_ = url.split('/')[-2:]
    tags.append(Tag(name, category, int(id_)))
  return tags
    
      

# class ScrapeTag():
#   def __call__(
#     self,
#     section: bs4.element.Tag,
#   ) -> typing.List[Tag]:
#     self.__section = section
#     self.__scrape()
#     return self.__tags
  

#   def __scrape(
#     self,
#   ) -> typing.NoReturn:
#     ls = self.__section.find(
#       class_='NA_taglist',
#     ).find_all('a')
#     tags = []
#     for elm in ls:
#       name = elm.text
#       url = elm.get('href')
#       categ, id_ = url.split(
#         '/',
#       )[-2:]
#       tags.append(Tag(
#         name,
#         categ,
#         int(id_),
#       ))
#     self.__tags = tags
      