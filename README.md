# Word-Sense-Disambiguation-

* The [Simplified Lesk algorithm](http://en.wikipedia.org/wiki/Lesk_algorithm) using WordNet as the lookup source.

1. lesk.py is the main program we need to compile and execute;
2. ReadMe.txt is a description of this program and instructions to compile and execute this program.  
3. report.docx includes three test cases: two positive cases that the program outputs the correct sense of the input word in the input sentence and one negative case that the program fails to output the correct sense of the input word in the input sentence
4. stop_words.txt includes stop words list

To compile and execute the program, you will need python 3.6 and NLTK. Instructions are followed.
1. download and unzip zipped program file into your home directory. 
2. open your command prompt and direct to your home directory.
3. type command line to compile and execute this program. The command is python lesk.py <word> <sentence>

Test case 1. python lesk.py bank the bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities. 
Test case 2. python lesk.py activity The traditions and activities that take place in celebration of the Day of the Dead are not universal, often varying from town to town.
Test case 3. python lesk.py spirit During Day of the Dead festivities, food is both eaten by living people and given to the spirits of their departed ancestors. 

4. in the command prompt, it will show the most probable sense of input word in the input sentence. 

