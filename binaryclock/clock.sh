#!/bin/sh
ON=${ON:-"●"}
OFF=${OFF:-"○"}
FORMAT=${FORMAT:-"%02d %04d %03d %04d %03d %04d"}
date +%H%M%S |
sed -e 's/./&;/g' -e  's/^/ibase=10;obase=2;/' |
bc |
tr "\n" " " |
awk -v on="${ON}" -v off="${OFF}" -v format="${FORMAT}" \ '{
    $0 = sprintf (format, $1, $2, $3, $4, $5, $6)
    gsub("0",off)
    gsub("1",on)
    print
}'
