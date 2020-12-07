from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def process_str(x, i) :
	list_type = []
	for a in x :
		if a.isalpha() :
			list_type.append(2)
		if a.isnumeric() :
			list_type.append(1) 
		if a in ["+", "-"] :
			list_type.append(0)
	string = ""
	for b in range(len(list_type)-1) :
		if list_type[b] ==1 and list_type[b+1] == 2 :
			string += x[b] + "*"
		elif list_type[b] == 2 and list_type[b+1] == 2 :
			string += x[b] + "*" 
		elif list_type[b] == 2 and list_type[b+1] == 1 :
			string += x[b] + "**"
		else :
			string += x[b]
	string += x[-1]
			
	if i == 1:
		if string[0] == "+" :
			string = "-" + string[1:]
		else :
			string = "+" + string[1:]
	return string
		

def eq_solver(equation) :
	list_eq = []
	for eq in equation :
		string = ""
		#left : 0 , right : 1
		for i, side in enumerate(eq.split("=")) :
			if side[0] not in ["+", "-"] :
				side = "+" + side
			pos_sign = [i for i, char in enumerate(side) if char in ["+","-"]]
			pos_sign.append(len(side))
			
			for j in range(len(pos_sign)-1) :
				string += process_str(side[pos_sign[j] : pos_sign[j+1]], i)
		list_eq.append(string)
	
	result = solve([parse_expr(i) for i in list_eq]) 
	return result
	
	
