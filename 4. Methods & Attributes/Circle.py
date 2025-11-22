class Circle:
    center = (0, 0)
    radius = 8

    def get_area(self):
        return 3.14 * (self.radius ** 2)
    
    def __repr__(self):
        pass
    
c1 = Circle()

c2 = Circle()
c2.radius = 7

c3 = Circle()
c3.radius = 4

print(c1.get_area())
print(c2.get_area())
print(c3.get_area())

# 200.96
# 153.86
# 50.24