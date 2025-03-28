import os
print("Текущая рабочая директория:", os.getcwd())
file1 = r"C:\Users\iratk\OneDrive\Рабочий стол\files\1.txt"
file2 = r"C:\Users\iratk\OneDrive\Рабочий стол\files\2.txt"
file3 = r"C:\Users\iratk\OneDrive\Рабочий стол\files\3.txt"
result = r"C:\Users\iratk\OneDrive\Рабочий стол\files\result.txt"

with open(file1, encoding='utf-8') as f:
    lines1 = f.read()

with open(file2, encoding='utf-8') as f:
    lines2 = f.read()

with open(file3, encoding='utf-8') as f:
    lines3 = f.read()


with open(result, 'w', encoding='utf-8') as f:
    f.write('2.txt\n')

with open(result, 'a') as f:
    f.write('1\n')

with open(result, 'a', encoding='utf-8') as f:
    f.write(lines2)

with open(result, 'a', encoding='utf-8') as f:
    f.write('\n1.txt\n')

with open(result, 'a') as f:
    f.write('8\n')

with open(result, 'a', encoding='utf-8') as f:
    f.write(lines1)

with open(result, 'a', encoding='utf-8') as f:
    f.write('\n3.txt\n')

with open(result, 'a') as f:
    f.write('9\n')

with open(result, 'a', encoding='utf-8') as f:
    f.write(lines3)







