import re

pattern = r"\s+"  
string = "This is a All Regular Expression which one we are using with spaces."
result = re.split(pattern, string)

print(result)  
