s = input(" ")
print(s[:s.find(" ")])
print(s[s.rfind(' ')+1:])
print(s[s.find(" ")+1:s.rfind(" ")].replace("n",("N")))
print(s[:s.find(" ")+1] + s[s.find(" ")+1:s.rfind(" ")].replace("n",("N")) +s[s.rfind(' '):])



