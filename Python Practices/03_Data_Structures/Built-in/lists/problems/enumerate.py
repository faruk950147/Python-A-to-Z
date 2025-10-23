sports = ['cricket', 'football', 'basketball', 'tennis']
print(list(sports))

sports_enumerate = enumerate(sports)
print(sports_enumerate)
for i, sport in enumerate(sports):
    print(i, sport)

# Output:
# 0 cricket
# 1 football
# 2 basketball
# 3 tennis
