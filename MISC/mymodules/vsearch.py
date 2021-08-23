def search4vowels(phrase:str) -> set:
    """this function reads a mentioned phrase and prints all unique vowels that are present in the phrase"""    
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
