# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# True Anagram
def find_anagram():
    # [assignment] Add your code here
    word1 = input('type a word \n');
    word2 = input('type another word \n');
    sorted_word1 = sorted(word1);
    sorted_word2 =sorted(word2);
    if(sorted_word1 == sorted_word2):
        return True

    else:
        return False
print(find_anagram()) 


#False Anagram
def find_anagram():
    word3 = input('type a word: \n')
    word4 = input('type another word: \n')
    sorted_word3 = sorted(word3)
    sorted_word4 = sorted(word4)
    if(len(word3) == len(word4)):
        if(sorted_word3 == sorted_word4):  
            return True
    else:
        return False
print(find_anagram())