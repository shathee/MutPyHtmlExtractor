# TOM Generator
### This Tool mainly the Test Outcome Matrix from a given csv input.

TOM can be generated by passing then input file name or directory name. 
use the following command

`python tom.py -f path_to_filename` 
or
`python tom.py -d path_to_directory`




Steps to work with dataset from PIT

clean the PIT data with

`python tom.py -c filename`


Generate TOM with the cleaned dataset with  

`python tom.py -f path_to_filename` 
or
`python tom.py -d path_to_directory`


clean the generated TOM with 

`python tom.py -k filename` 

