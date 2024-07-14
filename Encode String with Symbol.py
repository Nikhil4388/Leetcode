class EncodeString:
    def find_longest_prefix(self, s: str) -> str:
        n = len(s)
        for i in range(1, n // 2 + 1):
            prefix = s[:i]
            if s[i:].startswith(prefix):
                return prefix
        return ""
    
    def encode_with_repeating_prefix(self, s: str, rep_string: str) -> str:
        encode_s = s[:len(rep_string)]
        pos = len(rep_string)
        n = len(s)
        
        while pos < n:
            if s[pos:pos+len(rep_string)] == rep_string:
                encode_s += "*"
                pos += len(rep_string)
            else:
                encode_s += s[pos]
                pos += 1
        
        return encode_s
    
    def encode_string(self, s: str) -> str:
        rep_string = self.find_longest_prefix(s)
        if not rep_string:
            return s
        return self.encode_with_repeating_prefix(s, rep_string)

# Test the function
s = 'abababaaa'
encode = EncodeString()
encoded_string = encode.encode_string(s)
print(f"Encoded string: {encoded_string}")

# Additional test cases
test_cases = {
    "ababab": "ab*ab*",
    "abcdabcd": "abcd*",
    "abcabcabc": "abc*abc*",
    "abcde": "abcde",  # No repeating prefix
    "aabbaabb": "aabb*",
    "aaaaaa": "a*a*a*a*a",
    "aabcaabc": "aabc*aabc", # Handling prefix within the word itself 
    "xyzxyzxyz": "xyz*xyz*",
    "zzzzzz": "z*z*z*z*z", # Single character repeating
    "mississippi": "mississippi", # Non-repeating string
}

for word, expected in test_cases.items():
    result = encode.encode_string(word)
    print(f"Tested word: {word}, Encoded string: {result}, Expected: {expected}")
