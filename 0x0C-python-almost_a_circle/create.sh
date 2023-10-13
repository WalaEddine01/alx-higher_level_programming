#!/bin/bash

read -p "Enter the filename: " wa

touch "$wa"
cat ../r.py > "$wa" && chmod +x "$wa"
# Add any additional commands to modify the file's content if needed
vi "$wa"
