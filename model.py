import json
import math

class Agent:
	"""docstring for Agent"""
	def say_hello(sef, first_name):
		return "Bien le bonjour"+first_name+" !"

	def __init__(self, **agent_attributes):
		for attr_name, attr_value in agent_attributes.items():
			# set attribute
			setattr(self, attr_name,attr_name)
class Possition:
	"""docstring for ClassName"""
	def __init__(self, longitude, latitude):
		self.latitude = latitude
		self.longitude = longitude

class Zone:
	MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1 # degrees of longitude
    HEIGHT_DEGREES = 1 # degrees of latitude
    ZONES = []
    EARTH_RADIUS_KILOMETERS = 6371

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = 0
		longitude = self.MIN_LONGITUDE_DEGREES

	def add_inhabitants(self,inhabitant):
		self.inhabitants.append(inhabitant)

	@property
	def population(self):
		return len(self.inhabitants)

	@property
	def width(self):
		return abs(self.corner1.longitude - self.corner2.longitude)*self.EARTH_RADIUS_KILOMETERS
	
	@property
	def height(self):
		return abs(self.corner1.longitude - self.corner2.longitude)*self.EARTH_RADIUS_KILOMETERS

	@property
	def area(self):
		return self.height * self.width

	def population_density(self):
		return self.population / self.area

	def average_agreeableness(self):
		if not self.inhabitants:
			return 0
		# agreeableness = []
		#for inhabitant in self.inhabitants:
	#agreeableness.append(inhabitant.agreeableness)
		return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population

	@classmethod
    def _initialize_zones(cls):
        for latitude in range (cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner, top_right_corner)
                cls.ZONES.append(zone)
        print(len(cls.ZONES))
     Zone.initialize_zones()

		
def main():
		for agent_attributes in json.load(open("agent-100k.json")):
			latitude = agent_attributes.pop('latitude')
			longitude = agent_attributes.pop('longitude')
			position = Possition(longitude, latitude)
			agent = Agent(position, **agent_attributes)
			zone = Zone.find_zone_that_contains(position)
			zone.add_inhabitants(agent)
			print(zone.average_agreeableness())
main()


