
import dataclasses
import typing
import pandas as pd
import datetime 
from lib.natalie.scrape import (
  ScrapeMultipleNewsConfig,
  ScrapeMultipleNews,
  Category,
)
from lib.natalie.scrape.news import (
  Tag,
  News,
) 
from lib.aws_util.s3.upload import upload_to_s3


def update_news_keywords() -> typing.NoReturn:
  TAG = Tag(name='新連載', category='tag', tag_id=43)
  scrape_cfg = ScrapeMultipleNewsConfig(max_page=1 << 3)
  scrape = ScrapeMultipleNews(scrape_cfg)
  keywords = [
    _make_dataframe(news)
    for news in scrape(Category.COMIC, TAG)
  ]
  _store_to_s3(pd.concat(keywords))


def _make_dataframe(news: News) -> pd.DataFrame:
  data = {
    'category': news.category.name.lower(),
    'news_id': news.news_id,
    'keyword': news.keywords,
  }
  return pd.DataFrame(data)


def _store_to_s3(df: pd.DataFrame) -> typing.NoReturn:
  dt = datetime.datetime.now()
  save_path = '/tmp/keyword.csv'
  bucket = 'av-adam-store' 
  upload_obj = f'natalie/keyword.csv'
  df['updated_at'] = dt.date()
  df.to_csv(save_path, index=False)
  upload_to_s3(bucket, upload_obj, save_path)