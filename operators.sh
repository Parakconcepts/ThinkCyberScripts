#! /bin/bash

age=10

if [ "$age" -gt 18 ] && [ "$age" -gt 9 ]

then
 echo "age is correct"
else
 echo "age is not correct"
fi


age=21

if [ "$age" -gt 18  -a  "$age" -gt 9 ]

then
 echo "age is correct"
else
 echo "age is not correct"
fi



age=10

if [ "$age" -gt 18  -o  "$age" -gt 9 ]

then
 echo "age is correct"
else
 echo "age is not correct"
fi
