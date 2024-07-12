class MostFrequentWords:
    def __init__(self):
        pass
    
    def frequent_words(self, words: list, k: int):
        frequency = {}
        
        # Count the frequency of each word
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        
        
        
        # Sort the words first by frequency (descending), then by alphabetical order
        sorted_items = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))
        
        # Print the sorted frequency dictionary items
        print("Sorted dictionary items:", sorted_items)
        
        # Get the top k most frequent words
        result = [word for word, count in sorted_items[:k]]
        
        return result

# Example usage
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

most_frequent_words = MostFrequentWords()
result = most_frequent_words.frequent_words(words, k)

print("Most frequent words:", result)  # Output the k most frequent words
