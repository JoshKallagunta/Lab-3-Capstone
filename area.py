
def triangle_area(height, base):
    if base < 0 or height < 0:
        raise ValueError('Base and Height must be positive. ')
    return height * base * 0.5

