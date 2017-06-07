def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        try:
            int(pin)
        except ValueError:
            return False
        return True
    else:
        return False