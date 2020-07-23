# You need to find two sentences that are closest in meaning to the one located in the very first line.
# As a measure of closeness in meaning, you need to use the cosine distance.


import re
import numpy as np
from scipy.spatial import distance


# this function removes x while it is present
def deletes(list_of_words, x):
    if x in list_of_words:
        list_of_words.remove(x)
        deletes(list_of_words, x)
    return list_of_words


# create variables
dictionary = {}
index = 1
indexes = {}
# open the file
lines = [line.lower() for line in open('sentences.txt')]
# delete unnecessary characters
all_words = re.split('[^a-z]', str(lines))
# delete spaces
words_without_spaces = deletes(all_words, '')
# save all the text in the line
text_in_line = ' '.join(words_without_spaces[:-1])
# delete unnecessary "n" characters
words = deletes(words_without_spaces, 'n')
# write dictionaries with word indexes(indexes) and count the total number of words(dictionary)
for word in words:
    if word not in indexes:
        indexes[word] = index
        index += 1
        dictionary[indexes[word]] = 1
    else:
        dictionary[indexes[word]] += 1
# divide the sentences
list_of_sentences = text_in_line.split(' n ')
# create a list of the number of words used
ls = [[sentence.split().count(element) for element in indexes] for sentence in list_of_sentences]
# create array
arr = np.array(ls)
# calculate and sort the cosine distance from the first row to the others
list_of_distances = [distance.cosine(arr[0], line) for line in arr]
list_of_distances_sorted = sorted(list_of_distances)
print(f'{list_of_distances.index(list_of_distances_sorted[1])} {list_of_distances.index(list_of_distances_sorted[2])}')
