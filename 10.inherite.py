class Vehicle:
  def __init__(self,seating_capacity):
    self.seating_capacity=seating_capacity
    

  def fare(self):
    fare_Amount = self.seating_capacity*100
    return(fare_Amount)


class Bus(Vehicle):
  
  def __init__(self):
    Vehicle.__init__(self,50)
    self.seating_capacity = 50
    

  def fare(self):    
    fare_Amount = (self.seating_capacity*100)   
    final_Amount = int(fare_Amount + fare_Amount * 0.1)
    return(final_Amount)

capacity = 50 
bus = Bus()
Total_fare = bus.fare()
print(f"The bus seating capacity is {capacity}. so the final fare amount should be {Total_fare}.")
