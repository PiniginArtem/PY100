from pprint import pprint
dict_ = {'bin': bin, 'dec': int, 'hex': hex, 'oct': oct}
list_dict = [{key_: value_(i) for key_, value_ in dict_.items()} for i in range(16)]
pprint(list_dict)