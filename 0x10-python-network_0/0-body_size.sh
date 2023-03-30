#!/bin/bash
#Write a Bash script that takes in a URL, sends a request
curl -s "$1" | wc -c
