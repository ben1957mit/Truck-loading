def weight_okay(total_weight, max_weight):
    return total_weight <= max_weight

def axle_split(total_weight):
    steer = total_weight * 0.12
    drive = total_weight * 0.43
    tandem = total_weight * 0.45
    return steer, drive, tandem
