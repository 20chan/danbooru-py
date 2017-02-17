# danbooru-py
Very simple Danbooru crawler written in python3

## How to use
`danbooru.pages()` returns danbooru pages - lazily.
Each page is dict parsed from official api.
 - `page['rating']`
  - `s` : safe
  - `q` : questionable
  - `e` : explicit

[More in Danbooru API Document](https://danbooru.donmai.us/wiki_pages/43568)
