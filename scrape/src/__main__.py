from lib.adam import (
  MakeAdamDFs,
)


from lib.adam import (
  AdamDF,
)


import typing
from datetime import (
  datetime,
)
import boto3 


class StoreDF():
  def __call__(
    self,
    df: AdamDF,
  ) -> typing.NoReturn:
    self.__df = df
    self.__add_timestamp()
    self.__save()
    self.__upload()


  def __init__(
    self,
  ) -> typing.NoReturn:
    dt = datetime.now()
    date = dt.date()
    self.__dt = dt
    self.__save_dir = '/tmp/'
    self.__upload_dir = (
      f'natalie/{date}/'
    )

  
  def __add_timestamp(
    self,
  ) -> typing.NoReturn:
    df = self.__df
    dt = self.__dt
    df.keyword['datetime'] = dt
  

  def __save(
    self,
  ) -> typing.NoReturn:
    d = self.__save_dir
    keyword_path = (
      f'{d}keywords.csv'
    )
    df = self.__df
    df.keyword.to_csv(
      keyword_path,
      index=False,
    )
    self.__keyword_path = (
      keyword_path
    )
  

  def __upload(
    self,
  ) -> typing.NoReturn:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(
      'av-adam-entrance',
    )
    d = self.__upload_dir
    bucket.Object(
      f'{d}keywords.csv',
    ).upload_file(
      self.__keyword_path,
    )

    

def main():
  base_url = (
    'https://natalie.mu/comic/'
  )


  make = MakeAdamDFs()
  df = make()
  store = StoreDF()
  store(df)
  print(df)



if __name__ == '__main__':
  main()