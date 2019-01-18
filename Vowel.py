a=input()
l=['a','e','i','o','u']
if a.isalpha():
    if any(i in l for i in a):
        print("yes")
    else:
      print("no")
else:
  print("no")
