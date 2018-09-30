def Weight_Sort(a):
  passenger_car=0
  busOrLiteTrack=0
  truck=0
  for i in range (1,len(a)):
    if (a[i] <=18):
      passenger_car += 1
    elif(a[i] <= 24):
      busOrLiteTrack += 3
    else:
      truck += 1
  classified_cars = [passenger_car, busOrLiteTrack, truck]
  return classified_cars
  #Возвращает список типа: кол-во легковушек, кол-во автобусов или маленьких грузовых машин, кол-во грузовых машин
