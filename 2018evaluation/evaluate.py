###################################################
# Multimodal Lexical Translation Evaluation
###################################################

# Reading the Index File which contains location of
# files to be evaluated, year, target_language
f = open('index.txt', 'r')
lines = f.readlines()
f.close()

filenames = {}
for line in lines:
    filename = line.split()[0]
    year = line.split()[1]
    language = line.split()[2]
    key = year+'_'+language
    if key not in filenames.keys():
        filenames[key] = [filename]
    else:
        filenames[key].append(filename)

# Test 2018 ENDE
f = open('MLTreferences/ENDE_MLTD_test2018.txt', 'r')
references = f.readlines()
f.close()

for file in filenames['18_de']:
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    correct = 0
    for i in range(len(references)):
        splitted = references[i].split()
        linenum = int(splitted[-1])
        for word in splitted[1:]:
            if word in lines[linenum].split():
                correct += 1
                break
    print(file)
    print('accuracy = '+str(correct)+
          ' / '+str(len(references))+
          ' = '+str(float(correct)/len(references)))
    print('\n')

# Test 2018 ENFR
f = open('MLTreferences/ENFR_MLTD_test2018.txt', 'r')
references = f.readlines()
f.close()

for file in filenames['18_fr']:
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    correct = 0
    for i in range(len(references)):
        splitted = references[i].split()
        linenum = int(splitted[-1])
        for word in splitted[1:]:
            if word in lines[linenum]:
                correct += 1
                break
    print(file)
    print('accuracy = '+str(correct)+' / '+
          str(len(references))+' = '+
          str(float(correct)/len(references)))
    print('\n')
