
from sklearn.metrics import matthews_corrcoef
import csv

y_true = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y_pred = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# print (matthews_corrcoef(y_true, y_pred))


empty_dict = {}
with open("input_for_distance/VoidMethodCallMutator-cli.csv", mode='r') as infile:
  files = csv.reader(infile)
  next(files)
  next(files)
  for line in files:
    empty_dict[line[0]] = line[1:]


tc1_list = []
tc2_list = []
dist_list = []
for key1, value1 in empty_dict.items():
  tmp_lst = []
  tmp_lst.append(key1)
  for key2, value2 in empty_dict.items():
    d = (1-matthews_corrcoef(value1,value2))/2
    tc2_list.append(key2)
    tmp_lst.append(d)
  dist_list.append(tmp_lst)
  tc1_list.append(key1)


new_tc1 = ['']
for ur in tc1_list:
  new_tc1.append(ur)




f = csv.writer(open('VoidMethodCallMutator_cli_dis.csv', "a", newline='',  encoding="Latin-1"))
f.writerow(new_tc1)
for d in dist_list:
    f.writerow(d)

