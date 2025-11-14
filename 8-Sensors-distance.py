from XRPLib.defaults import *
import time

board = Board.get_default_board();
drivetrain = DifferentialDrive.get_default_differential_drive();
rangefinder = Rangefinder.get_default.rangefinder();


while True:
    print(rangefinder.get_distance());
    time.sleep(0.1);

#board.wait_for_button();
#while (rangefinder.get_distance() > 10):
#    drivetrain.set_effort(0.5,0.5);
#drivetrain.stop();