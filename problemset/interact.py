# -*- coding: utf-8 -*-

def get_input():

    """

    """
    
    try:
        minimum_support = float(input('Minimum support value:\t'))

        metric = input('Metric (Confidence, Lift or Leverage):\t').lower()
        if (metric not in ['confidence', 'lift', 'leverage']):
            raise ValueError()
        
        min_threshold = float(input('Minimum threshold:\t'))

        return minimum_support, metric, min_threshold

    except (ValueError, TypeError) as e:
        print("Invalid input!", e, "\n", type(e))
        get_input()
