import matplotlib.pyplot as plt

#Physical Constants
G = 6.6743e-11
EARTH_MASS = 5.972e24
EARTH_RADIUS = 6.371e6

#Rocket Specifications
rocket_dry_mass = 20000 #kg
fuel_mass = 30000 #kg
thrust = 800000 #N
fuel_burn_rate = 200 #kgs-1

#Inital Simulation State
height = 0.0 #AGL (m)
velocity = 0.0 #ms-1
time = 0.0 #s
dt = 0.1 #Time step in seconds (dt->0)

#Data lists for Plotting
time_history = []
height_history = []
velocity_history = []
fuel_history = []

#Simulation Loop (discrete calculus approximation)
while height >= 0:
    #Stop if too high
    if height > 1000000 or time > 500:
        break

    total_mass = rocket_dry_mass + fuel_mass
    current_radius = EARTH_RADIUS + height

    #Calculate dynamic acceleration due to gravity
    gravity_acceleration = (G * EARTH_MASS) / (current_radius**2)

    #Calculate thrust force based on remaining fuel
    if fuel_mass > 0:
        current_thrust = thrust
        fuel_mass -= fuel_burn_rate * dt # Burn fuel over time interval dt
        if fuel_mass <= 0:
            fuel_mass = 0
    else:
        current_thrust = 0.0

    #Newtons second law: f=ma -> a = f/m

    acceleration = (current_thrust / total_mass) - gravity_acceleration

    #EULERS METHOD (Integration): Update velocity and position using the derivatives
    velocity += acceleration * dt
    height += velocity * dt
    time += dt

    #Store history for data visualisation
    time_history.append(time)
    height_history.append(height/1000)
    velocity_history.append(velocity)
    fuel_history.append(fuel_mass)


#Plot results

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(time_history,height_history, color="blue")
plt.title('Rocket Altitiude Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Altitude (me3)')

#Plot Velocity
plt.subplot(1,2,2)
plt.plot(time_history,velocity_history,color='red')
plt.title('Rocket Velocity Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity ms-1')

plt.tight_layout()
plt.show()

print("All done here!")