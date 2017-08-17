with open("sample.in") as f:
  for line in f:
    int_list = [int(i) for i in line.split()]
    print (abs(int_list[0]-int_list[1]))
