class Record_List():
    def __init__(self,id,
                date_updated=None,
                vehicle_id=None,
                vehicle_label=None,
                vehicle_status=None,
                geographic_point=None,
                position_odometer=None,
                position_speed=None) -> None:
        
        self.id=id
        self.date_updated=date_updated,
        self.vehicle_id=vehicle_id,
        self.vehicle_label=vehicle_label,
        self.vehicle_status=vehicle_status,
        self.geographic_point=geographic_point,
        self.position_odometer=position_odometer,
        self.position_speed=position_speed
                
                
    def to_JSON(self):
        return {
                'id':self.id,
                'date_updated': self.date_updated,
                'vehicle_id':self.vehicle_id,
                'vehicle_label': self.vehicle_label,
                'vehicle_status': self.vehicle_status,
                'geographic_point':self.geographic_point,
                'position_odometer':self.position_odometer,
                'position_speed':self.position_speed
        
        }
    