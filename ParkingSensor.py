"""
Parking Sensor Simulation for UMBC
by Thomas(Sascha) Alexander Steinholz
"""

from multiprocessing.connection import Client
from random import randint
from time import sleep

SERVER = 'localhost'
SERVER_PORT = 7980

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

def quit_program(client):
    """ Quits program ;) """
    print("Finished the Parking Sensor Simulator!")
    client.close()
    exit()

def car_enter(client):
    """ Send car enter cmd to the server. """
    client.send('enter')

def car_leave(client):
    """ Send car leave cmd to the server. """
    client.send('leave')

def simulate(client):
    """ Every [1-5s] have a car [enter or leave]. """
    del client
    print("Started Automatic Simulation...")
    while True:
        sleep(randint(1, 5))
        (car_enter if randint(0, 1) == 0 else car_leave)()

def print_help(client):
    """ Print the help message ;) """
    del client
    print("Valid Commands:")
    for cmd in COMMANDS:
        print(cmd[0], "\t["+cmd[1]+"]\t-", cmd[2])


def main():
    """ Program Entry Point. """

    print( "This program emulates a connection to a vehicle sensor which is "\
          "connected to LinkLab's Symphony Link Network which sends all the" \
          "data to LinkLab's Conductor.\n")
    print_help(None)
    print("")

    try:
        client = Client((SERVER, SERVER_PORT))
    except ConnectionRefusedError:
        print("ERROR: Could not connect to server!")
        exit()

    # Main Loop
    while True:
        try:
            {
                0: quit_program,
                1: car_enter,
                2: car_leave,
                3: simulate,
                4: print_help,
            }[validate_input(input("Parking Sensor Terminal > "))](client)
        except KeyError:
            print("ERROR: Unknown command!")

main()
