class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sorted_str = "".join(sorted(word))

            if sorted_str in anagrams:
                anagrams[sorted_str].append(word)
            else:
                anagrams[sorted_str] = [word]

        return list(anagrams.values())