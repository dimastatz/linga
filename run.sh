#!/bin/bash

abort()
{
    echo "*** FAILED ***" >&2
    exit 1
}


if [ "$#" -eq 0 ]; then
    echo "No arguments provided. Usage: 
    1. '-flask' to run flask"

elif [ $1 = "-flask" ]; then
    trap 'abort' 0
    flask --app ./linga/app.py run
fi

trap : 0
echo >&2 '*** DONE ***'