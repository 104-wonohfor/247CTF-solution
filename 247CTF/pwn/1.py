
problem = "What is the answer to 377 + 309?"
split = problem.split() # ['What', 'is', 'the', 'answer', 'to', '64', '+', '491']
split2 = split[7].split('?')



a = int(split[5])		# '64' - 64
b = int(split2[0].strip(''))
print(a+b)