import hid
import time

vendor_id = 1699
multi_id = 3334
radio_id = 3333

multi = hid.device()
multi.open(vendor_id, multi_id)
multi.set_nonblocking(True)

radio = hid.device()
radio.open(radio_id, radio_id)
radio.set_nonblocking(True)

multi.write(
    [
        0b00000001,  # Upper row, digit 1
        0b00000001,  # Upper row, digit 2
        0b00000001,  # Upper row, digit 3
        0b00000001,  # Upper row, digit 4
        0b00000001,  # Upper row, digit 5
        0b00000001,  # Upper row, digit 1
        0b00000001,  # Lower row, digit 2
        0b00000001,  # Lower row, digit 3
        0b00000001,  # Lower row, digit 4
        0b11011110,  # Lower row, digit 5
        0b11111111,  # Lights
    ]
)

radio.write(
    [
        0b00000001,  # Upper row, left, digit 1
        0b00000001,  # Upper row, left, digit 2
        0b00000001,  # Upper row, left, digit 3
        0b00000001,  # Upper row, left, digit 4
        0b00000001,  # Upper row, left, digit 5
        0b00000001,  # Upper row, right, digit 1
        0b00000001,  # Upper row, right, digit 2
        0b00000001,  # Upper row, right, digit 3
        0b00000001,  # Upper row, right, digit 4
        0b00000001,  # Upper row, right, digit 5
        0b00000001,  # Lower row, left, digit 1
        0b00000001,  # Lower row, left, digit 2
        0b00000001,  # Lower row, left, digit 3
        0b11100001,  # Lower row, left, digit 4
        0b00000001,  # Lower row, left, digit 5
        0b00000001,  # Lower row, right, digit 1
        0b00000001,  # Lower row, right, digit 2
        0b00000001,  # Lower row, right, digit 3
        0b00000001,  # Lower row, right, digit 4
        0b00000001,  # Lower row, right, digit 5
    ]
)


def hdg_pressed(data):
    return data[1] & 0b00000001


def nav_pressed(data):
    return data[1] & 0b00000010


while True:
    time.sleep(0.5)

    data_multi = multi.read(64)
    if data_multi:
        if hdg_pressed(data_multi):
            print("HDG pressed")

        if nav_pressed(data_multi):
            print("NAV pressed")

    data_radio = radio.read(64)
    if data_radio:
        print("Data_radio: ", data_radio)
