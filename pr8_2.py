def filter_cars(year : int) -> list:
    result = []
    for car in car_list:
        if car["year"] < year:
            result.append(car)
        return result


if __name__ == "__main__":
    car_list = [
          {
              "serial": 32145,
              "color": "red",
              "year": 2015,
          },
          {
              "serial": 32133,
              "color": "black",
              "year": 2011,
          },
          {
              "serial": 31145,
              "color": "white",
              "year": 2010,
          }
    ]
    year = int(input("year: "))
    print(list(filter(lambda x: x["year" < year, car_list])))