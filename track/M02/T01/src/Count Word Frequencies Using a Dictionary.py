n = int(input())
word_frequemcy = {}

for i in range(n):
    word = input().strip()

    word_frequency[word] = word_frequency.get(word, 0) + 1

for word in sorted(word_frequency.keys()):
    print(f"{word}: {word_frequency[word]}")