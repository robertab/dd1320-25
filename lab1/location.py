# Author: Robert Åberg, Sara Ervik
# Laboration 1.
# Klass

class Location:
    """
    Klass för "plats". Innehåller attributerna name,  
    ge_description, latitud, longitid, uppdateringsdatum
    """
    def __init__(self, name, geo_description, latitude, longitude, date):
        self.name = name
        self.geo_description = geo_description
        self.latitude = latitude
        self.longitude = longitude
        self.date = date

    def get_geo_description(self):
        return self.geo_description

    def get_name(self):
        return self.name

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_date(self):
        return self.date

    def __str__(self):
        return self.name + "\n" + self.geo_description + "\n" + self.latitude \
            + "\n" + self.longitude  + "\n" + self.date
