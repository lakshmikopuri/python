#Ransom Note
#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True
        
