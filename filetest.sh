#!/bin/bash
if [ $# == 0 ]
then
  echo "You have not provided any arguments. You
  must provide at least 1!"
  echo "filetest.sh"
  echo "Usage: filetest.sh filename1 [filename2,filename3,...]"
  echo " "
else
  for file in $*; do
      echo "Testing to see if $file exists..."
      if [ -e $file ]; then
	  comment="$file exists!"
	  perms=$(ls -l "$file" | awk '{print $1}')
	  echo "Permissions: $perms"
      else
	  comment="Sorry, $file does not exist"

      fi

      if [ -d "$file" ]; then
	  comment2="and it is a directory"

      else
	  comment2=""
  
          if [ ! -s "$file" ]; then
              echo "This file is blank."
	  fi
      fi
      echo "$comment $comment2"
      echo " "
  done
fi