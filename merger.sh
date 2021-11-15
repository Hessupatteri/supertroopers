#!/usr/bin/env bash
#This script merges all files in the current directory and outputs into a new file.

rm output.py

for file in *.py;do (cat "${file}";echo;echo) >> output.py;done
