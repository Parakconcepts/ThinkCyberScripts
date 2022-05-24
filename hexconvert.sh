#! /bin/bash

echo "Enter the Hex  number of your choice"

read Hex
 echo  "The decimal value of $Hex is: "
 echo  "obase=10; ibase=16; $Hex" | bc -l
