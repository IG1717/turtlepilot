# Turtle Pilot

## About
A simple ROS2 package which uses a PID controller to drive the turtle to a given x and y position.

## How it works
An implementation of PID can be found in `pid.py`. Two controllers are used to drive the turtle to a given position. One controller sets the turtle's angle to face the target and the other one sets the forward velocity. Only the proportional part of PID is needed here to successfully land on the target position. 

There are two ROS2 nodes included in this package: the `turtle_controller` node and the `goal_input` node. The `turtle_controller` handles the actual movement of the turtle, while the `goal_input` node allows a user to set a coordinate position as a goal for the turtle.

## Running it
First install ROS2. I use [RoboStack](https://robostack.github.io/GettingStarted.html). Then clone the repo and run:

```bash
colcon build
source install/setup.bash

# in separate windows (source in each window)
ros2 run turtlesim turtlesim_node
ros2 run controller turtle_controller
ros2 run controller goal_input
```
In the `goal_input` window, type `x y` to send the turtle to a given position.