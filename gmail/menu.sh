#!/bin/sh
n=$(echo "${I3__messages}" | jq -r '.[] | "\(.from): \(.subject)"' \
| rofi -dmenu -format i -p "" \
  -no-cumstom -no-sort \
  -location 1 -xoffset $((I3_OUTPUT_X - I3_RELATIVE_X)) -yoffset ${I3_HEIGHT} \
)
if [ -z "$n" ]; then
    exit
fi

xdg-open https://mail.google.com/mail/#inbox/"$(echo "${I3__messages}" | jq -r .[$n].id)"
