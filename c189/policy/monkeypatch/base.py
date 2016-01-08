years_range = (-17,10)

patched_years_range = lambda : years_range

def apply_patched_const(scope, original, replacement):
    setattr(scope, original, replacement())
    return