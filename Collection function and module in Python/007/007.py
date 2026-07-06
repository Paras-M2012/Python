#1. Character Frequency Counter
text = input("Enter a string: ")

alph_count = {}

for alph in text:
    if alph in alph_count:
        alph_count[alph] += 1
    else:
        alph_count[alph] = 1

print(alph_count)


#2. Word Frequency from a Review (Multi-line String)
review = """
Naroda orthopedic Hospital is provided mutliple services?.
There are two, Orthopedic Surgeon in Hospital.
One is The / Gold Medalist Orthopedic, Surgeon.
There is Robotic Surgery Services also available.

"""

cleaned = review.lower()
for punct in ".,!?\n":
    cleaned = cleaned.replace(punct, " ")

words = cleaned.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


#3. word_freq_dict() Function
def word_freq_dict(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"
result = word_freq_dict(text)
print(result)


#4. Word Frequency — Ignoring Stopwords

def word_freq_dict(text):
    stopwords = ['the', 'and', 'in', 'of', 'a', 'to', 'is']
    
    
    cleaned = text.lower()
    for punct in ".,!?":
        cleaned = cleaned.replace(punct, "")
    
    words = cleaned.split()
    
    freq = {}
    for word in words:
        if word not in stopwords:
            freq[word] = freq.get(word, 0) + 1
    return freq

text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"
result = word_freq_dict(text)
print(result)


#5. char_count_dict() Function — Sorted Output

def digit_count_dict(text):
    freq = {}
    for digit in text:
        freq[char] = freq.get(digit, 0) + 1
    return freq

text = input("Enter a string: ")
result = digit_count_dict(text)

sorted_result = dict(sorted(result.items()))

print(sorted_result)
