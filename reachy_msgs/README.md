# Reachy 2021 messages

Custom ROS2 messages and services used by Reachy's ROS2 packages.

**ROS2 Version: Foxy**

How to install:

```bash
cd ~/reachy_ws/src
git clone https://github.com/pollen-robotics/reachy_msgs.git
cd ~/reachy_ws/
colcon build --packages-select reachy_msgs
```

## Messages
* **ForceSensor.msg**
* **JointTemperature.msg**
* **PidGains.msg**
* **FanState.msg**

## Services
* **GetArmFK.srv** - Carry out the forward kinematics computation for Reachy's arm.
* **GetArmIK.srv** - Carry out the inverse kinematics computation for Reachy's arm.
* **JointFullState.srv** - Return positon, speed, effort, temperature, compliance, goal position, speed limit, torque limit and the PID gains of the requested joints.
* **GetOrbitaIK.srv** - Carry out the inverse kinematics computation for Orbita.
* **GetQuaternionTransform.srv** - Compute the quaternion to reach the requested vector in the *look_out* function.
* **SetCameraZoomLevel.srv** - Send command to the zoom of a given camera.
* **SetCameraZoomSpeed.srv** - Send speed to the zoom of a given camera.
* **SetFanState.srv** - Set the requested fans to the requested states. (True = on / False = off).
* **SetJointCompliancy.srv** - Set the requested joints to the requested compliance level. (True = Compliant / False = Stiff)
* **SetJointPidGains.srv** - Set the requested PID gains (see the joint documentation for more information on how the different values are used).
* **GetReachyModel.srv** - Get Reachy's configuration and mobile base version (if a mobile base is connected).
---

This package is part of the ROS2-based software release of the version 2021 of Reachy.

Visit [pollen-robotics.com](https://pollen-robotics.com) to learn more or visit [our forum](https://forum.pollen-robotics.com) if you have any questions.
