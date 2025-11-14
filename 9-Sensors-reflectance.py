from XRPLib.defaults import *
import time

board = Board.get_default_board();
drivetrain = DifferentialDrive.get_default_differential_drive();

while True:
    print("Right", reflectance.get_right_reflectance());
    print("Left", reflectance.get_left_reflectance());
    time.sleep(0.1);