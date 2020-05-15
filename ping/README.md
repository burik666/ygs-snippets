# Ping

## Events

- Left-click to refresh.

## Variables
Default values:
  - `host: 127.0.0.1`
  - `interval: 30`
  - `color_down: "#ff0000"`
  - `color_up: "#00ff00"`
  - `color_refresh: "#ffff00"`

## Example
```yml
  - widget: $ygs-snippets/ping/ping.yaml
    host: 8.8.8.8
    interval: 30
    templates: >
        [{
            "full_text": "\uf26b",
            "separator": true,
            "separator_block_width": 21
        }]
```
