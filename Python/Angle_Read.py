# File name: Angle_Read.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.polynomial.polynomial import Polynomial


def limit_angle_differences(angles, max_diff=2):
    angles = list(angles)
    smoothed_angles = angles.copy()
    for i in range(1, len(angles) - 1):
        diff_prev = abs(smoothed_angles[i] - smoothed_angles[i - 1])
        diff_next = abs(smoothed_angles[i] - smoothed_angles[i + 1])
        if diff_prev > max_diff or diff_next > max_diff:
            smoothed_angles[i] = (smoothed_angles[i - 1] + smoothed_angles[i + 1]) / 2

    return smoothed_angles


def clean_and_convert(column):
    return pd.to_numeric(column, errors='coerce').dropna()


def convert_dBm_to_linear(dBm_values):
    return 10 ** (dBm_values / 10) / 1000


def calculate_angle(P5, P4, P3):
    re = (-P3 + (P4 / 2) + (P5 / 2))
    im = ((math.sqrt(3) / 2) * (-P4 + P5))
    phase_diff = math.atan2(im, re)
    phase_diff_rad = math.degrees(phase_diff)
    angle_rad = math.asin(phase_diff_rad / 180)
    angle_degrees = math.degrees(angle_rad)
    return angle_degrees


# REF DATA
angles_ref_data = pd.read_excel("angle_ref_file.xlsx", usecols=[0], skiprows=1, header=None)
angles_ref_data = angles_ref_data.iloc[:180, 0].tolist()
angles_ref_limited_90 = np.clip(angles_ref_data, -90, 90)
x_values_90 = np.linspace(-90, 90, len(angles_ref_limited_90))          # For all
mask_60 = (x_values_90 >= -60) & (x_values_90 <= 60)                         # For all
x_values_60 = x_values_90[mask_60]                                           # For all
angles_ref_limited_60 = np.array(angles_ref_limited_90)[mask_60]
angles_ref_limited_60 = limit_angle_differences(angles_ref_limited_60, 2)
poly_angle = Polynomial.fit(angles_ref_limited_60, x_values_60, 10)     # For All
polyAngleRef = poly_angle(angles_ref_limited_60)

# DATA 1 10dB_n6dBm_PolV
Test_10dB_n6dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_10dB_n6dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_n6dBm_PolV = Test_10dB_n6dBm_PolV.iloc[:180, 0].tolist()
Test_10dB_n6dBm_PolV = np.clip(Test_10dB_n6dBm_PolV, -90, 90)
Test_10dB_n6dBm_PolV_limited_60 = np.array(Test_10dB_n6dBm_PolV)[mask_60]
Test_10dB_n6dBm_PolV_limited_60 = limit_angle_differences(Test_10dB_n6dBm_PolV_limited_60, 2)
Test_10dB_n6dBm_PolV_limited_60 = poly_angle(Test_10dB_n6dBm_PolV_limited_60)

# DATA 2 10dB_n12dBm_PolV
Test_10dB_n12dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_10dB_n12dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_n12dBm_PolV = Test_10dB_n12dBm_PolV.iloc[:180, 0].tolist()
Test_10dB_n12dBm_PolV = np.clip(Test_10dB_n12dBm_PolV, -90, 90)
Test_10dB_n12dBm_PolV_limited_60 = np.array(Test_10dB_n12dBm_PolV)[mask_60]
Test_10dB_n12dBm_PolV_limited_60 = limit_angle_differences(Test_10dB_n12dBm_PolV_limited_60, 2)
Test_10dB_n12dBm_PolV_limited_60 = poly_angle(Test_10dB_n12dBm_PolV_limited_60)

# DATA 3 10dB_n18dBm_PolV
Test_10dB_n18dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_10dB_n18dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_n18dBm_PolV = Test_10dB_n18dBm_PolV.iloc[:180, 0].tolist()
Test_10dB_n18dBm_PolV = np.clip(Test_10dB_n18dBm_PolV, -90, 90)
Test_10dB_n18dBm_PolV_limited_60 = np.array(Test_10dB_n18dBm_PolV)[mask_60]
Test_10dB_n18dBm_PolV_limited_60 = limit_angle_differences(Test_10dB_n18dBm_PolV_limited_60, 2)
Test_10dB_n18dBm_PolV_limited_60 = poly_angle(Test_10dB_n18dBm_PolV_limited_60)

# DATA 4 10dB_n24dBm_PolV
Test_10dB_n24dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_10dB_n24dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_n24dBm_PolV = Test_10dB_n24dBm_PolV.iloc[:180, 0].tolist()
Test_10dB_n24dBm_PolV = np.clip(Test_10dB_n24dBm_PolV, -90, 90)
Test_10dB_n24dBm_PolV_limited_60 = np.array(Test_10dB_n24dBm_PolV)[mask_60]
Test_10dB_n24dBm_PolV_limited_60 = limit_angle_differences(Test_10dB_n24dBm_PolV_limited_60, 2)
Test_10dB_n24dBm_PolV_limited_60 = poly_angle(Test_10dB_n24dBm_PolV_limited_60)

# DATA 5 10dB_n30dBm_PolV
Test_10dB_n30dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_10dB_n30dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_n30dBm_PolV = Test_10dB_n30dBm_PolV.iloc[:180, 0].tolist()
Test_10dB_n30dBm_PolV = np.clip(Test_10dB_n30dBm_PolV, -90, 90)
Test_10dB_n30dBm_PolV_limited_60 = np.array(Test_10dB_n30dBm_PolV)[mask_60]
Test_10dB_n30dBm_PolV_limited_60 = limit_angle_differences(Test_10dB_n30dBm_PolV_limited_60, 2)
Test_10dB_n30dBm_PolV_limited_60 = poly_angle(Test_10dB_n30dBm_PolV_limited_60)

# DATA 6 0dB_n24dBm_PolV
Test_0dB_n24dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_0dB_n24dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_0dB_n24dBm_PolV = Test_0dB_n24dBm_PolV.iloc[:180, 0].tolist()
Test_0dB_n24dBm_PolV = np.clip(Test_0dB_n24dBm_PolV, -90, 90)
Test_0dB_n24dBm_PolV_limited_60 = np.array(Test_0dB_n24dBm_PolV)[mask_60]
Test_0dB_n24dBm_PolV_limited_60 = limit_angle_differences(Test_0dB_n24dBm_PolV_limited_60, 2)
Test_0dB_n24dBm_PolV_limited_60 = poly_angle(Test_0dB_n24dBm_PolV_limited_60)

# DATA 7 0dB_n30dBm_PolV
Test_0dB_n30dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_0dB_n30dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_0dB_n30dBm_PolV = Test_0dB_n30dBm_PolV.iloc[:180, 0].tolist()
Test_0dB_n30dBm_PolV = np.clip(Test_0dB_n30dBm_PolV, -90, 90)
Test_0dB_n30dBm_PolV_limited_60 = np.array(Test_0dB_n30dBm_PolV)[mask_60]
Test_0dB_n30dBm_PolV_limited_60 = limit_angle_differences(Test_0dB_n30dBm_PolV_limited_60, 2)
Test_0dB_n30dBm_PolV_limited_60 = poly_angle(Test_0dB_n30dBm_PolV_limited_60)

# DATA 8 0dB_n36dBm_PolV
Test_0dB_n36dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_0dB_n36dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_0dB_n36dBm_PolV = Test_0dB_n36dBm_PolV.iloc[:180, 0].tolist()
Test_0dB_n36dBm_PolV = np.clip(Test_0dB_n36dBm_PolV, -90, 90)
Test_0dB_n36dBm_PolV_limited_60 = np.array(Test_0dB_n36dBm_PolV)[mask_60]
Test_0dB_n36dBm_PolV_limited_60 = limit_angle_differences(Test_0dB_n36dBm_PolV_limited_60, 2)
Test_0dB_n36dBm_PolV_limited_60 = poly_angle(Test_0dB_n36dBm_PolV_limited_60)

# DATA 9 0dB_n42dBm_PolV
Test_0dB_n42dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_0dB_n42dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_0dB_n42dBm_PolV = Test_0dB_n42dBm_PolV.iloc[:180, 0].tolist()
Test_0dB_n42dBm_PolV = np.clip(Test_0dB_n42dBm_PolV, -90, 90)
Test_0dB_n42dBm_PolV_limited_60 = np.array(Test_0dB_n42dBm_PolV)[mask_60]
Test_0dB_n42dBm_PolV_limited_60 = limit_angle_differences(Test_0dB_n42dBm_PolV_limited_60, 2)
Test_0dB_n42dBm_PolV_limited_60 = poly_angle(Test_0dB_n42dBm_PolV_limited_60)

# DATA 10 0dB_n48dBm_PolV
Test_0dB_n48dBm_PolV = pd.read_excel("PomiaryDoA/FirstTest_0dB_n48dBm_PolV_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_0dB_n48dBm_PolV = Test_0dB_n48dBm_PolV.iloc[:180, 0].tolist()
Test_0dB_n48dBm_PolV = np.clip(Test_0dB_n48dBm_PolV, -90, 90)
Test_0dB_n48dBm_PolV_limited_60 = np.array(Test_0dB_n48dBm_PolV)[mask_60]
Test_0dB_n48dBm_PolV_limited_60 = limit_angle_differences(Test_0dB_n48dBm_PolV_limited_60, 2)
Test_0dB_n48dBm_PolV_limited_60 = poly_angle(Test_0dB_n48dBm_PolV_limited_60)

# DATA 11 10dB_0dBm_PolH_Ele-15
Test_10dB_0dBm_PolH_EleN15 = pd.read_excel("PomiaryDoA/FirstTest_10dB_0dBm_PolH_Ele-15_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_0dBm_PolH_EleN15 = Test_10dB_0dBm_PolH_EleN15.iloc[:180, 0].tolist()
Test_10dB_0dBm_PolH_EleN15 = np.clip(Test_10dB_0dBm_PolH_EleN15, -90, 90)
Test_10dB_0dBm_PolH_EleN15_limited_60 = np.array(Test_10dB_0dBm_PolH_EleN15)[mask_60]
Test_10dB_0dBm_PolH_EleN15_limited_60 = limit_angle_differences(Test_10dB_0dBm_PolH_EleN15_limited_60, 2)
Test_10dB_0dBm_PolH_EleN15_limited_60 = poly_angle(Test_10dB_0dBm_PolH_EleN15_limited_60)

# DATA 12 10dB_0dBm_PolH_Ele0
Test_10dB_0dBm_PolH_Ele0 = pd.read_excel("PomiaryDoA/FirstTest_10dB_0dBm_PolH_Ele0_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_0dBm_PolH_Ele0 = Test_10dB_0dBm_PolH_Ele0.iloc[:180, 0].tolist()
Test_10dB_0dBm_PolH_Ele0 = np.clip(Test_10dB_0dBm_PolH_Ele0, -90, 90)
Test_10dB_0dBm_PolH_Ele0_limited_60 = np.array(Test_10dB_0dBm_PolH_Ele0)[mask_60]
Test_10dB_0dBm_PolH_Ele0_limited_60 = limit_angle_differences(Test_10dB_0dBm_PolH_Ele0_limited_60, 2)
Test_10dB_0dBm_PolH_Ele0_limited_60 = poly_angle(Test_10dB_0dBm_PolH_Ele0_limited_60)

# DATA 13 10dB_0dBm_PolH_Ele15
Test_10dB_0dBm_PolH_Ele15 = pd.read_excel("PomiaryDoA/FirstTest_10dB_0dBm_PolH_Ele15_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_0dBm_PolH_Ele15 = Test_10dB_0dBm_PolH_Ele15.iloc[:180, 0].tolist()
Test_10dB_0dBm_PolH_Ele15 = np.clip(Test_10dB_0dBm_PolH_Ele15, -90, 90)
Test_10dB_0dBm_PolH_Ele15_limited_60 = np.array(Test_10dB_0dBm_PolH_Ele15)[mask_60]
Test_10dB_0dBm_PolH_Ele15_limited_60 = limit_angle_differences(Test_10dB_0dBm_PolH_Ele15_limited_60, 2)
Test_10dB_0dBm_PolH_Ele15_limited_60 = poly_angle(Test_10dB_0dBm_PolH_Ele15_limited_60)

# DATA 14 10dB_0dBm_PolV_Ele-15
Test_10dB_0dBm_PolV_EleN15 = pd.read_excel("PomiaryDoA/FirstTest_10dB_0dBm_PolV_Ele-15_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_0dBm_PolV_EleN15 = Test_10dB_0dBm_PolV_EleN15.iloc[:180, 0].tolist()
Test_10dB_0dBm_PolV_EleN15 = np.clip(Test_10dB_0dBm_PolV_EleN15, -90, 90)
Test_10dB_0dBm_PolV_EleN15_limited_60 = np.array(Test_10dB_0dBm_PolV_EleN15)[mask_60]
Test_10dB_0dBm_PolV_EleN15_limited_60 = limit_angle_differences(Test_10dB_0dBm_PolV_EleN15_limited_60, 2)
Test_10dB_0dBm_PolV_EleN15_limited_60 = poly_angle(Test_10dB_0dBm_PolV_EleN15_limited_60)

# DATA 15 10dB_0dBm_PolV_Ele0
Test_10dB_0dBm_PolV_Ele0 = pd.read_excel("PomiaryDoA/FirstTest_10dB_0dBm_PolV_Ele0_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_0dBm_PolV_Ele0 = Test_10dB_0dBm_PolV_Ele0.iloc[:180, 0].tolist()
Test_10dB_0dBm_PolV_Ele0 = np.clip(Test_10dB_0dBm_PolV_Ele0, -90, 90)
Test_10dB_0dBm_PolV_Ele0_limited_60 = np.array(Test_10dB_0dBm_PolV_Ele0)[mask_60]
Test_10dB_0dBm_PolV_Ele0_limited_60 = limit_angle_differences(Test_10dB_0dBm_PolV_Ele0_limited_60, 2)
Test_10dB_0dBm_PolV_Ele0_limited_60 = poly_angle(Test_10dB_0dBm_PolV_Ele0_limited_60)

# DATA 16 10dB_0dBm_PolV_Ele15
Test_10dB_0dBm_PolV_Ele15 = pd.read_excel("PomiaryDoA/FirstTest_10dB_0dBm_PolV_Ele15_angle.xlsx", usecols=[0], skiprows=1, header=None)
Test_10dB_0dBm_PolV_Ele15 = Test_10dB_0dBm_PolV_Ele15.iloc[:180, 0].tolist()
Test_10dB_0dBm_PolV_Ele15 = np.clip(Test_10dB_0dBm_PolV_Ele15, -90, 90)
Test_10dB_0dBm_PolV_Ele15_limited_60 = np.array(Test_10dB_0dBm_PolV_Ele15)[mask_60]
Test_10dB_0dBm_PolV_Ele15_limited_60 = limit_angle_differences(Test_10dB_0dBm_PolV_Ele15_limited_60, 2)
Test_10dB_0dBm_PolV_Ele15_limited_60 = poly_angle(Test_10dB_0dBm_PolV_Ele15_limited_60)

plt.figure(figsize=(10, 6))

# DATA REF
# plt.plot(x_values_90, angles_ref_limited_90, label="Reference")
# plt.plot(x_values_60, polyAngleRef, label="Reference")
plt.plot(x_values_60, polyAngleRef - x_values_60, label="Reference")

# DATA 1 10dB_n6dBm_PolV
# plt.plot(x_values_90, Test_10dB_n6dBm_PolV, label="10dB_n6dBm_PolV")
# plt.plot(x_values_60, Test_10dB_n6dBm_PolV_limited_60, label="10dB_n6dBm_PolV")
plt.plot(x_values_60, Test_10dB_n6dBm_PolV_limited_60 - x_values_60, label="10dB_n6dBm_PolV")

# DATA 2 10dB_n12dBm_PolV
# plt.plot(x_values_90, Test_10dB_n12dBm_PolV, label="10dB_n12dBm_PolV")
# plt.plot(x_values_60, Test_10dB_n12dBm_PolV_limited_60, label="10dB_n12dBm_PolV")
plt.plot(x_values_60, Test_10dB_n12dBm_PolV_limited_60 - x_values_60, label="10dB_n12dBm_PolV")

# DATA 3 10dB_n18dBm_PolV
# plt.plot(x_values_90, Test_10dB_n18dBm_PolV, label="10dB_n18dBm_PolV")
# plt.plot(x_values_60, Test_10dB_n18dBm_PolV_limited_60, label="10dB_n18dBm_PolV")
plt.plot(x_values_60, Test_10dB_n18dBm_PolV_limited_60 - x_values_60, label="10dB_n18dBm_PolV")

# DATA 4 10dB_n24dBm_PolV
# plt.plot(x_values_90, Test_10dB_n24dBm_PolV, label="10dB_n24dBm_PolV")
# plt.plot(x_values_60, Test_10dB_n24dBm_PolV_limited_60, label="10dB_n24dBm_PolV")
plt.plot(x_values_60, Test_10dB_n24dBm_PolV_limited_60 - x_values_60, label="10dB_n24dBm_PolV")

# DATA 5 10dB_n30dBm_PolV
# plt.plot(x_values_90, Test_10dB_n30dBm_PolV, label="10dB_n30dBm_PolV")
# plt.plot(x_values_60, Test_10dB_n30dBm_PolV_limited_60, label="10dB_n30dBm_PolV")
plt.plot(x_values_60, Test_10dB_n30dBm_PolV_limited_60 - x_values_60, label="10dB_n30dBm_PolV")

# DATA 6 0dB_n24dBm_PolV
# plt.plot(x_values_90, Test_0dB_n24dBm_PolV, label="0dB_n24dBm_PolV")
# plt.plot(x_values_60, Test_0dB_n24dBm_PolV_limited_60, label="0dB_n24dBm_PolV")
plt.plot(x_values_60, Test_0dB_n24dBm_PolV_limited_60 - x_values_60, label="0dB_n24dBm_PolV")

# DATA 7 0dB_n30dBm_PolV
# plt.plot(x_values_90, Test_0dB_n30dBm_PolV, label="0dB_n30dBm_PolV")
# plt.plot(x_values_60, Test_0dB_n30dBm_PolV_limited_60, label="0dB_n30dBm_PolV")
plt.plot(x_values_60, Test_0dB_n30dBm_PolV_limited_60 - x_values_60, label="0dB_n30dBm_PolV")

# DATA 8 0dB_n36dBm_PolV
# plt.plot(x_values_90, Test_0dB_n36dBm_PolV, label="0dB_n36dBm_PolV")
# plt.plot(x_values_60, Test_0dB_n36dBm_PolV_limited_60, label="0dB_n36dBm_PolV")
plt.plot(x_values_60, Test_0dB_n36dBm_PolV_limited_60 - x_values_60, label="0dB_n36dBm_PolV")

# DATA 9 0dB_n42dBm_PolV
# plt.plot(x_values_90, Test_0dB_n42dBm_PolV, label="0dB_n42dBm_PolV")
# plt.plot(x_values_60, Test_0dB_n42dBm_PolV_limited_60, label="0dB_n42dBm_PolV")
plt.plot(x_values_60, Test_0dB_n42dBm_PolV_limited_60 - x_values_60, label="0dB_n42dBm_PolV")

# DATA 10 0dB_n48dBm_PolV
# plt.plot(x_values_90, Test_0dB_n48dBm_PolV, label="0dB_n48dBm_PolV")
# plt.plot(x_values_60, Test_0dB_n48dBm_PolV_limited_60, label="0dB_n48dBm_PolV")
plt.plot(x_values_60, Test_0dB_n48dBm_PolV_limited_60 - x_values_60, label="0dB_n48dBm_PolV")
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# DATA 11 10dB_0dBm_PolH_EleN15
# plt.plot(x_values_90, Test_10dB_0dBm_PolH_EleN15, label="10dB_0dBm_PolH_Ele-15")
# plt.plot(x_values_60, Test_10dB_0dBm_PolH_EleN15_limited_60, label="10dB_0dBm_PolH_Ele-15")
# plt.plot(x_values_60, Test_10dB_0dBm_PolH_EleN15_limited_60 - x_values_60, label="10dB_0dBm_PolH_Ele-15")
#
# DATA 12 10dB_0dBm_PolH_Ele0
# plt.plot(x_values_90, Test_10dB_0dBm_PolH_Ele0, label="10dB_0dBm_PolH_Ele0")
# plt.plot(x_values_60, Test_10dB_0dBm_PolH_Ele0_limited_60, label="10dB_0dBm_PolH_Ele0")
# plt.plot(x_values_60, Test_10dB_0dBm_PolH_Ele0_limited_60 - x_values_60, label="10dB_0dBm_PolH_Ele0")

# DATA 13 10dB_0dBm_PolH_Ele15
# plt.plot(x_values_90, Test_10dB_0dBm_PolH_Ele15, label="10dB_0dBm_PolH_Ele15")
# plt.plot(x_values_60, Test_10dB_0dBm_PolH_Ele15_limited_60, label="10dB_0dBm_PolH_Ele15")
# plt.plot(x_values_60, Test_10dB_0dBm_PolH_Ele15_limited_60 - x_values_60, label="10dB_0dBm_PolH_Ele15")

# # DATA 14 10dB_0dBm_PolV_EleN15
# plt.plot(x_values_90, Test_10dB_0dBm_PolV_EleN15, label="10dB_0dBm_PolV_Ele-15")
# plt.plot(x_values_60, Test_10dB_0dBm_PolV_EleN15_limited_60, label="10dB_0dBm_PolV_Ele-15")
# plt.plot(x_values_60, Test_10dB_0dBm_PolV_EleN15_limited_60 - x_values_60, label="10dB_0dBm_PolV_Ele-15")
#
# # DATA 15 10dB_0dBm_PolV_Ele0
# plt.plot(x_values_90, Test_10dB_0dBm_PolV_Ele0, label="10dB_0dBm_PolV_Ele0")
# plt.plot(x_values_60, Test_10dB_0dBm_PolV_Ele0_limited_60, label="10dB_0dBm_PolV_Ele0")
# plt.plot(x_values_60, Test_10dB_0dBm_PolV_Ele0_limited_60 - x_values_60, label="10dB_0dBm_PolV_Ele0")
#
# # DATA 16 10dB_0dBm_PolV_Ele15
# plt.plot(x_values_90, Test_10dB_0dBm_PolV_Ele15, label="10dB_0dBm_PolV_Ele15")
# plt.plot(x_values_60, Test_10dB_0dBm_PolV_Ele15_limited_60, label="10dB_0dBm_PolV_Ele15")
# plt.plot(x_values_60, Test_10dB_0dBm_PolV_Ele15_limited_60 - x_values_60, label="10dB_0dBm_PolV_Ele15")

plt.rcParams['font.size'] = 16
plt.tick_params(axis='both', which='major', labelsize=22)
plt.xlabel("Real angles (degrees)", fontsize=22)
# plt.ylabel("Measured angles (degrees)", fontsize=22)
plt.ylabel("Measured angles - Real angles (degrees)", fontsize=20)
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.show()
