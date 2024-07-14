



class NonRepeatingString:
    def first_non_repeating(self,s:str):
        
        repeat_s={}
        for char in s:
            if char in repeat_s:
                repeat_s[char] +=1
            else:
                repeat_s[char] =1
        print(repeat_s)

        for char in s:
            if repeat_s[char]==1:
                return char

    def first_repeating(self, s):
        char_count = {}
        for char in s:
            if char in char_count:
                return char  
            else:
                char_count[char] = 1
        
        return None


s='swiss'


non_repeating_string = NonRepeatingString()

print(f"First non-repeating character: {non_repeating_string.first_non_repeating(s)}")
print(f"First repeating character: {non_repeating_string.first_repeating(s)}")
