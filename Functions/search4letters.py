def search4vowels(phrase:str) -> set:
    """this function returns uniqoe vovels present in entered phrase"""
    vowels = set('aeiou')
    return set(phrase).intersection(vowels)

def search4letters(phrase:str, letters:str) -> set:
    """this function reads a mentioned phrase and letters that need to be found, and then prints all unique letters that are present in the phrase"""    
    return set(letters).intersection(set(phrase))
   
