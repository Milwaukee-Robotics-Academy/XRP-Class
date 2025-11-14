from XRPLib.defaults import *
import time

board = Board.get_default_board();



board.wait_for_button();
left_motor.set_effort(0.5);
right_motor.set_effort(0.5);
time.sleep(2);
left_motor.set_effort(0);
right_motor.set_effort(0);
