#!/bin/bash
# run lib generator to create library 

mkdir output

edx_gen="../edx-gen/lib-gen.py"
input = $1 

python3 $edx_gen $input
