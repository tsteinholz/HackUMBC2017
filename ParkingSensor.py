"""
Parking Sensor Simulation for UMBC
by Thomas(Sascha) Alexander Steinholz
"""

from random import randint
from time import sleep

COMMANDS = [
    ['done',  'q', 'Exits the application.'],
    ['enter', 'j', 'Simulates a car entering the parking lot.'],
    ['leave', 'k', 'Simulates a car leaving the parking lot.'],
    ['sim',   's', 'Puts the application in simulation mode.'],
    ['help',  'h', 'Will display this message.']
]


def validate_input(user_input):
    """ Will return the index of cmd or -1 if invalid. """
    for index, cmd in enumerate(COMMANDS):
        if user_input == cmd[0] or user_input == cmd[1]:
            return index
    return -1

def quit_program():
    """ Quits program ;) """
    print("Finished the Parking Sensor Simulator!")
    exit()

def car_enter():
    """ TODO """
    print("")

def car_leave():
    """ TODO """
    print("")

def simulate():
    """ Every [1-5s] have a car [enter or leave]. """
    print("Started Automatic Simulation...")
    while True:
        sleep(randint(1, 5))
        (car_enter if randint(0, 1) == 0 else car_leave)()

def print_help():
    """ Print the help message ;) """
    print("Valid Commands:")
    for cmd in COMMANDS:
        print(cmd[0], "\t["+cmd[1]+"]\t-", cmd[2])


def main():
    """ Program Entry Point. """

    print( "This program emulates a connection to a vehicle sensor which is "\
          "connected to LinkLab's Symphony Link Network which sends all the" \
          "data to LinkLab's Conductor.\n")
    print_help()
    print("")

    # Main Loop
    while True:
        try:
            {
                0: quit_program,
                1: car_enter,
                2: car_leave,
                3: simulate,
                4: print_help,
            }[validate_input(input("Parking Sensor Terminal > "))]()
        except KeyError:
            print("ERROR: Unknown command!")

main()
