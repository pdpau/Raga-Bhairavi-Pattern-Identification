import math

def pitch_to_cents(pitch: float) -> float:
    """
    Convert pitch to cents
    """
    return 1200 * math.log2(pitch / 440)

def cents_to_pitch(cents: float) -> float:
    """
    Convert cents to pitch
    """
    return 440 * 2 ** (cents / 1200)