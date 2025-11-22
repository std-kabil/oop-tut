class Car():
    color = "red"
    numDoors = 4
    isElectric = False

    def start():
        print('the car has started')

    def turn_on_lights():
        print("the lights are on")

    def lock_dors():
        print('the doors are locked')


porsche_911 = Car()

print(porsche_911.color)

porsche_911.start()

# porsche_911.start()
# ~~~~~~~~~~~~~~~~~^^
# TypeError: Car.start() takes 0 positional arguments but 1 was given