#! /bin/bash

number=1

while [ $number -lt 10 ]
do
 echo $number
 number=$(( number+1 ))
done

for (( i=0; i<=10; i++ ))
do 
 if [ $1 -gt 5 ]
then
 break
fi
 echo "$1"
done
