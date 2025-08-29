dictionary={'alice':'85', 'joe':'58','rambo':'90'}
name=(input("Enter the student's name: ")).lower()
if(name in dictionary):
   print(f"{name} marks: {dictionary[name]}")
else:
   print(f"{name} not found")