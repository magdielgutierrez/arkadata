import json
class get_available_units():
    def __init__(self,vehicle_id) -> None:
        
        
        self.vehicle_id=vehicle_id
                
    def to_JSON(self):
          return {   
                'vehicle_id': self.vehicle_id               
                }  
    