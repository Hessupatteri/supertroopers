#!/usr/bin/env bash
#This script merges all files in the current directory and outputs into a new file.
rm output.py 2>/dev/null

after="main.py"
pat="def"

for file in *.py
do 
    if [ $file != $after ]
    then
        (echo "# ${file}";cat "${file}";echo;echo) >> output.py
        # Skriv ut samtliga funktioner från handle.py-filernas namn
        # cube(), tetrahedron()
        # ta reda pa hur vi laser ut specifikt funktionen namn ur dess definition
        foo=$(sed -n "/$pat/p" $file | cut -d' ' -f2)
        #sed 's/py:def\s//; s/://'
        
        echo ${foo%???}
        #echo $foo
        #cat $file | grep def | cut -d' ' -f2
    fi  
done

cat "$after" >> output.py
