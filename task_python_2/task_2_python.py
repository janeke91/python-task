# TASK1
# nums = [int(i) for i in input().split()]
# print(*[num*2 for num in nums if num % 2 == 0])
#
# TASK4
# words = input().split()
# print(max(words, key=len))
#  TASK4
# s = input()
# best = cur = s[0]
# for i in range(1, len(s)):
#     if s[i] > s[i-1]:
#         cur += s[i]
#     else:
#         if len(cur) > len(best):
#             best = cur
#         cur = s[i]
# if len(cur) > len(best):
#     best = cur
# print(best)
# TASK3
# words = input().split()
# freq = {}
# for word in words:
#     if word not in freq:
#         freq[word] = 0
#     freq[word] += 1
# for word in freq:
#     print(word + ": " + str(freq[word]))
# TASK5
# s = input()
# digits = ""
# for ch in s:
#     if ch.isdigit():
#         digits += ch
# print(int(digits) if digits else 0)
