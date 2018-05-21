def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
       	return False



def add2vals(first, second):
	if is_number(first) and is_number(second):
		return float(first)+float(second)
	else:
		return str(first)+str(second)

arg1 = input("Enter the first value: ")
arg2 = input("Enter the second value: ")
print(add2vals(arg1, arg2))