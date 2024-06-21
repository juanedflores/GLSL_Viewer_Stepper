import argparse
import time
import serial

from pythonosc import udp_client

dir = 1

# s = serial.Serial('/dev/ttyACM0', 115200)

# Wake up grbl
# s.write(str.encode('\r\n\r\n'))
# time.sleep(2)   # Wait for grbl to initialize
# s.flushInput()  # Flush startup text in serial input

# Home command
# s.write(str.encode("$H\n"))
# time.sleep(6)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    while True:
        if (dir == 1):
            coord = -100
            num_range = range(0, 120, 20)
        else:
            coord = -5
            num_range = range(100, 0, -20)

        # s.write(str.encode("G01 Y" + str(coord) + " F900\n"))
        dir = -dir

        # osc message
        num_list = list(num_range)

        num_list_reverse = num_list[::-1]
        num_list.extend(num_list_reverse)
        print("num_list: " + str(num_list))
        print("num_list_reverse: " + str(num_list_reverse))
        # print("num_list_joined: " + str(num_list_joined))
        print(num_list_reverse)
        # num_list = num_list_forward.extend(num_list_reverse)
        print("dir:" + str(dir))
        print("osc: " + str(abs(coord)/100))
        for x in num_list:
            client.send_message("/alpha", abs(-x)/100)
            time.sleep(0.6)
            print(x)
        time.sleep(6.0)
