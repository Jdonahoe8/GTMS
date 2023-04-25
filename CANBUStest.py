import can

# Candlelight firmware on Linux
#bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)


# Stock slcan firmware on Windows
bus = can.interface.Bus( channel='COM0', bitrate=500000)



try:
    bus.send(msg)
    print("Message sent on {}".format(bus.channel_info))
except can.CanError:
    print("Message NOT sent")
