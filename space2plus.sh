#!/bin/bash

# Check if input was provided
if [ -z "$1" ]; then
    echo "Usage: $0 \"your string here\""
    exit 1
fi

# Replace spaces with +
modified="${1// /+}"

# Output the result
echo "$modified"
