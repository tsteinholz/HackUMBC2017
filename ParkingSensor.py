# Parking Sensor Code for UMBC

import ll_ifc

EXIT_CMD      = 'done'
EXIT_KEY      = 'q'
CAR_ENTER_CMD = 'car enter'
CAR_ENTER_KEY = 'j'
CAR_EXIT_CMD  = 'car exit'
CAR_EXIT_KEY  = 'k'
SIM_CMD       = 'simulate'
SIM_KEY       = 's'
HELP_CMD      = 'help'
HELP_KEY      = 'h'


def car_enter():
    print ""

def car_exit():
    print ""

def simulate():
    print ""

def print_help():
    print ""


def main():

    print "\nThis program emulates a connection to a vehicle sensor which is "\
          "connected to LinkLab's Symphony Link Network which sends all the" \
          "data to LinkLab's Conductor.\n"


    # Main Loop
    while True:
        user_input = input("- ")

        if user_input == EXIT_CMD or user_input == EXIT_KEY:
            break
        elif user_input == CAR_ENTER_CMD or user_input == CAR_ENTER_KEY:
            car_enter()
        elif user_input == CAR_EXIT_CMD or user_input == CAR_EXIT_KEY:
            car_exit()
        elif user_input == HELP_CMD or user_input == HELP_KEY:
            print_help()
        else:
            print "ERROR:", user_input, "is an invalid input!"

    print "Finished the Parking Sensor Simulator!"



main()
