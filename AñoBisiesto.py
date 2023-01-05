def years(year):
  counter = 0
  while counter < 30:
    year += 1
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
      print(year)
      counter += 1
years(2000)