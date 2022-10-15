import subprocess
import ast

subprocess.call('python3 interpreter.py>exit.txt', shell=True)
subprocess.call('scheme < input.txt>golden.txt', shell=True)
with open("golden.txt", "r") as golden:
	gold = golden.read()
l = gold.split('\n')
def rm(list,sub):
    text = str(list)
    new_text =''
    i=0
    last_i = 0
    while i <  len(text):
        if text[i:i+len(sub)] == sub:
            new_text += text[last_i:i]
            last_i=i+len(sub)
            i=i+len(sub)
        else:
            i+=1
    new_text += text[last_i:i]
    res = ast.literal_eval(new_text)
    return res
l = rm(l,"> ")
goldstr = "\n".join(l[3:])
with open("golden.txt", "w") as golden:
	golden.write(goldstr)
	
def test():
	with open('exit.txt', 'r') as e, open('golden.txt', 'r') as g,\
		open('result.txt', 'w') as r:
		golden_lst = [x for x in g.read().split("\n")]
		exit_lst = [x for x in e.read().split("\n")]
		for j in range(1, len(golden_lst), 3):
			if golden_lst[j] == exit_lst[j]:
				r.write(f"{golden_lst[j-1]} is passed\n")
			else:
				r.write(f"{golden_lst[j-1]} is failed\n")
			
                        
test()
