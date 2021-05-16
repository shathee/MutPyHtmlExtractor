def true_positive(l1,l2):
    tp = 0
    for i in range(len(l1)):
        if l1[i]==l2[i]==1:
            tp += 1
    return tp


def true_negative(l1,l2):
    tn = 0
    for i in range(len(l1)):
        if l1[i]==l2[i]==0:
            tn += 1
    return tn


def false_positive(l1,l2):
    fp = 0
    for i in range(len(l1)):
        if l1[i] != l2[i] and l2[i]==1:
            fp += 1
    return fp


def false_negative(l1,l2):
    fn = 0
    for i in range(len(l1)):
        if l1[i] != l2[i] and l2[i] ==0:
            fn += 1
    return fn

def calc_mcc(l1,l2):
    tp = float(true_positive(l1,l2))
    tn = float(true_negative(l1,l2))
    fp = float(false_positive(l1,l2))
    fn = float(false_negative(l1,l2))
    
    num = (tp * tn) - (fp * fn)
    den = (tp+fp) * (tp+fn) * (tn+fp) * (tn+fn)
    print(num, den)
    den = den**(1/2)
    if num != 0 or den != 0:
        mcc = num / den
    else:
        mcc = 0
    return mcc



# if __name__ == "__main__":
#   test1 = [0,1,1,0,0,0]
#   test2 = [0,1,1,0,1,0]

#   print('Value', calc_mcc(test1, test2))
