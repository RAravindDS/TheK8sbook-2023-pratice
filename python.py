class Batcher: 
    def __init__(self, batch_size): 
        self.batch_size = batch_size 
        self.common_feature_list = []
        self.common_label_list = [] 
        self.starting = 0 
        self.ending = batch_size 

    def add(self, feature, label): 
        self.common_feature_list.extend(feature) 
        self.common_label_list.extend(label) 

    def get(self): 

        # print(self.starting, self.ending)
        a = self.common_feature_list[self.starting:self.ending]
        b = self.common_label_list[self.starting:self.ending]
        
        c = self.batch_size + self.ending 
        self.starting = self.ending 
        self.ending = c

        # print(self.starting, self.ending)

        return (a, b)




a = Batcher(3) 

feature = [ [1, 2, 3], [4, 5, 6]]
labels = [0, 1]
a.add(feature, labels) 

feature = [ [7, 8, 9], [10, 11, 12] ]
labels = [2, 3]
a.add(feature, labels) 

feature = [ [13, 14, 15], [16, 17, 18] ]
lables = [4, 5]
a.add(feature, lables)

f, l = a.get()
print(f, l)

f, l = a.get() 
print(f, l)

f, l = a.get()
print(f, l)

