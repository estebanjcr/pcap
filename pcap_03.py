def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100000 / 1609.344
    gallons_per_100km = liters / 3.785411784
    miles_per_gallon = miles_per_100km / gallons_per_100km
    return miles_per_gallon
    

def miles_gallon_to_liters_100km(miles):
    km_per_gallon = miles * 1.609344
    liters_per_100km = 100 / km_per_gallon * 3.785411784
    return liters_per_100km
    
    user_input = input("Enter ...")