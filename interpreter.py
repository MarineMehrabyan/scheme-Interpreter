import re
import ast
import math
             
# Splits the file into words            
def parting(filename):
	char = ''
	with open(filename, "r") as file:
		all_words = []
		curr_word = []
		while True:
			if char != ';':
				char = file.read(1)
			if not char: return ["("]+all_words+[")"]
			if char == ";":
				temp = ''
				while temp != "\n":
					temp = file.read(1)
				char = file.read(1)
				if char == ';':
					continue
			if char != " " and char != "\r" and char != "\t" and char !="\n":
				if char =="(" or char == ")" or char =="[" or char == "]" :
					if len(curr_word) != 0:
						all_words.append("".join(curr_word))
						curr_word = []
					all_words.append(char)				
				elif  char == '"' :
					curr_word.append(char)
					char = file.read(1)
					while(char != '"'):
						curr_word.append(char)
						char = file.read(1)
					curr_word.append(char)
				else: curr_word.append(char)
			else:	
				if len(curr_word) != 0:
					all_words.append("".join(curr_word))
					curr_word = []
# Check parentheses 
def parentheses(expression):
	bastard_tup = tuple('{}[]')
	open_tup = tuple('(')
	close_tup = tuple(')')
	map = dict(zip(open_tup, close_tup))
	queue = []
	for i in expression:
		if i in open_tup: queue.append(map[i])
		elif i in close_tup:
			if not queue or i != queue.pop(): return 0
		elif i in bastard_tup: return 0
	if not queue: return 1
	else: return 0

def push(obj, l, depth):
        while depth:
                l = l[-1]
                depth -= 1
        l.append(obj)

#divides a list into blocks of actions that are themselves lists
def parse(s):
        if parentheses(s) == 0:
                print("ERROR: Problem with parentheses")
                exit()               	
        groups = []
        depth = 0
        for char in s:
                if char == '(':
                        push([], groups, depth)
                        depth += 1
                elif char == ')':
                        depth -= 1
                else:
                        push(char, groups, depth)
        if depth <= 0:
                return groups

#default functions of scheme, jumps to a new line
def newline(l):
	if l == ['newline']:
		print('\n',end = "")
		
#default functions of scheme, are several mathematical functions
def math_(l):
	l = change(l)
	if isinstance(l[1],list):
		return l
	try:
		eval(l[1])
		if l[0] == "sin": return math.sin(eval(l[1]))
		if l[0] == "cos": return math.cos(eval(l[1]))
		if l[0] == "tan": return math.tan(eval(l[1]))
		if l[0] == "asin": return math.asin(eval(l[1]))
		if l[0] == "acos": return math.acos(eval(l[1]))
		if l[0] == "atan": return math.atan(eval(l[1]))
		if l[0] == "sinh": return math.sinh(eval(l[1]))
		if l[0] == "cosh": return math.cosh(eval(l[1]))
		if l[0] == "tanh": return math.tanh(eval(l[1]))
		if l[0] == "asinh": return math.asinh(eval(l[1]))
		if l[0] == "acosh": return math.acosh(eval(l[1]))
		if l[0] == "atanh": return math.atanh(eval(l[1]))
		if l[0] == "sqrt": return math.sqrt(eval(l[1]))
		if l[0] == "exp": return math.exp(eval(l[1]))
		if l[0] == "log": return math.log(eval(l[1]))
		if l[0] == "abs": return math.fabs(eval(l[1]))		
		if l[0] == "floor": return math.floor(eval(l[1]))
		if l[0] == "round": return math.round(eval(l[1]))
		if l[0] == "truncate": return math.trunc(eval(l[1]))
		if l[0] == "ceiling": return math.ceil(eval(l[1]))
	except:
		print("\n\nError math in\t\t",l,"\n")
		exit()
# checks whether a string is a number or not, this function is used in other functions    
def is_number_or_float(sample_str):
    result = True
    if re.search("[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$", sample_str) is None:
        result = False
    return result
    
#default operators of scheme    +, -, *, /,
def quantity_operators(l):
	l = change(l)
	if len(l) <= 2:
		if l[0] == "+": return eval(l[1])
		elif l[0] == "-": return -eval(l[1])
		else: print("error"); exit()
	for i in l[1:]:
		if is_number_or_float(i) == False:
			print("ERROR: {} all arguments in the operator must be numbers".format(l[0]))
			exit()	
	if True:
		if l[0]=="+": value = 0; return  sum(eval(i) for i in l[1:])
		if l[0]=="-":
			value = eval(l[1])
			for i in l[2:]: value = value - eval(i)
			return value
		if l[0]=="*":
			value = 1
			for i in l[1:]: value *= eval(i)
			return value
		if l[0]=="/":
			value = eval(l[1])
			for i in l[2:]: value /= eval(i)
			return value

#default operators of scheme  =, >, <, >=, <=
def arithmetic_operators(l):
	l =change(l)
	res = "#t"
	for i in l[1:]:
		if is_number_or_float(i) == False:
			print("ERROR: {} all arguments in the operator must be numbers".format(l[0]),i)
			exit()
	if len(l) < 2:
		print("ERROR: {}  the number of all arguments in the operator must be  greater than 1".format(l[0]))
		exit()
	result = all(is_number_or_float(c) for c in l[1:])
	if result == "#f":
		raise NameError("key error")
	else:
		if l[0]=="<":
			for i in range(len(l[1:])-1):
				if not eval(l[1+i]) < eval(l[2+i]): res = "#f"
			return res
		if l[0]=="<=":
			for i in range(len(l[1:])-1):
				if not eval(l[1+i]) <= eval(l[2+i]): res = "#f"
			return res
		if l[0]==">":
			for i in range(len(l[1:])-1):
				if not eval(l[1+i]) > eval(l[2+i]): res = "#f"
			return res
		if l[0]==">=":
			for i in range(len(l[1:])-1):
				if not eval(l[1+i]) >= eval(l[2+i]): res = "#f"
			return res
		if l[0]=="=":
			for i in range(len(l[1:])-1):
				if not eval(l[1+i]) == eval(l[2+i]): res = "#f"
			return res

#default operators of scheme and,  or, not 		
def logical_operators(l):
	if len(l) == 1:
		if l[0]=="and": return "#t"
		if l[0]=="or": return "#f"
	if len(l) == 2 and l[0] == "not":
		return "#f" if l[1] == "#t" else "#t"
	elif l[0] == "not" and len(l) != 2:
		print("ERROR: the number of all arguments in the not operator must be 1")
		exit()
	else:
		if l[0]=="and":
			for i in l[1:]:
				if i == "#f" or i == '0': return "#f"
				else: res = i
			return res
		if l[0]=="or":
			for i in l[1:]:
				if i != "#f" and i != '0': return i
				else: res = "#f"
			return res

#default functions of scheme,  If/else statement
def if_statement(l):
	if len(l) == 4:
 		if calculate_expression(l[1])!='#f' and calculate_expression(l[1])!='0':
 			return l[2]
 		else:
 			return l[3]
	elif len(l) == 3:
 		if calculate_expression(l[1])!=('#f' or '0'):
 			return l[2]	
 		else:
 			exit()
	else:
 		print("Error ։ Syntax error in if  statement")
 		exit()
 		
#default functions of scheme, returns the mod of 2 numbers
def remainder(l):
	if len(l) != 3:
		print("ERROR: {}  the number of all arguments in the operator must be  2".format(l[0]))
		exit()
	l = change(l)
	if isinstance(eval(l[1]),int) and isinstance(eval(l[2]),int):
		return eval(l[1])%eval(l[2])
	else:
		print("ERROR: {}  the number of all arguments  must be type of int".format(l[0]))
		exit()

# The change function receives a list, there may be unknown values ​​in the list,
# the function checks if there is a created variables, places it instead of the list, 
# and also performs calculations in some cases
def change(l):
	res = str(l)
	if l[0] == 'list':
		for i in l[1:]:
			if i in my_var:
				res = res.replace(f"'{str(i)}'",str(my_var[i]))
		return ast.literal_eval(res)
	for i in range(1, len(l)):
		if not isinstance(l[i], list) and l[i] in my_var:
			if isinstance(my_var[l[i]],list):
				res = res.replace(f"'{str(l[i])}'",str(compile(my_var[l[i]])))
			res = res.replace(f"'{str(l[i])}'",f"'{str(my_var[l[i]])}'")
		elif isinstance(l[i], list):
			temp = str(l[i])
			print("l]i\=", l[i])
			for j in l[i]:
				print("j=", j)
				if j in my_var:
					if isinstance(my_var[j],list):
						temp = temp.replace(f"'{str(j)}'",str(compile(my_var[j])))
					temp = temp.replace(f"'{str(j)}'",f"'{str(my_var[j])}'")
			res = res.replace(f"{str(l[i])}",f"'{str(calculate_expression(ast.literal_eval(temp)))}'")
	return ast.literal_eval(res)
		

#in scheme is the list function
def list_(l):
	s = "("
	for i in l[1:-1]:
		if not i in my_var and is_number_or_float(i)==False and i[0] != '"' and i[-1] != '"' and i[0] != '(' :
			print("ERROR։ {} variable is not defined".format(i))
			exit()
		if i in my_var:
			s+=str(calculate_expression(my_var[i]))+' '
		else: s+=i+" "
	if l[-1] in my_var:
		s+=str(calculate_expression(my_var[l[-1]]+')'))
	else: s+=l[-1]+')'
	return s
	
#in scheme is the define-syntax function		
def def_syntax(l):
	if len(l) != 3:
		print("ERROR։ Syntax error in {} function".format(l[0]))
		exit()
	else:
		my_def_syntax[l[1]]=l[2]
		return l[2]

#in scheme it is the syntax-rules function		
def syntax_rules(l):
	res = ["define"]
	if len(l) != 3:
		print("ERROR։ Syntax error in {} function".format(l[0]))
		exit()
	else:
		res.append(l[2][0])
		res.append(l[2][1])
		define(res)
		
#Check syntax it is used in the run function
def check_syntax(s,a,b):
	for i in s:
		if i in a and i in b:
			if a.index(i) != b.index(i):
				return False
		else:
			return False
	return True

#rm is used in the clean function
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

# clean receives a list in which there may be None values ​​during the recursion,
# the function deletes them, the list brings the correct look
def clean(k):
    if isinstance(k,str):
        return [k]
    a = rm(rm(k,"'None',"),"'None'")
    temp=[]
    for i in range(len(a)):
        if isinstance(a[i], list) and len(a[i])==1 and isinstance(a[i][0], list):
            while isinstance(a[i][0], list):
                if len(a[i][0]) == 0:
                    a[i] = []
                    break
                a[i] = a[i][0]
        temp.append(a[i])
    return list(filter(None, temp))

#in scheme it is the display function
def display(l):
	if len(l) != 2:
		print("ERROR: {}  the number of all arguments in the operator must be 1".format(l[0]))
		exit()
	elif l[1] in my_identify:
		print("ERROR։ In {} function passed {} keyword  as argument ".format(l[0], l[1]))
		exit()
	elif l[1] in my_var:
		if isinstance(my_var[l[1]],list):
			a = []
			a.append("display")
			a.append(my_var[l[1]])
			return a
		else:
			print(my_var[l[1]],end="")
	else:
		try:
			float(l[1])
			print(l[1],end = "")
		except:
			if l[1][0] == '"' and l[1][-1] == '"':
				print(l[1][1:-1],end = "")
			elif l[1][0] == '(' and l[1][-1] == ')':
				print(l[1],end = "")
			else:
				print(" ERROR: in display  function used non-existent  ",l[1]," variable!")

#in scheme it is the define function
def define(l):
	if len(l) == 2:
		my_var[l[1]] = ""
		return
	if len(l)!=3:
		print("ERROR։ Syntax error in  {} function".format(l[1][0]))
		exit()	
	if isinstance(l[2], list) and l[2][0] == "list":
		l[2] = change(l[2])
		my_var[l[1]] = list_(l[2])
	if  not isinstance(l[1] ,list):
		my_var[l[1]] = l[2]
		my_var[l[1]] = calculate_expression(my_var[l[1]])
	else:
		args = l[1][1:]
		body = l[2:]
		my_func[l[1][0]]=[args,body]
		
#The run function receives a list, which is actually a dictionary, 
#where the function name, arguments and body are stored,
# run performs the work of that function			
def run(func):
	if func[0] in my_def_syntax:
		if check_syntax(my_def_syntax[func[0]][1],my_def_syntax[func[0]][2][0],func):
			index = 1
			temp = str(my_func.get(func[0])[1][0])
			for j in my_func.get(func[0])[0]:
				if isinstance(func[index],list):
					temp = temp.replace(f"'{j}'", f"{func[index]}")	
				else:
					temp = temp.replace(f"'{j}'", f"'{func[index]}'")
				index += 1
			temp = ast.literal_eval(temp)
			return temp
		else:
			print("ERROR։ Syntax error in  {} function".format(func[0]))
			exit()
	else:
		if not func[0] in my_func:
			print("ERROR։ Function named  {} is  not defined".format(func[0]))
			exit()
		if len(func[1:]) != len(my_func[func[0]][0]):
			print(f"ERROR։ In {func[0]} funcion instead of passing argument {len(my_func[func[0]][0])}, was passed {len(func[1:])}")
			exit()
		index = 1
		temp = str(my_func.get(func[0])[1][0])
		for j in my_func.get(func[0])[0]:
			temp = temp.replace(f"'{j}'", f"'{func[index]}'")
			index += 1
		temp = ast.literal_eval(temp)
		return temp
#in scheme it is the begin function
def begin(l):
	a = []
	if len(l) > 2: 
		a.append(l[1])
		a.append(["begin"])
		for i in l[2:]:
			a[1].append(i)
	else:
		a = l[1]
	return a

#in scheme it is the length function	
def length(l):
	if len(l) !=2:
		print(f"ERROR։ Instead of passing 1 argument to the  length  function, were passed {len(l)}")
		exit()
	if l[1][0] == "(":
		return len(l[1].split())
	elif l[1] in my_var and my_var[l[1]][0] == '(':
		return len(my_var[l[1]].split())
	else:
		print("ERROR։ Syntax error in  length function")
		exit()
#in scheme it is the car function
def car(l):
	if len(l) !=2:
		print(f"ERROR։ Instead of passing 1 argument to the  car  function, were passed  {len(l)}")
		exit()
	if l[1][0] == "(":
		temp = l[1][1:-1]
		return temp.split()[0]
	elif l[1] in my_var and my_var[l[1]][0] == '(':
		return my_var[l[1]].split()[0][1:]
	elif len(l)==2:
		if l[1] in my_var:
			return my_var[l[1]]
		return l[1]
	else:
		print("ERROR։ Syntax error in  car function")
		exit()
	
#in scheme it is the cdr function
def cdr(l):
	if len(l) !=2:
		print(f"ՍERROR։ Instead of passing 1 argument to the  cdr  function, were passed  {len(l)}")
		exit()
	if l[1][0] == "(":
		return "("+" ".join(l[1].split()[1:])
	elif l[1] in my_var and my_var[l[1]][0] == '(':
		return "("+" ".join(my_var[l[1]].split()[1:])
	
	elif len(l)==2:
		if l[1] in my_var:
			return my_var[l[1]]
		return l[1]
	else:
		#print(l)
		print("ERROR։ Syntax error in  cdr function")
		exit()
		
#in scheme it is the lambda function
def lambda_(l):
	l[0] = 'define'
	l[1].insert(0,'arg')
	define(l)
	return 'arg'

my_def_syntax={}   
my_func = {}
func_call = {"?" : run}
my_var = {"#t":"#t","#f":"#f"}

#in scheme it is the let function
def let(l):
	if len(l)==3:
		for i in l[1]:
			my_var[i[0]]=calculate_expression(i[1])
		calculate_expression(l[2])
	elif len(l)==4:
		args = []
		val = []
		for i in l[2]:
			args.append(i[0])
			val.append(i[1])
		body = l[3]
		my_func[l[1]]=[args,[body]]
		val.insert(0,l[1])
		return val
	else:
		print("ERROR: Syntax error in let  function")
		exit()
			
#this dictionary is stored so that when it sees the key values ​​in the file, it calls the given function
my_identify= { "display" :  display, "+" : quantity_operators, "-" : quantity_operators,"*" : quantity_operators,\
  "/" : quantity_operators, ">" : arithmetic_operators, ">=" : arithmetic_operators, "<=" : arithmetic_operators,\
   "<" : arithmetic_operators, "=" : arithmetic_operators, "and" :  logical_operators, "or" : logical_operators, \
   "not" : logical_operators, "if" : if_statement,"define" : define,"begin" : begin , "remainder" : remainder,\
    "define-syntax" : def_syntax,"syntax-rules" : syntax_rules, "sin" : math_, "cos" : math_, "tan" : math_,\
     "asin" : math_, "acos" : math_, "atan" : math_, "sinh" : math_, "cosh" : math_, "tanh" : math_,\
      "asinh" : math_, "acosh" : math_, "atanh" : math_, "sqrt" : math_, "floor" : math_, "ceiling" : math_,\
       "truncate" : math_, "round" : math_, "abs" : math_, "exp" : math_, "log" : math_,'newline' : newline, \
       "lambda" : lambda_, "length" : length, "car" : car, "cdr" : cdr, "list" : list_, "let" : let, "set!" : define}
#these are separated because the implementation is done differently
uni_tokens=["define","if",'begin', "define-syntax", "syntax-rules", "let", "for"]

# current_action is a recursive function that takes a list and finds the first action to be executed, 
# this is used in the compile function
def current_action(expr):
	if len(expr)==1 and isinstance(expr, list) and len(expr[0])==1  and isinstance(expr[0], list):
		if expr[0][0]  in my_var:
			return compile(my_var[expr[0][0]])
	for i in range(len(expr)):
		if expr[i]== []:
			continue
		if not isinstance(expr[i],list) and (expr[i] in uni_tokens or expr[i] in my_var):
			return expr
		elif isinstance(expr[i],list) and not expr[i][0] in uni_tokens :
			return current_action(expr[i])
		elif isinstance(expr[i],list) and expr[i][0] in uni_tokens:
			return expr[i]
		else:
			if len(expr)>1 and isinstance(expr[1],list) and isinstance(expr[1][0],list):
				return expr[1][0]
			if i == len(expr)-1:
				return expr

result = parse(parting("input.txt"))[0]

#compile is the main function of the program that performs the current operations
# by calling the corresponding functions
def compile(result):
	if len(result)==1 and isinstance(result[0], str) and result[0] !="newline" and result[0] != "list":
		return
	curr_list = current_action(result)
	temp = curr_list
	if curr_list == ['None']: return
	if isinstance(curr_list,list) and isinstance(curr_list[0],list):
		while(isinstance(curr_list[0],list)):
			curr_list = curr_list[0]
	if curr_list[0] in my_identify or curr_list[0] in my_func:
		if curr_list[0] in my_identify:
			value = my_identify[curr_list[0]](curr_list)
		else :
			value = func_call['?'](curr_list)
		res = str(result)
		if not isinstance(value,list):
			res = res.replace(str(curr_list),f"'{value}'",1)
		else:
			res = res.replace(str(curr_list),str(value),1)
		result=ast.literal_eval(res)
		if len(result)==1:
			result = result[0]
		if result[0] == 'let':
			compile(result)
		compile(clean(result))
	else:
		res = str(result)
		if curr_list[0][0] == '(':
			res = res.replace(str([temp]),f"'{curr_list[0]}'",1)
		else:
			res = res.replace(str(temp),f"'{curr_list[0]}'",1)
		result=ast.literal_eval(res)
		compile(clean(result))

def helper(curr_list):
	if curr_list[0] in my_identify or curr_list[0] in my_func:
		if curr_list[0] in my_identify:
			return my_identify[curr_list[0]](curr_list)
		else :
			return func_call['?'](curr_list)
	
#in some cases, it is necessary to calculate the expressions,
# the function calculate_expression receives a list, calculates the value of the expression
def calculate_expression(l):
	while not isinstance(l, str):
		first_op = (current_action(l))
		val = helper(first_op)
		if not isinstance(val,list):
			l = ast.literal_eval(str(l).replace(str(first_op), f"'{val}'",1))
		else:
			l = ast.literal_eval(str(l).replace(str(first_op),str(val),1))
	return l
compile(result)
