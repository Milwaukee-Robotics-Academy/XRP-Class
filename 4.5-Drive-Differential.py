from XRPLib.defaults import *
import time

board = Board.get_default_board();
drivetrain = DifferentialDrive.get_default_differential_drive();


board.wait_for_button();
drivetrain.straight_distance(20);
drivetrain.turn(45);
time.sleep(2);
drivetrain.stop();