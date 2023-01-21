import math
import matplotlib.pyplot as plt



print("Car Braking Simulator \n");


# input the initial velocity of the car (in km/hr)

while True:
    v0_kmh = float(input("Enter the initial velocity of the car before braking (in km/hr): "))
    if v0_kmh <= 0:
        print("Incorrect choice, the initial velocity must be greater than 0 \n")
    else:
        print("Your input velocity before braking is: \n", v0_kmh,"km/hr")
        break

# convert the initial velocity to m/s

v0 = v0_kmh * 0.277778

# create a list of initial velocities
v = list(range(0, int(v0+1), 10))


# input the road type

while True:
    road_type = input("Enter the road type (concrete, ice, water, gravel, sand): ")
    if road_type not in ["concrete","ice","water","gravel","sand"]:
        print("Incorrect choice, the road type must be one of these options: concrete, ice, water, gravel, sand \n")
    else:
        print("Your input road type is: \n", road_type)
        break

# input the road condition

while True:
    road_condition = input("Enter the road condition (dry, wet, aquaplaning): \n")
    if road_condition not in ["dry","wet","aquaplaning"]:
        print("Incorrect choice, the road type must be one of these options: dry, wet, aquaplaning)")
    else:
        print("Your input road type is:\n", road_condition)
        break

# input the coefficient of friction type

while True:
    friction_type = input("Enter the coefficient of friction type (static or dynamic): \n")
    if friction_type not in ["static","dynamic"]:
        print("Incorrect choice, the friction type must be one of these options: static or dynamic)")
    else:
        print("Your input friction type is:\n", friction_type)
        break

# input the inclination angle of the road
while True:
    incline = float(input("Enter the inclination angle of the road (in degrees): "))
    if incline < -90 or incline > 90:
        print("Incorrect choice, the inclination angle must be between -90 and 90 degrees.\n")
    else:
        print("Your input inclination angle is: \n", incline,"degrees")
        break


# set the coefficient of friction based on road type, condition and type
#if none of the options provided in the task's table, mu will be set to 0.8 
#longer method of if and elif was used instead of dictionary as it's basic 

if road_type == "concrete":
    if road_condition == "dry":
        if friction_type == "static":
            mu = 0.65
        elif friction_type == "dynamic":
            mu = 0.5
    elif road_condition == "wet":
        if friction_type == "static":
            mu = 0.4
        elif friction_type == "dynamic":
            mu = 0.35
elif road_type == "ice":
    if road_condition == "dry":
        if friction_type == "static":
            mu = 0.2
        elif friction_type == "dynamic":
            mu = 0.15
    elif road_condition == "wet":
        if friction_type == "static":
            mu = 0.1
        elif friction_type == "dynamic":
            mu = 0.08
elif road_type == "water":
    if road_condition == "aquaplaning":
        if friction_type == "static":
            mu = 0.1
        elif friction_type == "dynamic":
            mu = 0.05
elif road_type == "gravel":
    if road_condition == "dry":
        if friction_type == "static":
            mu = 0.8
        elif friction_type == "dynamic":
            mu = 0.35
elif road_type == "sand":
    if road_condition == "dry":
        if friction_type == "static":
            mu = 0.8
        elif friction_type == "dynamic":
            mu = 0.3
else:
    mu = 0.8


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

# export the figure as a PDF file
plt.savefig('braking_distance.pdf', format='pdf')
