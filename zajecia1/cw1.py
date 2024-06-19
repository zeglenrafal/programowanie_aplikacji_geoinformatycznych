import json
import urllib.request
import string

with open('teksty.json') as user_file:
 dane=json.load(user_file)

tekst_polaczony = ""
for tekst in dane["teksty"]:
    tekst_polaczony += tekst[next(iter(tekst))]

tekst_polaczony = tekst_polaczony.lower()

wyrazy = tekst_polaczony.split()
wyrazy = [wyraz.strip(string.punctuation) for wyraz in wyrazy]
wyrazy = [wyraz[:-1] + wyraz[-1].upper() for wyraz in wyrazy]
wyrazy = [wyraz for wyraz in wyrazy if 'a' in wyraz or 'A' in wyraz]

unique_words = set(wyrazy)
words_count = {wyraz: wyrazy.count(wyraz) for wyraz in unique_words}

with open("wyniki.json", "w") as file:
    json.dump({"tekst_polaczony": tekst_polaczony,
               "unique_words": list(unique_words),
               "words_count": words_count}, file, indent=4)