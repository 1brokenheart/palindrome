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
