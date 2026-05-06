import pint

ureg = pint.UnitRegistry()

def convert_to_meters(value, unit):
    """Przelicza wartość na metry."""
    quantity = value * ureg(unit)
    return quantity.to(ureg.meter).magnitude