# DataServer1.py

from threading import Thread
import socket
import time
#import RPi.GPIO as GPIO

VERBOSE = False
IP_PORT = 9080
#P_BUTTON = 24 # adapt to your wiring

#def setup():
#    GPIO.setmode(GPIO.BOARD)
#    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

def debug(text):
    if VERBOSE:
        print("Debug:---", text)

# ---------------------- class SocketHandler ------------------------
class SocketHandler(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):
        global isConnected
        debug("SocketHandler started")
        while True:
            cmd = ""
            try:
                debug("Calling blocking conn.recv()")
                cmd = self.conn.recv(1024)
            except:
                debug("exception in conn.recv()") 
                # happens when connection is reset from the peer
                break
            debug("Received cmd: " + cmd.decode("utf-8") + " len: " + str(len(cmd.decode("utf-8"))))
            if len(cmd) == 0:
                break
            self.executeCommand(cmd)
        conn.close()
        print("Client disconnected. Waiting for next client...")
        isConnected = False
        debug("SocketHandler terminated")

    def executeCommand(self, cmd):
        debug("Calling executeCommand() with  cmd: " + cmd.decode("utf-8"))

        if cmd.decode("utf-8")[:4] == "syst":  # remove trailing "\0"
            if cmd.decode("utf-8")[5:] == "stp":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])

        elif cmd.decode("utf-8")[:4] == "move":  # remove trailing "\0"
            if cmd.decode("utf-8")[5:] == "fwd":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "bwd":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "lft":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "rht":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "stp":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sw01":  # remove trailing "\0"
            if cmd.decode("utf-8")[5:] == "_on":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "off":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
              
            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sw02":  # remove trailing "\0"
            if cmd.decode("utf-8")[5:] == "_on":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "off":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
              
            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sw03":  # remove trailing "\0"
            if cmd.decode("utf-8")[5:] == "_on":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "off":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
              
            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sw04":  # remove trailing "\0"
            if cmd.decode("utf-8")[5:] == "_on":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "off":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
              
            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sw05":  # remove trailing "\0"
            if cmd.decode("utf-8")[5:] == "_on":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "off":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
              
            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sw06":  # remove trailing "\0"
            if cmd.decode("utf-8")[5:] == "_on":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
                
            elif cmd.decode("utf-8")[5:] == "off":
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])
              
            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sl01":  # remove trailing "\0"
            global SLValue1
            try:
                SLValue1 = int(cmd.decode("utf-8")[5:])

            except:
                pass

            print("")

            if isinstance(SLValue1, int) == True :
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])

            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sl02":  # remove trailing "\0"
            global SLValue2
            try:
                SLValue2 = int(cmd.decode("utf-8")[5:])

            except:
                pass

            print("")

            if isinstance(SLValue2, int) == True :
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])

            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sl03":  # remove trailing "\0"
            global SLValue3
            try:
                SLValue3 = int(cmd.decode("utf-8")[5:])

            except:
                pass

            print("")

            if isinstance(SLValue3, int) == True :
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])

            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sl04":  # remove trailing "\0"
            global SLValue4
            try:
                SLValue4 = int(cmd.decode("utf-8")[5:])

            except:
                pass

            print("")

            if isinstance(SLValue4, int) == True :
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])

            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sl05":  # remove trailing "\0"
            global SLValue5
            try:
                SLValue5 = int(cmd.decode("utf-8")[5:])

            except:
                pass

            print("")

            if isinstance(SLValue5, int) == True :
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])

            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")


        elif cmd.decode("utf-8")[:4] == "sl06":  # remove trailing "\0"
            global SLValue6
            try:
                SLValue6 = int(cmd.decode("utf-8")[5:])

            except:
                pass

            print("")

            if isinstance(SLValue6, int) == True :
                print(cmd.decode("utf-8")[:4] + " = " + cmd.decode("utf-8")[5:])

            else:
                print(cmd.decode("utf-8")[:4] + " = " + "cmd error")

        else:
            print("")


#            if GPIO.input(P_BUTTON) == GPIO.LOW:
#                state = "Button pressed"
#            else:
#                state = "Button released"
#            print("Reporting current state:", state)
#            self.conn.sendall(state + "\0")
# ----------------- End of SocketHandler -----------------------

#setup()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# close port when process exits:
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
debug("Socket created")
HOSTNAME = "" # Symbolic name meaning all available interfaces
try:
    serverSocket.bind((HOSTNAME, IP_PORT))
except socket.error as msg:
    print("Bind failed", msg[0], msg[1])
#    sys.exit()
serverSocket.listen(10)

print("Waiting for a connecting client...")
isConnected = False
while True:
    debug("Calling blocking accept()...")
    conn, addr = serverSocket.accept()
    print("Connected with client at " + addr[0])
    isConnected = True
    socketHandler = SocketHandler(conn)
    # necessary to terminate it at program termination:
    socketHandler.setDaemon(True)  
    socketHandler.start()
#    t = 0
#    while isConnected:
#        print("Server connected at", t, "s")
#        time.sleep(10)
#        t += 10

