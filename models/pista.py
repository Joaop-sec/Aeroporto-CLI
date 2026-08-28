class Pista:
    def __init__(self, id, airport_ident, ident, length_ft, width_ft, surface, closed,
                 le_lat, le_lon, le_heading, he_lat, he_lon, he_heading):
        self.id = id
        self.airport_ident = airport_ident
        self.ident = ident
        self.length_ft = length_ft
        self.width_ft = width_ft
        self.surface = surface
        self.closed = closed
        self.le_lat = le_lat
        self.le_lon = le_lon
        self.le_heading = le_heading
        self.he_lat = he_lat
        self.he_lon = he_lon
        self.he_heading = he_heading
