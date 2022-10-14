#!/bin/sh
while read LINE; do 
echo "$LINE" | awk '{print toupper($0) }';
done
    
    
