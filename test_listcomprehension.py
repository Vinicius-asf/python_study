test_string = '1234567890'
n = 2

arr_test = [test_string[x:x+2] for x in range(0,len(test_string),n)]
print(arr_test)