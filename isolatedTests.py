def test(variableOfUnknownType):return eval(f"{str(type(variableOfUnknownType))[8:-2]}(str(variableOfUnknownType)[::-1])")
print(test(7431))