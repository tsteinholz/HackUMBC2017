"""
The sign display server
by Thomas(Sascha) Alexander Steinholz
"""

from multiprocessing.connection import Listener
from time import sleep
from _thread import start_new_thread, allocate_lock


SERVER_PORT = 7980
parking_access_lock = allocate_lock()
parking_directory = []
progress_bars = []

def start_server():
    """ Add new connections as they come in. """
    server = Listener(('', SERVER_PORT))
    print("[+] Server Created.")
    while True:
        connection = server.accept()
        print("[+] Connected to Parking Sensor", str(connection.fileno()) + ".")
        start_new_thread(client_thread, (connection,))

def update_parking(identifier, direction):
    """ Safely update the parking_directory slot count. """
    with parking_access_lock:
        # Find the identifier in the directory.
        for lot in parking_directory:
            if identifier == lot[0]:
                if direction == 'enter':
                    lot[1] += 1
                    return
                elif direction == 'leave':
                    if lot[1] > 0:
                        lot[1] -= 1
                    return
                else:
                    print("[!] Error: Unknown message from", identifier)
                    return

        # Add the new key in the directory if not found.
        parking_directory.append([identifier, 1 if direction == 'enter' else 0])

def client_thread(conn):
    """ Handles a client thread, """
    while True:
        try:
            msg = conn.recv()
        except EOFError:
            print("[-] Disconnected from Parking Sensor", str(conn.fileno()) + ".")
            conn.close()
            return
        #print(conn.fileno(), "]", msg)
        update_parking(conn.fileno(), msg)

def render_parking_spots():
        with parking_access_lock:
            print("")
            for index, lot in enumerate(parking_directory):
                print("=============================================")
                print("Parking Lot #" + str(index + 1), " || Avalible Spots: ", 150 - lot[1], "/ 150")
                print("=============================================")

def main():
    """ Program Entry Point. """
    start_new_thread(start_server, ())
    while True:
        render_parking_spots()
        sleep(3)


main()
