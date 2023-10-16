f = open("demofile.txt", "r")
txt = f.read().lower()

if "welcome" in txt:
  print("Yes, 'welcome' is present.")
if "testing" in txt:
  print("Yes, 'testing' is present.")