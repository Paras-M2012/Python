import re 

pattern = r"\d+" 
string = "I have 12 Toys, 15 Cars, and 100 Blocks."
result = re.findall(pattern, string)

print(result) 
