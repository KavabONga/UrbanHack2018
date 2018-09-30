def Weight_Sort(a):
  passenger_car=0
  busOrLiteTrack=0
  truck=0
  for j in range (1,len(a)):
    if (a[i] <=3):
      passenger_car += 1
    elif(3 < a[i] <= 8):
      busOrLiteTrack += 3
    elif(a[i] > 8):
      truck += 1
  classified_cars = [passenger_car, busOrLiteTrack, truck]
  return classified_cars
  #Возвращает список типа: кол-во легковушек, кол-во автобусов или маленьких грузовых машин, кол-во грузовых машин
