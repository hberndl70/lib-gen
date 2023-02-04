#!/bin/bash
# run lib generator to create library 

mkdir output

edx_gen="../edx-gen/lib_gen.py"
input="./input"
output="./output"

python3 $edx_gen $input $output
