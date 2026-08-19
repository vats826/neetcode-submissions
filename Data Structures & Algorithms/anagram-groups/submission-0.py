class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for words in strs:
            char_frequency = [0]*26
            for char in words:
                char_frequency[ord(char) - ord('a')]+=1

            char_frequency_as_key = tuple(char_frequency)
            if char_frequency_as_key not in anagram_groups:
                anagram_groups[char_frequency_as_key] = []
            anagram_groups[char_frequency_as_key].append(words)

        return list(anagram_groups.values())