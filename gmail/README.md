# Gmail checker

## Installation

Follow the instructions by Google: https://developers.google.com/gmail/api/quickstart/python
Save the file credentials.json to `ygs-snippets/gmail/` directory.

## Events

- Left-click to open gmail.com.
- Right-click to refresh.

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
