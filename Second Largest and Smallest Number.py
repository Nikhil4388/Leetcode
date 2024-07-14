class SecondLargestNumber:
    def largest_number(self,arr1):
        sorted_arr=sorted(arr1,reverse=True)
        seocnd_largest= sorted_arr[1]
        seocnd_small = sorted_arr[-2]
 
        return seocnd_largest,seocnd_small

arr1=[1,2,3,4,5,6,7,8]
largestNumber= SecondLargestNumber()

print("2nd Largest: ",largestNumber.largest_number(arr1)[0])
print("2nd Smallest: ",largestNumber.largest_number(arr1)[1])
