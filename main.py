# your functions here



# main function
def main(): 
  # 1 tuple  
  tuplea = 'green',4,5,6,7,5,5,'blue','green'
  count, ix = tuple_func(tuplea, 5)
  print('count',count,'ix',ix)
  count, ix = tuple_func(tuplea, 'green')
  print('count',count,'ix',ix)
  
  # 2 list 
  word_list = [ 'blueish', 'green grass', 'brown dirt', 'newfoundland']
  size = smallest_word(word_list)
  print('size',count,'@ix',word_list[ix])

  # 3 dictionary 
  empty = {}
  months = { "jan" : 1 , "feb" : 2 , "mar" : 3 , \
        "apr" : 4 , "may" : 5 , "jun" : 6 , "jul" : 7 , "aug" : 8 , \
        "sep" : 9 , "oct" : 10 , "nov" : 11 , "dec" : 12}
  print("sb False", find_kv(months, "apr", 12))
  print("sb True", find_kv(months, "apr", 4))

  # 4 dictionary
  print("sb 10", find_kv(months, "oct"))
  print("sb 0", find_kv(months, "xyz"))
  
  # 5 dictionary
  print(make_alpha())
  
if __name__ == "__main__":
  main():