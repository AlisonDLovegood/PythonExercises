from msilib.schema import Directory
import os

way = os.path.basename("/Users\Aliso\Desktop\delnatur\s1.PNG")
split = way.split(".")
print("The extension is: " + repr(split[-1]))
