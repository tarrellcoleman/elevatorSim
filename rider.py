from elevatorController import ElevatorController
class Rider:

    def __init__(self):
        self.elevator = ElevatorController()
        
    
    def validation(self, userInput):
        class OutOfRangeError(Exception):
            "Building does not have this floor"
            pass

        isValid = True
        try:
            if not int(userInput):
                raise ValueError
            elif int(userInput) > 5 or int(userInput) < 1:
                raise OutOfRangeError
            
        except OutOfRangeError:
            print("This floor does not exist.")
            isValid = False
        except ValueError:
            print("Oops you press wrong button.")
            isValid = False
        except Exception:
            print("Oops you press wrong button.")
            isValid = False

        return isValid


    def callElevator(self):
        currentFloor = input("Current Floor:")
        if not self.validation(currentFloor) : self.callElevator()
        userDestination = input ("Destination:")
        if not self.validation(userDestination) : self.callElevator()
        self.elevator.move(userDestination, currentFloor)