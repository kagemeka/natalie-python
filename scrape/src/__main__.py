from \
  lib.natalie.scrape \
  .comic_news \
import (
  ScrapeNews,
)
  






def main():
  base_url = (
    'https://natalie.mu/comic/'
  )


  id_ = 433741
  id_ = 435656

  scrape = ScrapeNews()
  res = scrape(id_)
  print(res)
  



if __name__ == '__main__':
  main()