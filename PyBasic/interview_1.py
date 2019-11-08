import re

text = "AS7G123m (d)F77k"
nums = re.findall(r'(\d+)',text)
nums_double = [2*int(i) for i in nums]
print(nums)
the_str = []
for i in nums:
    the_str.append(text.split(i,1)[0])
    text = text.split(i,1)[1]

result = ""
for i in range(len(nums)):
    result += the_str[i] + str(nums_double[i])

result += text
print(result)