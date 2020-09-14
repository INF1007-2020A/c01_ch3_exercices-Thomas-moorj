#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
def average(a: float, b: float, c: float) -> float:
   
    return  (a+b+c)/3.0


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    
    return math.radians(angle_degs + angle_mins / 60 + angle_secs /3600)


def to_degrees(angle_rads: float) -> tuple:
    
    degrees= angle_rads% math.pi
    angle_rads = angle_rads-degrees
    minutes= angle_rads % 60
    angle_rads = angle_rads-minutes
    seconds= angle_rads /3600.0
    return degrees, minutes, seconds


def to_celsius(temperature: float) -> float:
    return 


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.0, 4.0, 6.0)}")
    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
