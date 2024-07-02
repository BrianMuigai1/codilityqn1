import random
import string

def generate_random_word(length):
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)

    word = []
    letter_count = {}
    for _ in range(length):
        if len(letters) > 0:
            letter = letters.pop()
        else:
            letter = random.choice(list(letter_count.keys()))  
            letter_count[letter] += 1  
        word.append(letter)
        letter_count[letter] = letter_count.get(letter, 0) + 1

    return ''.join(word)

def solution(N):
  if N < 1 or N > 200000:
    print("Jaba limpueza")
    return

  word = generate_random_word(N)
  print(word)

solution(27)
