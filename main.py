# Using readlines()
# file1 = open('eidl1.csv', 'r')
# Lines = file1.readlines()
with open('eidl5.csv', 'r', encoding='utf-8') as f:
    Lines = f.readlines()
f.close()

ex = []
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    l =  line.strip()
    if '.com' in l:
        if '@' in l:
      
            ex.append(l)
print(ex)
# file1 = open('public_150k_plus_parsed.csv', 'w')
# file1.writelines(ex)
# file1.close()

with open('public_150k_plus_parsed.csv', mode='a', encoding='utf-8') as myfile:
    myfile.write('\n'.join(ex))
