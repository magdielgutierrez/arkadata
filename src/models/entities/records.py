from utils.dateformat_value import DateFormat
import json
class Record_List():
    def __init__(self,id,date_updated=None,vehicle_id=None,vehicle_label=None,
                        vehicle_status=None,geographic_point=None,position_odometer=None,position_speed=None) -> None:
        self.id=id
        self.date_updated=date_updated,
        self.vehicle_id=vehicle_id,
        self.vehiclelabel=vehicle_label,
        self.vehicle_status=vehicle_status,
        self.geographic_point=geographic_point,
        self.position_odometer=position_odometer,
        self.position_speed=position_speed
        # print("valor de objeto en CLASE", vehicle_label)
        # print("valor de objeto para JSON", self.vehiclelabel)
       
                
    def to_JSON(self):
        print(len(self.vehicle_id))
        dict_json= {   
                'id': self.id,
                'date_updated': self.date_updated,
                'vehicle_id':56,
                'vehicle_label': self.vehiclelabel,
                'vehicle_status': self.vehicle_status,
                'geographic_point':self.geographic_point,
                'position_odometer':self.position_odometer,
                'position_speed': self.position_speed                       
                }   
          
        return dict_json
    