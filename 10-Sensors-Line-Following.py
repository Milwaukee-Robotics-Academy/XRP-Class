from XRPLib.defaults import *
import time

board = Board.get_default_board();
drivetrain = DifferentialDrive.get_default_differential_drive();

def line_track_P():
    base_effort = 0.6;
    KP = 0.6;
    while True:
        # You always want to take the difference of the sensors because the raw value isn't always consistent.
        error = reflectance.get_left() - reflectance.get_right();
        print(error);
        drivetrain.set_effort(base_effort - error * KP, base_effort + error * KP);
        time.sleep(0.01);

def line_track_bang_bang():
    base_effort = 0.5;
    while True:
        left = reflectance.get_left();
        right = reflectance.get_right();
        if (left > right):
            drivetrain.set_effort(base_effort * 0.5, base_effort);
        else:
            drivetrain.set_effort(base_effort, base_effort * 0.5);
        time.sleep(0.01);