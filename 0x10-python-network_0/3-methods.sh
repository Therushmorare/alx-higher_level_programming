#!/bin/bash
#task 3
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
