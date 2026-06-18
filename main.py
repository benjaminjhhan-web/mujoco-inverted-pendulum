import mujoco
import matplotlib.pyplot as plt
import numpy as np

model = mujoco.MjModel.from_xml_path("robot.xml")
data = mujoco.MjData(model)
data.qpos[1] = 0.2 
mujoco.mj_forward(model, data)

Kp = 100.0  
Kd = 10.0   

angles = []

for i in range(1000):
    noise = np.random.normal(0, 0.05) 
    current_angle = data.qpos[1] + noise
    angular_velocity = data.qvel[1]
    
    force = (Kp * current_angle) + (Kd * angular_velocity)
    data.ctrl[0] = force
    
    mujoco.mj_step(model, data)
    angles.append(data.qpos[1])

plt.plot(angles)
plt.title("Stability with Noisy Sensor Data")
plt.xlabel("Step")
plt.ylabel("Angle (radians)")
plt.show()