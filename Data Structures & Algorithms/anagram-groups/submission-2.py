class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = {}

        for str in strs:
            key = "".join(sorted(str))

            if key in outputs:
                outputs[key].append(str)
            else:
                outputs[key] = [str]
        
        return list(outputs.values())