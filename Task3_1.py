# Попросить пользователя ввести текст. В результате вывести процент букв в верхнем
# регистре (заглавные) и в нижнем регистре (прописные).

text = input("Enter a text: ")
capit = sum(1 for c in text if c.isupper())
small = sum(1 for s in text if s.islower())

print("Capital letters: ", capit)
print("Small letters: ", small)

all = (capit + small)
per_cap = capit*100/all
per_small = 100 - per_cap
print("Percent of capitals: ", round(per_cap), "%")
print("Percent of smalls: ", round(per_small), "%")
