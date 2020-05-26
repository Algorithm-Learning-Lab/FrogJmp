def solution(X, Y, D) :

  if (Y-X) % D == 0 :
    result = (Y-X) // D

  else :
    result = ((Y-X) // D) + 1

  print("result :", result)



X = int(input("insert X : "))
Y = int(input("insert Y : "))
D = int(input("insert D : "))

if (X < 1 or X > 1000000000) or (Y < 1 or Y > 1000000000) or (D < 1 or D > 1000000000) or X > Y :
  print("Error")

else :
  solution(X, Y, D)
