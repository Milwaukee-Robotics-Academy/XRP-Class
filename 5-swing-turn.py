from XRPLib.defaults import *
import time

board = Board.get_default_board();
drivetrain = DifferentialDrive.get_default_differential_drive();

board.wait_for_button();
drivetrain.set_speed(5,0);
time.sleep(3);
drivetrain.stop();
