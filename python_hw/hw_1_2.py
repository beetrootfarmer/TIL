score = {
'python': 80,
'django': 89,
'web': 83,
}
# 1.
score['algorithm'] = 90

# 2.
score.update({'python' : 85})

# 3.
print(sum(score.value())/len(score.value())