import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

print("Car Braking Simulator \n");

# input the initial velocity of the car (in km/hr)

while True:
    v0_kmh = input("Enter the initial velocity of the car before braking (in km/hr): ")
    try:
        v0_kmh = float(v0_kmh)
        if v0_kmh <= 0:
            raise ValueError
    except ValueError:
        print("Incorrect choice, the initial velocity must be greater than 0")
        continue
    print(f'Your input velocity before braking is: {v0_kmh} km/hr')
    break

# convert the initial velocity to m/s

v0 = v0_kmh * 0.277778

# create a list of initial velocities
v = list(range(0, int(v0+1), 10))

# input the road type

valid_road_types = ["concrete", "ice", "water", "gravel", "sand"]
while True:
    road_type = input("Enter the road type (concrete, ice, water, gravel, sand): ")
    if road_type in valid_road_types:
        print("Your input road type is: \n", road_type)
        break
    else:
        print("Incorrect choice, the road type must be one of these options: ", valid_road_types)

# input the road condition

valid_road_conditions = ["dry", "wet", "aquaplaning"]
while True:
    road_condition = input("Enter the road condition (dry, wet, aquaplaning): \n")
    if road_condition in valid_road_conditions:
        print("Your input road condition is:\n", road_condition)
        break
    else:
        print("Incorrect choice, the road condition must be one of these options: ", valid_road_conditions)

# input the coefficient of friction type

valid_friction_types = ["static", "dynamic"]
while True:
    friction_type = input("Enter the coefficient of friction type (static or dynamic): \n").lower()
    if friction_type in valid_friction_types:
        print("Your input friction type is:\n", friction_type)
        break
    else:
        print("Incorrect choice, the friction type must be one of these options: ", valid_friction_types)

# input the inclination angle of the road
while True:
    incline = input("Enter the inclination angle of the road (in degrees): ")
    try:
        incline = float(incline)
        if incline < -90 or incline > 90:
            raise ValueError
    except ValueError:
        print("Incorrect choice, the inclination angle must be between -90 and 90 degrees.")
        continue
    print(f'Your input inclination angle is: {incline} degrees')
    break

# set the coefficient of friction based on road type, condition and type
#if none of the options provided in the task's table, mu will be set to 0.8 
#longer method of if and elif was used instead of dictionary as it's basic 

coefficients = {
    ("concrete", "dry", "static"): 0.65,
    ("concrete", "dry", "dynamic"): 0.5,
    ("concrete", "wet", "static"): 0.4,
    ("concrete", "wet", "dynamic"): 0.35,
    ("ice", "dry", "static"): 0.2,
    ("ice", "dry", "dynamic"): 0.15,
    ("ice", "wet", "static"): 0.1,
    ("ice", "wet", "dynamic"): 0.08,
    ("water", "aquaplaning", "static"): 0.1,
    ("water", "aquaplaning", "dynamic"): 0.05,
    ("gravel", "dry", "static"): 0.8,
    ("gravel", "dry", "dynamic"): 0.35,
    ("sand", "dry", "static"): 0.8,
    ("sand", "dry", "dynamic"): 0.3
}

mu = coefficients.get((road_type, road_condition, friction_type), 0.8)

# calculate the corresponding braking distances using the formula:
# braking distance = (v^2) / (2 * mu * g * inclination)
# where g is the acceleration due to gravity (approximately 9.8 m/s^2)

g = 9.8
#iterating over the list of initial velocities v, and for each initial velocity i,
#and calculating the braking distance using the equation provided, and storing the result in a list d.
d = [(i**2 - v0**2) / (2 * mu * g* math.cos(math.radians(incline))) for i in v]

print("The braking distance is:", d, "meters")

# calculate the braking time using the formula:
# braking time = (v) / (mu * g)
t = [(v[i] - v0) / (-mu * g) for i in range(len(v))]
#t = float( v / (mu * g))
print("The braking time is:", t, "seconds")

# rule of thumb "it takes about one car length for every 10 km/h of speed to come to a stop."
d_rule_of_thumb = [v / 10 for v in v]

# plot the graph

plt.plot(v, d, label='Physics model')
plt.plot(v, d_rule_of_thumb, label='Rule of thumb')
plt.xlabel('Initial Velocity (km/h)')
plt.ylabel('Braking Distance (m)')
plt.title('Braking Distance vs. Initial Velocity')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()

# plot the graph for braking time
plt.plot(v, t)
plt.xlabel('Initial velocity (m/s)')
plt.ylabel('Braking time (s)')
plt.title('Braking time vs. Initial velocity')
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("output.pdf")

print("The plots have been exported to output.pdf")
