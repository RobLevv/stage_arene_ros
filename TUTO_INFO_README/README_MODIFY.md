# How To MODIFY this project
## 1. Modify the software
### 1.1. Modify the Arduino code
The Arduino code is located in the folder `arduino_script`. It is composed of 2 files:
#### 1.1.1. `arduino_arena_receiver.c`
This file is the main file. It is the one that is uploaded to the Arduino.
It is composed of a main loop that is executed indefinitely and choosing between 4 states:
- 'Opening the 1st barrier'
- 'Opening the 2nd barrier'
- 'Closing the 1st barrier'
- 'Closing the 2nd barrier'
The traffic lights are linked to the barriers so that they are green when the barrier is open and red when the barrier is closed. Those functions are implemented in this file. To modify the behavior of the traffic lights, you have to modify the functions `open_barrier()` and `close_barrier()`.
#### 1.1.2. `communication_arduino.py`
This file is the one that is executed on the Raspberry Pi. It allows the communication between the Arduino and the Raspberry Pi. It is composed of 2 functions:
- `callback()`: This function is called when a message is received on the topic `arene/cmd`, it makes the Arduino execute the command received.
- `send_to_arduino()`: This function sends a number to the arduino on the serial port. This number is the command that the Arduino will execute.
The main function of this files initializes the node and the subscriber to the topic `arene/cmd`.
### 1.2. Modify the Launch files
The launch files are located in the folder `launch`. There are 4 launch files:
#### 1.2.1. `arene_real.launch`
This launch file is used to launch the project on the real arena. It launches the node `communication_arduino.py` and an example of a node that sends commands to the Arduino.
To modify, remove the node that sends commands to the Arduino and replace it with your own node.
#### 1.2.2. `arene_simulation.launch`
This launch file is used to launch the project on the simulation arena. It launches Gazebo and initializes the world with the arena and the turtlebot. It contains the `world_control` node that sends commands to the Arduino automatically. There is also an example of teleop and world control nodes.
To modify, remove the `world_control` node and replace it with your own automatic control node or remove the `example_control` node and replace it with your own control node.

### 1.3. Modify the scripts