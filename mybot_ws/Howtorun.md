# mybot_ws
In terminal run: catkin_make

In mybot_ws/src/mybot_control/Node
1. Run file "speakerfeatures.py" to feature extraction of .wav files
2. Run file "train.py" to training speech model
3. Run file "record.py" to record command control
4. Run file "predict.py" to choose the action
5. Run file "goforward.py" to control the robot

Run:  roslaunch mybot mybot_world.launch
to connect ros, gazebo

