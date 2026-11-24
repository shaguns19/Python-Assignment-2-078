ch = input("Enter a single alphabet: ").lower()
if len(ch) != 1 or not ch.isalpha(): print("Please enter one alphabet.")
elif ch in "aeiou": print("Vowel")
else: print("Consonant")
