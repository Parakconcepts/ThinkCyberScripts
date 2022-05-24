#! /bin/bash

number=1

while [ $number -lt 10 ]

do
 echo $number
 number=$(( number+1 ))
done


number=1

until [ $number -eq 13 ]

do
 echo $number
 number=$(( number+1 ))
done

number=1

until [ $number -gt 15 ]

do
 echo $number
 number=$(( number+1 ))
done
 
