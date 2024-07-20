class RemoveDuplicate:
    def remove_duplicate(self,my_list):
        seen =[]
        for item in my_list:
            if not item in seen:
                seen.append(item)
        return seen


my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]
remove_duplicate= RemoveDuplicate()


print(remove_duplicate.remove_duplicate(my_list))
