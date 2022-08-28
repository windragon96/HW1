class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strings_length = []
        for string in strs:
            strings_length.append(len(string))
        shortest_string_length = min(strings_length)

        common_prefix = []
        for i in range(shortest_string_length):
            index = 0
            common_prefix.append(strs[index][i])
            while index < len(strs) - 1:
                if strs[index][i] == strs[index + 1][i]:
                    index += 1
                else:
                    common_prefix.pop()
                    return ''.join(common_prefix)

        return ''.join(common_prefix)
