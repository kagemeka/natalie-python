import typing
from lib.adam import update_news_keywords


def main() -> typing.NoReturn:
  update_news_keywords()


def lambda_handler(event, context) -> typing.NoReturn:  
  update_news_keywords()


if __name__ == '__main__':
  main()