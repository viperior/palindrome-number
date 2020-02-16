class Solution:
    def isPalindrome(self, x: int) -> bool:
        value_string = str(x)
        value_string_reversed = value_string[::-1]
        
        return value_string == value_string_reversed

tests = [
    [0, True],
    [1, True],
    [-1, False],
    [10, False],
    [11, True],
    [-11, False],
    [54345, True],
    [54346, False]
]

pass_count = 0
fail_count = 0

for test_number, test in enumerate(tests):
    print('Test #' + str(test_number) + ':')
    print('Input integer: ' + str(test[0]))
    print('Expected result: ' + str(test[1]))
    actual_result = Solution().isPalindrome(test[0])
    print('Actual result: ' + str(actual_result))
    test_result = test[1] == actual_result
    
    if test_result:
        test_result_text = 'PASS'
        pass_count += 1
    else:
        test_result_text = 'FALSE'
        fail_count += 1
    
    print('Test result: ' + test_result_text)
    
print('\nTests passed: ' + str(pass_count))
print('Tests failed: ' + str(fail_count))
