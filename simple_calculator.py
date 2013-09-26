import sys

minus = "-"
plus  = "+"
divis = "/"
multi = "*"
power = "^"
unary = "-"
br_op = "("
br_cl = ")"

operations = [power, divis, multi, minus, plus]
digits = ['1','2','3','4','5','6','7','8','9','0','.']

def find_close_pos(the_string):
	open_count = 0
	close_count = 0
	for i in range(len(the_string)):
		if the_string[i] == br_op :
			open_count = open_count + 1
		if the_string[i] == br_cl :
			close_count = close_count + 1
			if close_count == open_count:
				return i

def parse(the_string):
	parsed_string = []
	number = ""
	for i in range(len(the_string)):
		if the_string[i]  == "-" and i == 0: ### string = "-2 + blablabla"
			number += the_string[i]
		elif the_string[i] in operations and the_string[i-1] not in operations: ### ^
			parsed_string.append(float(number))
			parsed_string.append(the_string[i])
			number = ""
		elif the_string[i]  == "-" and the_string[i-1] in operations: ### ^-
			number += the_string[i]
		elif the_string[i] in digits: ### 2
			number += the_string[i]
	parsed_string.append(float(number))
	return parsed_string

def single_operation(parsed_string):
	if parsed_string[1] == "+":
		return parsed_string[0] + parsed_string[2]
	if parsed_string[1] == "-":
		return parsed_string[0] - parsed_string[2]
	if parsed_string[1] == "/":
		return parsed_string[0] / parsed_string[2]
	if parsed_string[1] == "*":
		return parsed_string[0] * parsed_string[2]
	if parsed_string[1] == "^":
		return parsed_string[0] ** parsed_string[2]

def compute(the_string):
	try:
		the_string = the_string.replace(" ", "") ### delete space chars
		while br_op in the_string : 
			open_pos = the_string.index(br_op)
			close_pos = find_close_pos(the_string)
			old = the_string[open_pos:close_pos+1]
			new = compute(the_string[open_pos+1:close_pos])
			the_string = the_string.replace(old, str(new))
		parsed_string = parse(the_string)
		for operation in operations:
			while operation in parsed_string:
				pos = len(parsed_string) - parsed_string[::-1].index(operation)
				res = single_operation(parsed_string[pos-2:pos+1])
				parsed_string[pos-2:pos+1] = [res]
		return parsed_string[0]
	except:
		pass

def read_file(path):
	lines = [ line for line in open (path,'r') if line.strip() != "" ]
	return lines

def main(path):
	try:
		for line in read_file(path):
			print str(round(float(compute(line)),5)).rstrip('0').rstrip('.')
	except:
		print line
		print "Unexpected error:", sys.exc_info()[0]

if __name__ == '__main__':
	path = sys.argv[1]
	main(path)
