#!/bin/bash
echo "Bash version ${BASH_VERSION}..."
for i in {30500000..1760000000..1000000} 
  do 
     python3 rfp.py plott $i
 done
 
