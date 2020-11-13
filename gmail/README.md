# Gmail checker

## Requirements
 - Python3
 - [jq](https://stedolan.github.io/jq/)
 - [rofi](https://github.com/davatorium/rofi)

## Installation

Follow the instructions by Google: https://developers.google.com/gmail/api/quickstart/python
Save the file `credentials.json` to `ygs-snippets/gmail/` directory.

## Events

- Left-click to open rofi menu.
- Middle-click to open gmail.com.
- Right-click to refresh.

## Variables
Default values:
- `interval: 60`
- `retry: 5`
- `icon: "\uf0e0"`
- `color_normal: "#ffffff"`
- `color_unread: "#ff0000"`
- `color_loading: "#ffff00"`

## Example
```yml
  - widget: $ygs-snippets/gmail/gmail.yaml
    interval: 60
    templates: >
        [{
            "separator": true,
            "separator_block_width": 21
        }]
```
