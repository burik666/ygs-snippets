# RSS feed

## Requirements
 - python3
 - [feedparser](https://pypi.org/project/feedparser/)

## Events

- Left-click to open current item.
- Scroll up/down to show previous/next item.

## Example
```yml
  - widget: $ygs-snippets/rss/rss.yaml
    interval: 60
    feed: https://lorem-rss.herokuapp.com/feed
    templates: >
        [{
            "separator": true,
            "separator_block_width": 21
        }]
```
