while True:
prompt = "Please enter score 0 to 1\n"
score = (input(prompt))
try:
  score = float(score)
  if score >= 0 and score <= 1:
    break;
  else:
    print("Input value out of range.")

except:
  print("Invalid input.")

if score >= 0.85:
 print("A")
elif score >= 0.75:
 print("B")
elif score >= 0.65:
 print("C")
elif score >= 0.50:
 print("D")
elif score < 0.5:
 print("F")
