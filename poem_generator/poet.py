import re, random
import numpy as np
import json
poem_files = ['pg17192.txt', 'Where the Sidewalk Ends by Shel Silverstein_djvu.txt']
poem_lines = []
firstword_count_dict = {}
firstword_prob_dict = {}

for poem_file in poem_files:
    f = open(poem_file, 'r')

    for line in f:
        if len(line) > 1:
            words = re.findall('\w+', line)
            if len(words) > 1:
                poem_lines.append(words)
    f.close()

#print poem_lines

unicorns = set()
words = []
last = 0
lines = 0
for line in poem_lines:
    lines += 1
    if len(line) >= 1 and line[-1] == 'weary':
        last += 1
    for word in line:
        unicorns.add(word)
        words.append(word)

# firstword_counts = {}
#
# for line in poem_lines:
#     if len(line) > 2:
#         first_word = line[0]
#
#         if first_word in firstword_counts:
#             firstword_counts[first_word] += 1
#         else:
#             firstword_counts[first_word] = 1
#
# print firstword_counts
# words = words.replace(',', '').replace('.', ' ')
#
# word_states = re.findall('\w+', words)
#
# print word_states
# print len(set(word_states))
#
# counts_dict = {}
#
# for i in range(len(word_states)-1):
#     first_word = word_states[i]
#     next_word = word_states[i+1]
#
#     if (first_word, next_word) in counts_dict:
#         counts_dict[(first_word,next_word)] += 1
#     else:
#         counts_dict[(first_word,next_word)] = 1
#
# transition_probabilities = {}
# s = sum(counts_dict.values())
#
#
# for key in counts_dict:
#     transition_probabilities[key] = float(counts_dict[key])/s
# print transition_probabilities
# #    float(counts_dict.keys())/s
# #for x in range(10):
# #    sentence = ''
# #    for i in range(10):
# #        word = results[random.randint(0, len(results) - 1)]
# #        sentence += ' ' + word
# #    print sentence

# next_word_counts_dict = {}
# for word_list in poem_lines:
#     word_list.append('\n')
#     for i in range(len(word_list) - 1):
#         thisword = word_list[i]
#         nextword = word_list[i+1]
#
#         if thisword not in next_word_counts_dict:
#             next_word_counts_dict[thisword] = {nextword:1}
#         else:
#             if nextword not in next_word_counts_dict[thisword]:
#                 next_word_counts_dict[thisword][nextword] = 1
#             else:
#                 next_word_counts_dict[thisword][nextword] += 1

for line in poem_lines:
    if len(line) > 0:
        first_word = line[0]

        if first_word in firstword_count_dict:
            firstword_count_dict[first_word] += 1
        else:
            firstword_count_dict[first_word] = 1

count_sum = sum(firstword_count_dict.values())

for first_word in firstword_count_dict:
    firstword_prob_dict[first_word] = firstword_count_dict[first_word]/float(count_sum)

print firstword_prob_dict

next_word_counts_dict = {}
for word_list in poem_lines:
    for i in range(len(word_list)):
        thisword = word_list[i]
        if i < len(word_list)-1:
            nextword = word_list[i+1]
        else:
            nextword = '\n'

        if thisword not in next_word_counts_dict:
            next_word_counts_dict[thisword] = {nextword:1}
        else:
            if nextword not in next_word_counts_dict[thisword]:
                next_word_counts_dict[thisword][nextword] = 1
            else:
                next_word_counts_dict[thisword][nextword] += 1

for thisword in next_word_counts_dict:
    count_sum = sum(next_word_counts_dict[thisword].values())
    for nextword in next_word_counts_dict[thisword]:
        old_next_word_count = next_word_counts_dict[thisword][nextword]
        next_word_counts_dict[thisword][nextword] = (float(next_word_counts_dict[thisword][nextword])/count_sum)

first_states = []
pp = []

for key in firstword_prob_dict:
    first_states.append(key)
    pp.append(firstword_prob_dict[key])
print first_states
print pp

#for i in range(len(next_word_counts_dict.items)):
#print next_word_counts_dict.items()

for x in range(1000):
    state = np.random.choice(first_states, p = pp)
    sentence = [state]
    for i in range(9):
        next_states = []
        p = []
        if state in next_word_counts_dict:
            for pair in next_word_counts_dict[state].items():
                next_states.append(pair[0])
                p.append(pair[1])
            state = np.random.choice(next_states, p = p)
            sentence.append(state)
    print ' '.join([w for w in sentence if w != '\n'])



#for word in next_word_counts_dict:
#    print next_word_counts_dict[word].items()
 #   np.random.choice(word, p=)
# word, ':', next_word_counts_dict[word]
print len(next_word_counts_dict)

output_file = open('poem_model.json', "w")
output_file.write(json.dumps(next_word_counts_dict))
output_file.close()

output_file2 = open('poem_model_firstword.json', "w")
output_file2.write(json.dumps(firstword_prob_dict))
output_file2.close()
