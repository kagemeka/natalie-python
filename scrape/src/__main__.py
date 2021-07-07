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
  for x in news:
    print(x)

  



if __name__ == '__main__':
  main()