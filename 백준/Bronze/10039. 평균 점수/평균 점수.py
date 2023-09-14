score = []
for i in range(5):
    score.append(int(input()))
score = [40 if i<40 else i for i in score]

print(int(sum(score)/len(score)))