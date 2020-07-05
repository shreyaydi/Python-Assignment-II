# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.
def findAnagram(wordArr):
    dict = {}
    for word in wordArr:
        key = ''.join(sorted(word))

        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key] = []
            dict[key].append(word)
        output = ""
        for key, value in dict.items():
            if len(value) > 1:
                output = output + ' '.join(value) + ' '

    return output


my_input = input('enter the paragraph')
wordArr = my_input.split(' ')
print(findAnagram(wordArr))
