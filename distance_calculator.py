
from sklearn.metrics import matthews_corrcoef
import csv

from mcc import calc_mcc

def calculate_distances(fileName):
  file_split = fileName.split('\\')
  empty_dict = {}
  with open(fileName, mode='r') as infile:
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
    t1 = [int(1) if x=='1' else int(-1) for x in value1] #converting 0s to -1s
    for key2, value2 in empty_dict.items():
      t2 = [int(1) if x=='1' else int(-1) for x in value1] #converting 0s to -1s
      d = (1-matthews_corrcoef(value1,value2))/2 #actual scikit learn function
      tc2_list.append(key2)
      tmp_lst.append(d)
    dist_list.append(tmp_lst)
    tc1_list.append(key1)

  new_tc1 = ['']
  for ur in tc1_list:
    new_tc1.append(ur)



  f = csv.writer(open('distance_'+ file_split[-1], "a", newline='',  encoding="Latin-1"))
  f.writerow(new_tc1)
  for d in dist_list:
      f.writerow(d)


def calculate_distances_manual(fileName):
  file_split = fileName.split('\\')
  empty_dict = {}
  with open(fileName, mode='r') as infile:
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
    t1 = [int(i) for i in value1] #converting from string to int 
    # t1 = [int(1) if x=='1' else int(-1) for x in value1] #converting 0s to -1s
    
    for key2, value2 in empty_dict.items():
      # t2 = [int(1) if x=='1' else int(-1) for x in value2] #converting 0s to -1s
      t2 = [int(i) for i in value2]
      
      m = calc_mcc(t1,t2)
      if m == 0:
        d = m
      else:
        d = (1-m)/2
      tc2_list.append(key2)
      tmp_lst.append(d)
    dist_list.append(tmp_lst)
    tc1_list.append(key1)


  new_tc1 = ['']
  for ur in tc1_list:
    new_tc1.append(ur)



  f = csv.writer(open('distance_manual_'+ file_split[-1], "a", newline='',  encoding="Latin-1"))
  f.writerow(new_tc1)
  for d in dist_list:
      f.writerow(d)


