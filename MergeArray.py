class MergeArray:
    def merg_two_array(self,dict1,dict2):
        



        for key, value in dict2.items():
            if key in dict1:
                dict1[key] += value  # Sum the values if key exists in both dictionaries
            else:
                dict1[key] = value  # Add the key-value pair if key does not exist in dict1

        return dict1

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merge_array = MergeArray()

print(merge_array.merg_two_array(dict1,dict2))
