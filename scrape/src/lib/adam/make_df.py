
import dataclasses
import typing
import pandas as pd
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
    df = pd.DataFrame(
      data,
    )
    self.__df = AdamDF(
      keyword=df,
    )


class MakeAdamDFs():
  def __call__(
    self,
  ) -> AdamDF:
    self.__scrape()
    self.__make()
    return self.__df
  

  def __scrape(
    self,
  ) -> typing.NoReturn:
    f = ScrapeMultipleNews()
    tag = Tag(
      name='新連載',
      category='tag',
      tag_id=43,
    )
    self.__news = f(
      Category.COMIC,
      tag,
      Condition(
        max_page=1 << 3,
      ),
    )
  

  def __make(
    self,
  ) -> typing.NoReturn:
    f =  MakeAdamDF()
    keyword = []
    for news in self.__news:
      df = f(news)
      keyword.append(
        df.keyword,
      )
    df = pd.concat(keyword)
    self.__df = AdamDF(
      keyword=df,
    )