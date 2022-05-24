#! /bin/bash

for i in {0..20}

do
 echo $i
done


if  [ "$1" == "" ]

then
echo "You forgot an IP address"
echo "Example:./ipsweeper.sh "

else
for ip in `seq 1 254` ; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 |tr -d ":" &
done
