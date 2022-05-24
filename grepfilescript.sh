#! /bin/bash

echo "Enter filename to search text"
read filename

if [[ -f $filename ]]
then

 echo "enter the text to search"
 read grepvar
 grep -i $grepvar $filename

else
 echo "filename not found"
fi
