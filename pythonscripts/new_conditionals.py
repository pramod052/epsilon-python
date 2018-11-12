## conditionals
s = "1asfdkjsdfdfdklk"
s = input("enter string:")

vowel = "aeiou"
for i in s:
	print(i)
i = 0

#while(i < len(s)):
#	print(s[i])
#	if (s[i] in vowel):
#		print('got a vowel"' + s[i] + '" breaking now')
#		break
#	i += 1

while(i < len(s)):
	if (s[i] in vowel):
		i += 1
		continue
	print(s[i])
	i += 1
vowel = "aeiou"

if (s[0] in vowel):
	print(s[0])
	print("First character is vowel")
	print("Still in First if block")
elif(s[0].isdigit()):
	print("First character is digit")
else:
	print("1st character is not vowel")
	print("Still in first else block")


a = "m"
a = input("Enter value for variable a: ")

if (a == "z"):
	print("a is z")
	print("still in second if block")
elif (a =="m"):
	print("a is m")
	print("still in second elif block")
print("out of if block")
