# -*- coding: utf-8 -*-

import os
from .metrics import Metric


def get_input():
    """
    Get corresponding inputs from user.

    Returns:
        A tuple such as:
            (minimum support value, metric, leverage value, filepath to parse)
    """

    try:
        minimum_support = float(input('Minimum support value:\t'))

        metric_option = int(
            input('Choose metric. Confidence[1] / Lift[2] / Leverage[3]:\t'))
        for m in Metric:
            if metric_option == m.value:
                metric_option = m
                break

        if metric_option not in Metric:
            raise ValueError("Invalid metric option -> {}"
                             .format(metric_option))

        min_threshold = float(input('Minimum metric threshold:\t'))

        filepath = input(
            'Absolute filepath which contains comma seperated values[Enter for default]:\t')

        return minimum_support, metric_option, min_threshold, filepath

    except (ValueError, TypeError) as e:
        print("{}Invalid input:{}\t{}"
              .format(os.linesep, os.linesep, e))

    except KeyboardInterrupt:
        print("Keyboard interrupt received, closing.")
        os._exit(0)

    except BaseException as e:
        print("{}Encountered unexpected exception: {}"
              .format(os.linesep, e))

    finally:
        print("Restarting input sequence." + os.linesep)
        return get_input()
