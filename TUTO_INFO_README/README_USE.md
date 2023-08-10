# How To USE this project
## 1. Install the project
### 1.1. Install ROS
Follow the instructions on the official website: http://wiki.ros.org/ROS/Installation
### 1.2. Install the project
Clone the project in your catkin workspace:
```bash
cd ~/catkin_ws/src
git clone
```
### 1.3. Install the dependencies
```bash
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
```
### 1.4. Build the project
```bash
cd ~/catkin_ws
catkin_make
```
## 2. Run the project
Every launch file in this project should launch everything required to run properly the project.
### 2.1. Run the project simulation with Gazebo
```bash
cd ~/catkin_ws
source devel/setup.bash
roslaunch stage_arene_ros arene_simulation.launch
```
### 2.2. Run the project real arena while connected to the Raspberry Pi
```bash
cd ~/catkin_ws
source devel/setup.bash
roslaunch stage_arene_ros arene_real.launch
```

### 2.3. Run a checkup for the turtlebot while connected to the robot
```bash
cd ~/catkin_ws
source devel/setup.bash
roslaunch stage_arene_ros checkup.launch
```

### 2.4. Spawn the turtlebot in the simulation arena while Gazebo is running
```bash
cd ~/catkin_ws
source devel/setup.bash
roslaunch stage_arene_ros spawn_turtlebot.launch
```

## 3. Build the arena
There is 2 traffic lights tri-colored, 1 bi-colored, 2 barriers and 1 control box.
- Plug the power supply to the Raspberry Pi.
- Plug the power supply to the board.
- Check that the Raspberry Pi is linked to the arduino with the USB cable.
- Check that the shield is plugged on the arduino.
- Plug each module to the box:
  1. Traffic light tri-colored n°1
  2. Barrier n°1
  3. Traffic light tri-colored n°2
  4. Barrier n°2
  5. Traffic light bi-colored
   
(In case the order the order is mixed up, the program will not work properly, please check that the traffic lights are connected with blue wires and the barriers with yellow wires inside the box)



