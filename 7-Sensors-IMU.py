from XRPLib.defaults import *
import time

board = Board.get_default_board();
drivetrain = DifferentialDrive.get_default_differential_drive();

def imu_test():
    while True:
        print(f"Pitch: {imu.get_pitch()}, Yaw: {imu.get_yaw()}, Roll: {imu.get_roll()}, Accelerometer output: {imu.get_acc_rates()}")
        time.sleep(0.1)

def turn_degrees(degrees):
    drivetrain.turn_degrees(degrees, speed=5);
    
def turn_using_imu(target_yaw):
    kp = 0.01
    while True:
        current_yaw = imu.get_yaw()
        error = target_yaw - current_yaw
        if abs(error) < 1:
            break
        turn_effort = kp * error
        drivetrain.set_effort(-turn_effort, turn_effort)
        time.sleep(0.01)
    drivetrain.stop()

imu_test();