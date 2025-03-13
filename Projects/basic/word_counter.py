def word_counter(user_input):
    '''split() changes into list, len to count the number of elements in the list'''
    return len(user_input.split())


sentence = input('enter something: ')
print(word_counter(sentence))
