class Batcher: 
    def __init__(self, batch_size): 
        pass


    def add(self, feature, label): 
        pass


    def get(self): 
        pass


a = Batcher(4) 

# FIFO 

feature = [ [1, 2, 3], [4, 5, 6]]
labels = [0, 1]
a.add(feature, labels) 

feature = [ [7, 8, 9], [10, 11, 12] ]
labels = [2, 3]
a.add(feature, labels) 

feature = [ [13, 14, 15], [16, 17, 18] ]
lables = [4, 5]
a.add(feature, lables)


a.get()
a.get()