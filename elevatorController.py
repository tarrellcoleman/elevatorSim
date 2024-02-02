import time

class ElevatorController:

    def __init__(self):
        #Initialize the elevator with 5 floor starting at floor 0
        self.numFloors = 5
        self.currentFloor = 0


    def elevatorPosition(self, startingPosition, nextPosition):
        if startingPosition < nextPosition:
            self.currentFloor += 1
        elif startingPosition > nextPosition:
            self.currentFloor -= 1

        self.move(nextPosition, startingPosition)
    

    def move(self, destination, sourceFloor):
        sourceFloor = int(sourceFloor)
        destination = int(destination)
       
        #Determine direction of movement based on destination
        if destination > self.currentFloor:
            direction = "↑" #Elevator going up
        elif destination < self.currentFloor:
            direction = "↓" #Elevator going down
        else:
            direction = None  #No movement

        if sourceFloor == destination:
            direction = None

        if direction is not None:
            #Changing currentFloor to the user's inital floor
            self.currentFloor = sourceFloor if self.currentFloor == 0 else self.currentFloor
            if sourceFloor is self.currentFloor:
                #Display the initial confirmation of destination and direction for user
                print(f"Moving from floor {self.currentFloor} {direction} to floor {destination}")
                self.elevatorPosition(sourceFloor, destination)
            elif sourceFloor is not destination:
                #Display current floor and direction to user
                print(f"Floor {self.currentFloor} {direction}")
                #Simulate travel time with a delay
                time.sleep(3)
                self.elevatorPosition(sourceFloor, destination)
        else:
            if self.currentFloor != 0 and self.currentFloor is destination:
                print(f"You have arrived on {destination}")
                self.currentFloor = 0
            else:
                print("You already on your floor, please enter a new destination.")
                return