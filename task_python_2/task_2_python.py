# TASK1
# nums = [int(i) for i in input().split()]
# print(*[num*2 for num in nums if num % 2 == 0])
#
# TASK4
# words = input().split()
# print(max(words, key=len))
# 
# TASK2
# s = input()
# substrings = []
# start = 0
# for i in range(1, len(s)):
    # if s[i] <= s[i-1]:
        # substrings.append(s[start:i])
        # start = i
# substrings.append(s[start:])
# print(max(substrings, key=len))
# 
#TASK3
# s = input().split()
# for word in dict.fromkeys(s):
#     print(f"{word}: {s.count(word)}")
# 
# TASK5
# s = input()
# print("".join(n for n in s if n.isdigit()) or 0)
