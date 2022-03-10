# Instructions  

  ** some exercises using tuples, lists, dicts**

  _ use functions _

  ## Steps
  1. Tuple `tuple_func()` Write a function that takes a tuple and an item, counts how many items are in the tuple, and returns the count  (or -1 if not found)
  2. List `smallest_word()` Write a function that takes a list of words and determines the smallest word, it returns the word  size and the index of the word (a tuple)
  3. Dict `find_kv()` Write a function that takes a dictionary, a key and a value. If the key is in the dictionary and associated with the value, return True, otherwise return False   (as a dict argument you use the month dict in main or create your own)
  4. Dict `find_val()` Write a function that takes a dictionary, and a key. If the key is in the dictionary return the value if not return 0  (as a dict argument you use the month dict in main or create your own)
  5. Dict `make_alpha()` Write a function that creates and returns a dictionary that contains all the letters of the alphabet with their values being their location in the alphabet. 
    * Example: lower_alpha = {'a': 0, 'b': 2 ... 'z': 25 }
    * Hint: import the string module, and use `string.ascii_...` lower or upper case string which contains all the letters https://docs.python.org/3/library/string.html   
    * Note: you can use the string constants variables the same way you use math.pi
6. Dict `make_digit_dict()` Write a function that creates and returns a dictionary that contains the numbers  as charcters use `string.digits` with their values being their number value.
    * Example = {'0':0, ...}