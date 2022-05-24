#! /bin/bash

for (( i=0; i<=10; i++ ))
do 
 if [ $i -gt 5 ]
then
 break
fi
 echo "$i"
 echo "TTTLLLLTTT"
done


for (( i=0; i<=15; i++ ))
do 
 if [ $i -eq 10 -o $i -eq 15 ]
then  continue
fi
 echo "$i"
done

