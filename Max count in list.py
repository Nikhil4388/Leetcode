class MaxNumber:
    def max_number(self,my_list):
        my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]
        count_item = {}
        for item in my_list:
            if item in count_item:
                count_item[item]+=1
            else:
                count_item[item]=1
        sorted_items= sorted(count_item.items(),key=lambda item:item)

        return sorted_items[0]

my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]

max_number =MaxNumber()

print(f"Max number : {max_number.max_number(my_list)[0]} count: {max_number.max_number(
#############################################################################################################


from collections import Counter

# Example list
my_list = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat', 'fish', 'dog', 'dog', 'cat', 'fish', 'fish', 'bird']

# Step 1: Create a Counter object
counter = Counter(my_list)

# Step 2: Use the most_common() method to get the most common elements
most_common_elements = counter.most_common()

print(most_common_elements) 
                                                                 
