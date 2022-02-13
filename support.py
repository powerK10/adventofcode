def main():
    print("Hello World")

def extract_number_from_str(i):
  f_result = int(list(filter(str.isdigit, i))[0])
  return f_result

def get__number_from_list(i):
    strings = [str(integer) for integer in i]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer
