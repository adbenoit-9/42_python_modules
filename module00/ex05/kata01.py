languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

str = 'Python was created by {Python}\n'
str += 'Ruby was created by {Ruby}\n'
str += 'PHP was created by {PHP}'
print(str.format(**languages))
