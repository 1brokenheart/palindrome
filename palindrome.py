class Deque:
  def __init__(self):
    self.elements = []
  def add_first(self, item):
    self.elements.append(item)
  def add_last(self, item):
    self.elements.insert(0, item)
  def remove_first(self):
    item = self.elements.pop()
    return item
  def remove_last(self):
    item = self.elements.pop(0)
    return item
  def is_empty(self):
    if len(self.elements) > 0:
      return False
    return True
  def size(self):
    return len(self.elements)
  def peek_first(self):
    return self.elements[-1]
  def peek_last(self):
    return self.elements[0]
  def display_deque(self):
    print('\t | \t'.join(str(item) for item in self.elements))
    
   
def is_palindrome(word):
  deque = Deque()
  for char in word:
    # Add the characters to the front of the deque
    deque.elements.append(char)

    #continuously check that the first and the last character of the word are equal until they either are different or there is only word character left on the stack.
  while deque.size() > 1:
      #remove from the rear character of the deque = the last letter of the word.
      first = deque.elements.pop()
      print(first)     
      #remove from the front of the deque = the first letter of the word.
      last = deque.elements.pop(0)
      print(last)
      # check if the first and last letter of the word are equal until we get to the center of the word.
  if first != last:
    return False
  return True


deque = Deque()
print(is_palindrome('hannah'))
print(is_palindrome('aristocrata'))
print(is_palindrome('level'))
print(is_palindrome('abecedario'))
print(is_palindrome('mom'))
