import serial
import time
import re

NUM_CHANNELS = 4


def log_to_file(averages, filename, attenuation_value):
    try:
        with open(filename, "a") as file:
            file.write(" ".join(str(avg) for avg in averages) + f" {attenuation_value}\n")
    except Exception as e:
        print(f"Error while writing to file: {e}")


def parse_response(serial_connection, command='m\n'):
    max_attempts = 5
    for attempt in range(1, max_attempts + 1):
        try:
            serial_connection.write(command.encode('utf-8'))
            time.sleep(0.5)
            response = serial_connection.readline().decode('utf-8').strip()
            response = re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', response)
            values = response.split()
            if len(values) == NUM_CHANNELS:
                return [int(val) for val in values]
        except (ValueError, serial.SerialException):
            pass
    return []


def read_attenuation_value(filename):
    try:
        with open(filename, "r") as file:
            value = file.readline().strip()
            value = int(value)
            if 0 <= value <= 63:
                return value
            else:
                print(f"Invalid attenuation value. It must be between 0 and 63. Value read: {value}")
                return None
    except Exception as e:
        print(f"Error reading attenuation file: {e}")
        return None


def send_attenuation_value(serial_port, baud_rate, attenuation_value):
    try:
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
            if not ser.is_open:
                print(f"Error: Unable to open port {serial_port}")
                return
            if 0 <= attenuation_value <= 9:
                match attenuation_value:
                    case 0:
                        ser.write(b'a\n')
                    case 1:
                        ser.write(b'b\n')
                    case 2:
                        ser.write(b'c\n')
                    case 3:
                        ser.write(b'd\n')
                    case 4:
                        ser.write(b'e\n')
                    case 5:
                        ser.write(b'f\n')
                    case 6:
                        ser.write(b'g\n')
                    case 7:
                        ser.write(b'h\n')
                    case 8:
                        ser.write(b'i\n')
                    case 9:
                        ser.write(b'j\n')
            elif 10 <= attenuation_value <= 63:
                attenuation_data = f"{attenuation_value}"
                ser.write(attenuation_data.encode('utf-8'))
                print(f"Sent attenuation value: {attenuation_value}")

            else:
                print(f"Error: Invalid attenuation value {attenuation_value}. Must be between 0 and 9.")

            time.sleep(0.6)
            while ser.in_waiting > 0:
                ser.readline()

    except serial.SerialException as e:
        print(f"Error during serial communication: {e}")


def communicate_with_device(port, baud_rate, output_file, attenuation_value):
    try:
        with serial.Serial(port, baud_rate, timeout=1) as ser:
            if not ser.is_open:
                return
            averages = parse_response(ser)
            if averages:
                log_to_file(averages, output_file, attenuation_value)
    except serial.SerialException:
        pass


def get_output_file_name(default_filename="PowerMSFDoAE.txt"):
    try:
        with open("Name.txt", "r") as file:
            name = file.readline().strip()
            if name:
                return name
    except FileNotFoundError:
        pass
    return default_filename


def main():
    serial_port = "COM4"
    baud_rate = 115200
    output_file = get_output_file_name()
    attenuation_file = "AttLvl.txt"

    attenuation_value = read_attenuation_value(attenuation_file)

    if attenuation_value is not None:
        send_attenuation_value(serial_port, baud_rate, attenuation_value)

    time.sleep(0.5)
    communicate_with_device(serial_port, baud_rate, output_file, attenuation_value)


if __name__ == "__main__":
    main()

# pyinstaller --onefile --name=MSFDoAEpomiar MSFDoAEpomiar.py
