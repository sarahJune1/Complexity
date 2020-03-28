#!/usr/bin/env python
# Sarah June March 28, 2020


from fractions import Fraction


# What is the curve length of the Koch Curve at each step interval?

### Rule of Koch Curve:

# Take the segment, remove the middle third. Where the segment was cut add a segment 1/3 length of initial segment rotated at 60 degree angle.

L = 1


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
    print(f"Iteration #{iteration}")
    num_segs, seg_len = input_segs(iteration)
    print(f"Number of Segments: {num_segs}")
    print(f"Length of Segments: {seg_len}")

    L = L * (num_segs/seg_len)

    return print(f"Curve Length: {Fraction(L).limit_denominator()}")


KochCurveLength(L,0)



KochCurveLength(L,1)


for i in range(10):
    KochCurveLength(L,i)
    print("")


KochCurveLength(L,22)
