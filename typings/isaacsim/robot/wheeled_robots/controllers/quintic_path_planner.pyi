"""

Quintic Polynomials Planner
author: Atsushi Sakai (@Atsushi_twi)
Source: https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/QuinticPolynomialsPlanner/quintic_polynomials_planner.py
Distributed under the MIT license:
The MIT License (MIT)

Copyright (c) 2016 - 2021 Atsushi Sakai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Ref:
- [Local Path planning And Motion Control For Agv In Positioning](http://ieeexplore.ieee.org/document/637936/)

CHANGELOG:
[2021-11-19]
- Remove __main__ function
- Remove plot and animation function
- Code formatting
"""
from __future__ import annotations
import math as math
import numpy as np
__all__ = ['MAX_T', 'MIN_T', 'QuinticPolynomial', 'math', 'np', 'quintic_polynomials_planner']
class QuinticPolynomial:
    def __init__(self, xs, vxs, axs, xe, vxe, axe, time):
        ...
    def calc_first_derivative(self, t):
        ...
    def calc_point(self, t):
        ...
    def calc_second_derivative(self, t):
        ...
    def calc_third_derivative(self, t):
        ...
def quintic_polynomials_planner(sx, sy, syaw, sv, sa, gx, gy, gyaw, gv, ga, max_accel, max_jerk, dt):
    """
    quintic polynomials planner
    
        Args:
            sx (_type_): start x position [m]
            sy (_type_): start y position [m]
            syaw (_type_): start yaw angle [rad]
            sv (_type_): start velocity [m/s]
            sa (_type_): start accel [m/ss]
            gx (_type_): goal x position [m]
            gy (_type_): goal y position [m]
            gyaw (_type_): goal yaw angle [rad]
            gv (_type_): goal velocity [m/s]
            ga (_type_): goal accel [m/ss]
            max_accel (_type_): maximum accel [m/ss]
            max_jerk (_type_): maximum jerk [m/sss]
            dt (_type_): time tick [s]
    
        Returns:
            time: time result
            rx: x position result list
            ry: y position result list
            ryaw: yaw angle result list
            rv: velocity result list
            ra: accel result list
    
        
    """
MAX_T: float = 100.0
MIN_T: float = 5.0
