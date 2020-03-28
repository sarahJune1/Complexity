#!/usr/bin/env python
# Sarah June March 28, 2020
"""
Calculate length of Koch Curve
Input: 
    Initial length of curve
    Iteration level
Output:
    Lenth of Koch Curve at iteration level
"""


from fractions import Fraction
import sys

if not len(sys.argv) == 3:
    print('''INPUT USAGE:
    $python KochCurve.py <Segment_Length> <Iteration> ''')
    sys.exit()


# What is the curve length of the Koch Curve at each step interval?

### Rule of Koch Curve:

# Take the segment, remove the middle third. 
# For each cut segment add a new segment 1/3 length and rotate at 60 degree angle

L, Iteration_Level = sys.argv[1:]


def input_segs(iteration):
    """
    Input parameters for segment of Koch Curve:
        At each iteration:

            num_seg = Number of segments to count
                Segment L is multiplied by 4 because of rule, where 1 segment is now considered 4 segments
                Exponentially grow by the iteartion step

            seg_len = Length of each segment
                Length of each num_seg is 1/3 of original

    """
    num_segs = 4**iteration
    seg_len = 3**iteration
    return num_segs, seg_len


def KochCurveLength(L, iteration):
    """
    L = Segment Length
    Count number of Segments at each interval following the rule
    Output curve length
    """
    print(f"Steps Taken: {iteration}")
    num_segs, seg_len = input_segs(iteration)
    print(f"Number of Segments: {num_segs}")
    print(f"Length of Segments: {seg_len}")

    L = L * (num_segs/seg_len)

    return print(f"Curve Length: {Fraction(L).limit_denominator()}")


KochCurveLength(float(L),float(Iteration_Level))

