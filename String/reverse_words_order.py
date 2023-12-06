## reverse_words_order ------------------------------------------------------------------------------------------------------------------------------------


def reverse_words_order(s):
   word = s.strip()
   word = s.split()  # Split the string into a list of words
   reversed_str = word[::-1] # Reverse the order of the words
   result = " ".join(reversed_str)
   return result




# Example
my_string = ' Azaz Khan'
reversed_order_string = reverse_words_order(my_string)
print("Reversed order of words:", reversed_order_string)

## Ans -> Khan Azaz


## another method------------------------------------------------------------------------------------


def reverse_words_order(s):
    words = s.split()  # Split the string into a list of words
    reversed_words = words[::-1]  # Reverse the order of the words
    result = " ".join(reversed_words)  # Join the reversed words back into a string
    return result

# Example
my_string = 'Azaz Khan'
reversed_order_string = reverse_words_order(my_string)
print("Reversed order of words:", reversed_order_string)


## Ans -> Khan Azaz