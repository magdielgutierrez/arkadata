import json
class get_unit_location_by_id():
    
    def __init__(self,vehicle_id,                
                    geographic_point=None,  postal_code=None,country_code=None,
                    community_name=None,state_name=None, road=None,neighbourhood=None,highway=None,place_name=None,
                    alcaldia_name  =None) -> None:
        
        
        self.vehicle_id=vehicle_id
        self.geographic_point=geographic_point
        self.postal_code= postal_code
        self.community_name=community_name
        self.state_name=state_name
        self.country_code=country_code
        self.road=road
        self.neighbourhood = neighbourhood
        self.highway =highway
        self.place_name=place_name
        self.alcaldia_name  = alcaldia_name
        
                
    def to_JSON(self):
          return {   
                'vehicle_id': self.vehicle_id,
                'geographic_point': self.geographic_point,
                'postal_code':self.postal_code,
                'country_code': self.country_code,
                'community_name': self.community_name,
                'state_name':self.state_name,
                'road':self.road,
                'neighbourhood': self.neighbourhood ,
                'highway': self.highway  ,
                'place_name': self.place_name,
                'alcaldia_name'  : self.alcaldia_name                         
                }  
 
 
 
class get_available_units():
    def __init__(self,vehicle_id) -> None:
        
        self.vehicle_id=vehicle_id
                
    def to_JSON(self):
          return {   
                'vehicle_id': self.vehicle_id               
                }  
       