# Weather

## Requirements
 - Python3
 - [Font Awesome](https://fontawesome.com)

## API Key

To get access to weather API you need an APIID.
See https://openweathermap.org/appid for details.

## Events

- Left-click to open openweathermap.org site.
- Right-click to refresh.

You can override the weather site by adding following event:
```yml
    events:
        - button: 1
          override: true
          command: xdg-open "https://yandex.ru/pogoda/saint-petersburg"
```

## Example
```yml
  - widget: $ygs-snippets/weather/weather.yaml
    interval: 600
    apikey: <YOUR_API_KEY>
    city: Saint Petersburg,ru
    units: metric
    template: >
        {
            "color": "#ffffff",
            "separator": true,
            "separator_block_width": 21
        }

```
