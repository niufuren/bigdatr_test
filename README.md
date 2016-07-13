## Drone coding test for Bigdatr

### Requirement

- install python 2.7
- install pip
- `pip install nose` (python unit test tool)

### Run code

Part1: `python src/drone.py input.txt`

Part2: `python src/multiple_drone.py input.txt`

### Output

Part1:     
   The number of billboards that are captured at least once is 997  
   The coordinate of the final location of the drone is (13, 138)

Part2:    
   The number of billboards that are captured by two drones at least once is 955  
   The coordinate of the final location of the first drone is (-29, 52)  
   The coordinate of the final location of the second drone is (42, 86)

### Run test

`nosetests`