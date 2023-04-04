def main():
  x = int(input("Masukkan nilai x: "))
  y = int(input("Masukkan nilai y: "))

  if x > 0 and y > 0:
    print(f"Koordinat ({x},{y}) berada pada kuadran I")
  elif x < 0 and y > 0:
    print(f"Koordinat ({x},{y}) berada pada kuadran II")
  elif x < 0 and y < 0:
    print(f"Koordinat ({x},{y}) berada pada kuadran III")
  elif x > 0 and y < 0:
    print(f"Koordinat ({x},{y}) berada pada kuadran IV")
  else:
    pass

main()