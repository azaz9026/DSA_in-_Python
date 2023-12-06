## length_of_last_word ------------------------------------------------------------------------------------------------------------------------------------


def length_of_last_word(s):
    s = s.strip()  # Assign the stripped string back to s
    if len(s) == 0:
        return 0

    return len(s) - s.rfind(" ") - 1  # Correct the syntax for rfind

# Example
my_string = "Azaz Khan"
length_of_last = length_of_last_word(my_string)
print("Length of the last word :- ", length_of_last)
