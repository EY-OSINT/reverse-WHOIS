import os 
from pathlib import Path
f=open('C:/Users/aicha/PycharmProjects/test_angular_flask/files/input.txt').read()
f2=open('C:/Users/aicha/PycharmProjects/test_angular_flask/files/output.txt','w')


filesize = os.path.getsize("C:/Users/aicha/PycharmProjects/test_angular_flask/files/output.txt")
if filesize == 0:
    f2.write("["+"\n")

try:    
    for i in f.split('\n')[:-1]:
        domain = i.split(' ')[0] 
        print(domain)
        f2.write("{"+"\n")
        f2.write('"domain" :' + '"'+ domain + '"' +","+"\n")
        f2.write("}"+"\n")
except:
	print("an error has occured ")

f2.write("]"+"\n")
f2 = open("C:/Users/aicha/PycharmProjects/test_angular_flask/files/output.txt", "r")
print(f2.read())	
f2.close()
p=Path('C:/Users/aicha/PycharmProjects/test_angular_flask/files/output.txt')
p.rename(p.with_suffix('.json'))	      

