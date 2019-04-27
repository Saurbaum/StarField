""" Tween Colours """
def tween_colours(start_colour, end_colour, progress):
    """ Tween between two colours """
    return (int(round((start_colour[0] + ((end_colour[0] - start_colour[0]) * progress)))), \
        int(round((start_colour[1] + ((end_colour[1] - start_colour[1]) * progress)))), \
            int(round((start_colour[2] + ((end_colour[2] - start_colour[2]) * progress)))))
