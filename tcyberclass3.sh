#! /bin/bash

age=7

if [ "$age" -gt 8 -a "$age" -lt 19 ]

then
  echo "the condition is true"
else
  echo "the condition is not true"
fi

age=22

if [ "$age" -gt 8 -o "$age" -lt 19 ]

then
  echo "the condition is okay"
else
  echo "the condition is not okay"
fi
