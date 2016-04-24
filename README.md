# Text Generator

##Overview
This is a Markov chain text generator. It reads in an input text file, generates random text, and writes to output.txt. It stops when the "current state" of the Markov chain is the last two words in your input file, or when it's generated 5000 words (whichever comes first).

##How do Markov chain text generators work?
Two consecutive words (word #1 and word #2 for our purposes) are picked from the corpus. These are our "current state". The next word in the generated text, word #3, is picked by:

1. searching the corpus for all occurences of our word #1 and word #2 bigram
2. making a list of all the words that follow this bigram
3. picking one of them randomly. (Note that the list in step 2 includes duplicates, so that more frequent following-words are more likely to be selected.)

Then, our "current state" is updated to be word #2 and word #3, and the process repeats to select word #4.


##What does this code do?
1. Text is read in and split into separate words.
2. A dictionary is created with bigrams as the keys and a list of "following words" as the values.
3. Two consecutive words are randomly selected to be the start of the generated text. These words are assigned to be our "current state". They are saved in a list.
4. The current state bigram is used to select the next word, using the dictionary created in step 2. The new word is appended to the list we created in step 3. The current state is updated to be the two most recent words in our list.
5. Step 4 repeats until either: a. the current state bigram isn't in the bigram dictionary, because it's the last two words in the input text (so there is no following word that could be used for the dict value), or b. 5000 words have been generated.
6. Generated text is written to output.txt.