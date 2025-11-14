from XRPLib.defaults import *
import time

board = Board.get_default_board();


board.wait_for_button();
left_motor.set_speed(5);
right_motor.set_speed(-5);
time.sleep(3);
left_motor.set_speed(0);
right_motor.set_speed(0);
