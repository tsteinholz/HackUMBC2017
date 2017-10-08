# Parking Sensor Simulation for UMBC
# Thomas(Sascha) Alexander Steinholz

COMMANDS = [
    ['done', 'q', 'exits the application.'],
    ['car enter', 'j', 'simulates a car entering the parking lot.'],
    ['car exit', 'k', 'simulates a car leaving the parking lot.'],
    ['simulate', 's', 'puts the application in simulation mode.'],
    ['help', 'h', 'will display this message.']
]


def validate_input(user_input):
    """ Will return the index of cmd or -1 if invalid. """
    for index, cmd in enumerate(COMMANDS):
        if user_input == cmd[0] or user_input == cmd[1]:
            return index
    return -1

def handle_error():
    """ Handles errors ;) """
    print "ERROR: Unknown command!"

def quit_program():
    """ Quits program ;) """
    print "Finished the Parking Sensor Simulator!"
    exit()

def car_enter():
    """ TODO """
    print ""

def car_exit():
    """ TODO """
    print ""

def simulate():
    """ Every [1-5s] have a car [enter or leave]. """
    print ""

def print_help():
    """ TODO """
    print ""


def main():
    """ Program Entry Point. """

    print "\nThis program emulates a connection to a vehicle sensor which is "\
          "connected to LinkLab's Symphony Link Network which sends all the" \
          "data to LinkLab's Conductor.\n"

    # Main Loop
    while True:
        {
            -1: handle_error,
            0: quit_program,
            1: car_enter,
            2: car_exit,
            3: simulate,
            4: print_help,
        }[validate_input(input("- "))]()


main()
