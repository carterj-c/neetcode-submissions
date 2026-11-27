class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # I would like to just do a simple comparason of sets when equal return true.
       # However I think there's an edge case that does not work. When you have a word
       # with more chars that are duplicated but of unequal numbers this would not work.
       # I know that I could just sort the lists and compare but that is too easy.

       return sorted(list(s)) == sorted(list(t))