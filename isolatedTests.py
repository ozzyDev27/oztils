def test(variableOfUnknownType):
  getType=type(variableOfUnknownType)
  variableOfUnknownType=eval(f"{str(getType)[8:-2]}(str(variableOfUnknownType)[::-1])")
  return variableOfUnknownType
print(test(7431))