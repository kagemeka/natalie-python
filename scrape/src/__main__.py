from lib.natalie.scrape import(
  ScrapeMultipleNews,
  Category,
)
from \
  lib.natalie.scrape \
  .multiple_news \
import (
  Condition,
)
from lib.natalie.scrape.news \
import (
  Tag,
  News,
) 



import dataclasses
import typing
import pandas as pd



@dataclasses.dataclass
class AdamDF():
  keyword: pd.DataFrame
  


class MakeAdamDF():
  def __call__(
    self,
    news: News, 
  ) -> AdamDF:
    self.__news = news
    self.__make()
    return self.__df
  

  def __make(
    self,
  ) -> typing.NoReturn:
    news = self.__news
    data = {
      'category': news.category,
      'news_id': news.news_id,
      'keyword': news.keywords,
    }
    self.__df = pd.DataFrame(
      data,
    )


def main():
  base_url = (
    'https://natalie.mu/comic/'
  )


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
      max_page=1 << 3,
    ),
  )
  make = MakeAdamDF()
  for x in news:
    # print(x)
    df = make(x)
    print(df)

  



if __name__ == '__main__':
  main()