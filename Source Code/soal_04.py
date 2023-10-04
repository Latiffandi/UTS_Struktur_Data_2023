class stack:
    def __init__(self):
        self.items = []
    
    def push (self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. ")
            return None
    
    def is_empty(self):
        return len(self.items)==0
    
# Contoh penggunaan
stack = stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Is Stack Empty:", stack.is_empty())

popped_item = stack.pop()
print("Popped Item:", popped_item)