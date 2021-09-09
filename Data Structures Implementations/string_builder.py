from dynamic_arrray import DynamicArray

class StringBuilder(DynamicArray):
    def toString(self):
        sentence = ""
        for w in self.data:
            sentence += w
        return sentence
    

p = StringBuilder()
print(p.data)
print(p.append("hi"))
print(p.append("gh"))
print(p.append('land'))
print(p.append('er'))
print(p.toString())
