# divide and conquer

brackets = [[")","}","]"],["(","{","["]]
close_bracket = 0
open_bracket = 1

def get_bracket_type(char):
        if char in brackets[1]:
                return open_bracket # 1 - true
        else:
                return close_bracket # 0 - false

def divide(string):
	array = []
	new_elem = []
	remember = []
	for i in range (len (string)):
		char = string[i]
		if get_bracket_type(char) == open_bracket : # till the first close-open (() | [
			if len(new_elem) > 0 : # check if prev is not closing bracket
				if get_bracket_type(new_elem[len(new_elem)-1]) == close_bracket :
					array.append(new_elem)
					new_elem = []
					remember = []
			new_elem.append(char)
			remember.insert(0, pair(char))
		if get_bracket_type(char) == close_bracket : # till the first closing bracket that doesnt have opening
			if len(new_elem) == 0: # if first is closing - divide as single
				new_elem.append(char)
				array.append(new_elem)
				new_elem = []
				remember = []
			else:
				if char in remember:
					remember = remember[remember.index(char)+1:]
					new_elem.append(char)
				else :
					array.append(new_elem)
					new_elem = []
					remember = []
					new_elem.append(char)
	array.append(new_elem)
	# print(array)
	for i in range(len(array)):
		array[i] = conquer(array[i])
	return "".join(array)

def pair(char):
	given_type = get_bracket_type(char)
	search_type = abs(given_type - 1)
	return brackets[search_type][brackets[given_type].index(char)]

def is_pair(char1, char2):
	return char2 == pair(char1)

def conquer(array):
	if len(array) == 0 :
		return ""
	if len(array) == 1 :
		if get_bracket_type(array[0]) == open_bracket :
			return array[0] + pair(array[0])
		else :
			return pair(array[0]) + array[0]
	if is_pair(array[0],array[len(array)-1]):
		return array[0] + conquer(array[1:len(array)-1]) + array[len(array)-1]
	else :
		return array[0] + conquer(array[1:len(array)]) + pair(array[0])

print("}([(]} --->", divide("}([(]}") ) # {}([()]){}
print("([([] --->", divide("([([]") )
print("([[] --->", divide("([[]") )
print("{{}[]]]([[] --->", divide("{{}[]]]([[]") )
print("{{}[]]]([[]}{ --->", divide("{{}[]]]([[]}{") )
print("{{}([(]} --->", divide("{{}([(]}") )
