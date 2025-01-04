# File name: FromQuantsToAngle.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.polynomial.polynomial import Polynomial


def clean_and_convert(column):
    return pd.to_numeric(column, errors='coerce').dropna()


def convert_dBm_to_linear(dBm_values):
    return 10 ** (dBm_values / 10) / 1000


def calculate_angle(P5, P4, P3):
    re = (-P3 + (P4 / 2) + (P5 / 2))
    im = ((math.sqrt(3) / 2) * (-P4 + P5))
    phase_diff = math.atan2(im, re)
    angle_rad = math.asin(phase_diff / math.pi)
    angle_degrees = math.degrees(angle_rad)
    return angle_degrees


test_file = "PomiaryDoA/FirstTest_All_Measure.xlsx"
ref_file = "PomiaryAkwizycja.xlsx"
ref_data = pd.read_excel(ref_file, header=None)
test_data = pd.read_excel(test_file, sheet_name="FirstTest_10dB_0dBm_PolH_Ele", header=None)


def save_angles_to_file():
    output_file_angles = "PomiaryDoA/FirstTest_10dB_0dBm_PolH_Ele-15_angle.xlsx"
    with pd.ExcelWriter(output_file_angles, engine='openpyxl', mode='a') as writer:
        angles_data.to_excel(writer, sheet_name="FirstTest_10dB_0dBm_PolH_Ele-15", index=False)


channel1_power = clean_and_convert(ref_data.iloc[5:186, 0])
channel1_quant = clean_and_convert(ref_data.iloc[5:186, 1])
channel2_power = clean_and_convert(ref_data.iloc[5:186, 4])
channel2_quant = clean_and_convert(ref_data.iloc[5:186, 5])
channel3_power = clean_and_convert(ref_data.iloc[5:186, 8])
channel3_quant = clean_and_convert(ref_data.iloc[5:186, 9])

poly1 = Polynomial.fit(channel1_quant, channel1_power, 15)
poly2 = Polynomial.fit(channel2_quant, channel2_power, 15)
poly3 = Polynomial.fit(channel3_quant, channel3_power, 15)

test_channel1_quant = clean_and_convert(test_data.iloc[1:181, 0])
test_channel2_quant = clean_and_convert(test_data.iloc[1:181, 1])
test_channel3_quant = clean_and_convert(test_data.iloc[1:181, 2])

test_channel1_power = poly1(test_channel1_quant)
test_channel2_power = poly2(test_channel2_quant)
test_channel3_power = poly3(test_channel3_quant)

test_channel1_linear = convert_dBm_to_linear(test_channel1_power)
test_channel2_linear = convert_dBm_to_linear(test_channel2_power)
test_channel3_linear = convert_dBm_to_linear(test_channel3_power)

angles = []
for P3, P4, P5 in zip(test_channel1_linear, test_channel2_linear, test_channel3_linear):
    angle = calculate_angle(P3, P4, P5)
    angles.append(angle)

angles_data = pd.DataFrame({
    'Angles (degrees)': angles
})

save_angles_to_file()

# output_data = pd.DataFrame({
#     'Channel 1 dBm': test_channel1_power,
#     'Channel 2 dBm': test_channel2_power,
#     'Channel 3 dBm': test_channel3_power
# })
# output_file_dBm = "Calculated_dBm_Values.xlsx"
# output_data.to_excel(output_file_dBm, sheet_name="FirstTest_10dB_0dBm_PolV", index=False)

plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.scatter(channel1_quant, channel1_power, label="Channel 1 Reference", color="blue")
plt.plot(channel1_quant, poly1(channel1_quant), label="Channel 1 Polynomial Fit", color="red")
plt.legend()
plt.title("Channel 1 Polynomial Fit")
plt.xlabel("Quantization")
plt.ylabel("dBm")

plt.subplot(3, 1, 2)
plt.scatter(channel2_quant, channel2_power, label="Channel 2 Reference", color="blue")
plt.plot(channel2_quant, poly2(channel2_quant), label="Channel 2 Polynomial Fit", color="red")
plt.legend()
plt.title("Channel 2 Polynomial Fit")
plt.xlabel("Quantization")
plt.ylabel("dBm")

plt.subplot(3, 1, 3)
plt.scatter(channel3_quant, channel3_power, label="Channel 3 Reference", color="blue")
plt.plot(channel3_quant, poly3(channel3_quant), label="Channel 3 Polynomial Fit", color="red")
plt.legend()
plt.title("Channel 3 Polynomial Fit")
plt.xlabel("Quantization")
plt.ylabel("dBm")

plt.tight_layout()
plt.subplot(3, 1, 1)
plt.scatter(test_channel1_quant, test_channel1_power, label="Channel 1 Calculated", color="orange")
plt.title("Channel 1")
plt.xlabel("Quantization levels")
plt.ylabel("dBm")
plt.legend()

plt.subplot(3, 1, 2)
plt.scatter(test_channel2_quant, test_channel2_power, label="Channel 2 Calculated", color="orange")
plt.title("Channel 2")
plt.xlabel("Quantization levels")
plt.ylabel("dBm")
plt.legend()

plt.subplot(3, 1, 3)
plt.scatter(test_channel3_quant, test_channel3_power, label="Channel 3 Calculated", color="orange")
plt.title("Channel 3")
plt.xlabel("Quantization levels")
plt.ylabel("dBm")
plt.legend()

plt.tight_layout()
plt.show()

test_data = pd.read_excel(test_file, sheet_name="FirstTest_10dB_n6dBm_PolV", header=None)

test_channel1_quant = clean_and_convert(test_data.iloc[1:181, 0])
test_channel2_quant = clean_and_convert(test_data.iloc[1:181, 1])
test_channel3_quant = clean_and_convert(test_data.iloc[1:181, 2])
