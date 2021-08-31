# Set - data structure to ensure only uniques exist
# API:
#   include
#   set
#   delete

class Set():
    def __init__(self):
        self.data = [1,2,3]
    
    def include(self, value):
        try:
            if self.data.index(value) >= 0:
                return True
            else:
                return False
        except ValueError:
            return 'Value {} does not exist'.format(value)
    def setValue(self, value):
        if self.include(value) == True:
            return 'Value {} already exists'.format(value)
        else:
            self.data.append(value)
            return self.data

s = Set()
print(s.include(1))
print(s.include(4))
print(s.setValue(4))
print(s.include(4))
