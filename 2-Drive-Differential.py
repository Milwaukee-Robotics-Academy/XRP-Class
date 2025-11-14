from XRPLib.defaults import *
import time

board = Board.get_default_board();
drivetrain = DifferentialDrive.get_default_differential_drive();

#def turnArc(radius, angle, speed):


board.wait_for_button();
drivetrain.set_speed(0.5);
time.sleep(2);
drivetrain.stop();