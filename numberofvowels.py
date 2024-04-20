# write a program that calculate the number of vowels and  count of each individual vowel 'a','e','i','o','u' in the string"Huvi Geek Network private Limited"

# number of vowels in the string

string="Guvi Geeks Network Private Limited"
count=0

for no_of_vowels in string:
    if no_of_vowels.lower() in ['a','e','i','o','u']:
        count+=1
        result=count

print(f"The Number of Vowels are {result}")

# count of each vowels in the string

string=string.casefold()
vowels="aeiou"
vowels_str={}.fromkeys(vowels,0)

for character in string:
    if character in vowels:
        vowels_str[character]+=1

print("Each Individual vowels in the input string")

for each_vowels in vowels_str:
    print(each_vowels,"",vowels_str[each_vowels])