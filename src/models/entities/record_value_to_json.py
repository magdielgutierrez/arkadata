import json
from utils.dateformat_value import DateFormat
class get_all_records():
    def __init__(self,id,date_updated=None,vehicle_id=None,vehicle_label=None,
                            vehicle_status=None,geographic_point=None,position_odometer=None,position_speed=None) -> None:
            self.id=id
            self.date_updated=date_updated
            self.vehicle_id=vehicle_id
            self.vehiclelabel=vehicle_label
            self.vehicle_status=vehicle_status
            self.geographic_point=geographic_point
            self.position_odometer=position_odometer
            self.position_speed=position_speed
                    
    def to_JSON(self):
           
            return {   
                    'id': self.id,
                    'date_updated': DateFormat.convert_date(self.date_updated),
                    'vehicle_id':self.vehicle_id,
                    'vehicle_label': self.vehiclelabel,
                    'vehicle_status': self.vehicle_status,
                    'geographic_point':self.geographic_point,
                    'position_odometer':self.position_odometer,
                    'position_speed': self.position_speed                       
                    }   
            
          

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

class get_municipal_available():
    def __init__(self,mayors) -> None:
        
        self.mayors=mayors
                
    def to_JSON(self):
          return {   
                'mayors_name':  self.mayors              
                }  
   

class get_municipal_units():
    def __init__(self,units) -> None:
        
        self.units=units
                
    def to_JSON(self):
          return {   
                'units_id':  self.units              
                }  
   