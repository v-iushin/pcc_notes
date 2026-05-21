# TASK

# N-BODY GRAVITATIONAL SIMULATION (OOP)

# 1. Vector class
# 2. Body class
# 3. Subclasses of Body
# 4. Simulation Class
# 5. test



import math

G = 6.674e-11

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
    def __truediv__(self, s):
        return Vector(self.x / s, self.y / s)
    def __abs__(self):
        return math.sqrt((self.x**2 + self.y**2))
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def unit(self):
        mag = abs(self)
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
        self.v += a * dt / 2
        self.r += self.v * dt
        self.v += a * dt / 2
    @property
    def kinetic_energy(self):
        return 0.5 * self.mass * abs(self.v)**2
    @property
    def momentum(self):
        return self.mass * self.v

class Star(Body):
    STELLAR_TYPE = "G-type"
    @classmethod
    def from_solar_units(cls, name, mass_in_solar_masses, x, y, vx, vy):
        solar_mass = 1.989e30
        mass_kg = mass_in_solar_masses * solar_mass
        return cls(name, mass_kg, x, y, vx, vy)

class Planet(Body):
    def orbital_period_estimate(self, central_mass):
        T = 2 * math.pi * math.sqrt(abs(self.r)**3 / G / central_mass )
        return T
        
class Simulation:
    def __init__(self, *bodies: Body, dt=3600):
        self.bodies = list(bodies)
        self.dt = dt
    def add_body(self, body):
        self.bodies.append(body)
    def remove_body(self, name):
        self.bodies = [b for b in self.bodies if b.name != name]
    def __len__(self):
        return len(self.bodies)
    def __iter__(self):
        return iter(self.bodies)
    def step(self):
        EPS = 1000
        forces = {b: Vector(0, 0) for b in self.bodies}
        for i, bi in enumerate(self.bodies):
            for j, bj in enumerate(self.bodies):
                if i < j:
                    d_ij = bj.r - bi.r
                    d_ij_u = d_ij.unit()
                    d_abs = abs(d_ij)
                    f_abs = G * bi.mass * bj.mass / (d_abs**2 + EPS**2)
                    f_ij = f_abs * d_ij_u
                    forces[bi] = forces[bi] + f_ij
                    forces[bj] = forces[bj] + f_ij * (-1)
        for b in self.bodies:
            b.apply_force(forces[b], self.dt)
    def total_energy(self):
        energy = 0
        for b in self.bodies:
            energy += b.kinetic_energy
        for i, bi in enumerate(self.bodies):
            for j, bj in enumerate(self.bodies):
                if i < j:
                    d_ij = bj.r - bi.r
                    d_abs = abs(d_ij)
                    energy += (-1) * G * bi.mass * bj.mass / d_abs
        return energy
    def run(self, N):
        snapshots = []
        for _ in range(N):
            self.step()
            snapshot = {b.name: (b.r.x, b.r.y) for b in self.bodies}
            snapshots.append(snapshot)
        return snapshots
    @classmethod
    def solar_system_demo(cls):
        sun = Star("Sun", 1.989e30, 0, 0, 0, 0)
        earth = Planet("Earth", 5.97e24, 0, 1.5e11, 29783, 0)
        mars = Planet("Mars", 6.39e23, 0, 2.28e11, 24077, 0)
        return cls(sun, earth, mars)

sim = Simulation.solar_system_demo()

e0 = sim.total_energy()
snapshots = sim.run(10000)
e1 = sim.total_energy()

print(f"Energy at step 0: {e0}")
print(f"Energy at step 10000: {e1}")
print(f"Energy drift: {abs(e1 - e0) / abs(e0) * 100}")

print()
