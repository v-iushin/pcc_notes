# TASK

# N-BODY GRAVITATIONAL SIMULATION (OOP)

# 1. Vector class
# 2. Body class
# 3. Subclasses of Body
# 4. Simulation Class
# 5. test



import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, s):
        return Vector(self.x * s, self.y * s)
    def __rmul__(self, s):
        return (self * s)
        #return self.__mul__(s)
    def __truediv__(self, s):
        return Vector(self.x / s, self.y / s)
    def __abs__(self):
        #return (self.x**2 + self.y**2)**(0.5)
        return math.sqrt((self.x**2 + self.y**2))
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def unit(self):
        mag = abs(self)
        #mag = self.__abs__()
        if mag == 0:
            raise ValueError("zero-vector")
        else:
            return Vector(self.x / mag, self.y / mag)
    def __eq__(self, other):
        eps = 1e-9
        return abs(self.x - other.x) < eps and abs(self.y - other.y) < eps

class Body:
    def __init__(self, name, mass, x, y, vx, vy):
        self.name = name
        self.mass = mass
        self.r = Vector(x, y)
        self.v = Vector(vx, vy)
    def apply_force(self, force: Vector, dt):
        a = force / self.mass
        self.v += a * dt
        self.r += self.v * dt
    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * abs(self.v)**2
    @property
    def momentum(self):
        return self.mass * self.v

s = Body("Sun", 1.989e30, 0, 0, 0, 0)
e = Body("Earth", 5.97e24, 0, 1.5e11, 29783, 0)
m = Body("Mars", 6.39e23, 0, 2.28e11, 24077, 0)


v0 = Vector(0, 0)
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v_ = Vector(2**(1/2)/2, 2**(1/2)/2)





