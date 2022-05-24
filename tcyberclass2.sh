#! /bin/bash

count=7

if [ $count -eq 10 ]

then
   echo "the condition is true"
elif [ $count <= 9 ]
then
  echo "the first condition is true"
else
  echo "the second condition is true"
fi

