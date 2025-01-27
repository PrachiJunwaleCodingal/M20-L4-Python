#Arrays
import array as arr

a= arr.array('i', [12,34,56,23,12,78,45])
print("Array: "+str(a))

print("Number of occurrences(Num:12): "+str(a.count(12)))

a.reverse()
print("Reverse array:", str(a))
