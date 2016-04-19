import random

# Create a dictionary with bigrams as the keys and a list of "following words" as the values.
def bigram_dictionary(training_text):
    bigram_dict = {}
    pos = 0
    length = len(training_text)
    for word in training_text:
        # stop after we get to the last bigram that has a word following it.
        if pos <= (length - 3):
            dict_key = (word, training_text[pos + 1])
            # in case where bigram is already in dictionary, we want to append the "following word" to the value
            if dict_key in bigram_dict:
                #append following word to list for that dict_key
                bigram_dict[dict_key].append(training_text[pos+2])
            # when bigram is not yet in dictionary, add it as key along with its value
            else:
                bigram_dict[dict_key] = [training_text[pos+2]]
        pos = pos + 1
    return bigram_dict
            
def create_text(bigram_dict): 
    #put together list of all of the tuples that start sentences
    starts_of_sentences = [key for key in bigram_dict.keys() if key[0][0].isupper()]
    #pick a sentence start from that list. Set it to be the current state, as well as add it
    # to our random sentence
    current_state = random.choice(starts_of_sentences)
    text = [current_state[0], current_state[1]]
    i = 0
    while current_state in bigram_dict and i < 5000:
        second_word = current_state[1]
        # look up the current state in our bigram dictionary, and choose the following word.
        next_word = random.choice(bigram_dict[current_state])
        # Add it to our text.
        text.append(next_word)
        # update the current_state to the new state
        current_state = (second_word, next_word)
        i = i + 1
    text = ' '.join(text)
    return text

def main():
    with open('/Users/eloiseheydenrych/Documents/input.txt', 'r') as myfile:
        corpus = myfile.read().replace('\n', '')
    corpus = corpus.split()
    mydict = bigram_dictionary(corpus)
    mytext = create_text(mydict)
    with open("Output.txt", "w") as text_file:
        text_file.write(mytext)


main()



