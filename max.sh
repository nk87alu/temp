#!/bin/bash

echo "First number:"
read num1
echo "Second number:"
read num2

if (( $(echo "$num1 > $num2" | bc -l) )); then
    echo "The larger number is: $num1"
elif (( $(echo "$num1 < $num2" | bc -l) )); then
    echo "The larger number is: $num2"
else
    echo "Both numbers are equal: $num1"
fi