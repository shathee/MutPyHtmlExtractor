class MCC():
      def __init__(self):
            self.tp=0
            self.tn=0
            self.fp=0
            self.fn=0

      def true_positive(self,l1,l2):
            for i in range(len(l1)):
                if l1[i]==l2[i]==1:
                    self.tp += 1
      
      def true_negative(self,l1,l2):
            for i in range(len(l1)):
                if l1[i]==l2[i]==-1:
                    self.tn += 1

      def false_positive(self,l1,l2):
            for i in range(len(l1)):
                if l1[i] != l2[i] and l2[i]==1:
                    self.fp += 1
        
      def false_negative(self,l1,l2):
            for i in range(len(l1)):
                if l1[i] != l2[i] and l2[i] ==-1:
                    self.fn += 1
        
      def calc_mcc(self,l1,l2):
            self.true_positive(l1,l2)
            self.true_negative(l1,l2)
            self.false_positive(l1,l2)
            self.false_negative(l1,l2)
            
            num = (self.tp * self.tn) - (self.fp * self.fn)
            den = (self.tp+self.fp) * (self.tp+self.fn) * (self.tn+self.fp) * (self.tn+self.fn)

            den = den**(1/2)
            if num != 0 or den != 0:
                mcc = num / den
            else:
                mcc = 0
            return mcc


# def main():
#     mcc = MCC()
#     y_true = [1, 1, -1, -1]
#     y_pred = [-1, -1, +1, +1]
#     print(mcc.calc_mcc(y_true,y_pred))

# if __name__=="__main__":
#     main()

