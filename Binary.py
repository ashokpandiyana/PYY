# # Decimal To Binaty
# print(bin(339).replace('0b', ''))


# def decimalToBinary(ip_val):
#     if ip_val >= 1:
#         # recursive function call
#         decimalToBinary(ip_val // 2)

#     # printing remainder from each function call
#     print(ip_val % 2, end='')


# decimalToBinary(24)
nums = [1, 2, 1, 1, 2, 5]
result = nums[0]
for i in range(1, len(nums)):
    result ^= nums[i]
print(result)
