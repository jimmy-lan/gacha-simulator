import time


def gen_seed() -> int:
    """
    Generate a complex seed based on the current time.
    :return: Randomized seed
    """
    t = int(time.time() * 1000.0)
    return ((t & 0xff000000) >> 24) + \
           ((t & 0x00ff0000) >> 8) + \
           ((t & 0x0000ff00) << 8) + \
           ((t & 0x000000ff) << 24)
