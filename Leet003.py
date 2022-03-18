def lengthOfLongestSubstring(self, s: str) -> int:
    last_idx, total = 0, 0
    letters = {} 
    for x in range(len(s)):
        if s[x] in letters:
            print(letters[s[x]])
            last_idx = max(letters[s[x]], last_idx)
        total = max(total, x - last_idx + 1)
        letters[s[x]] = x + 1
    return total