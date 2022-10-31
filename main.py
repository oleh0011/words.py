alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmйцукенгшщзхїфівапролджєячсмитьбю1234567890"
key = 3
s = input("Введіть символи для шифровки: ")
subst = dict(zip(alphabet, alphabet[key:]+alphabet[:key]))
res = ''.join(map(subst.__getitem__, s))
print('Result: "' + res + '"')