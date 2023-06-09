class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
#print(issubclass(TrackedVehicle,(Vehicle,LandVehicle)))
v=Vehicle()
lv=LandVehicle()
tv=TrackedVehicle()
#print(issubclass(TrackedVehicle,Vehicle))


for cls1 in [v,lv,tv]:
      for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
          print(isinstance(cls1,cls2), end="\t")
      print()


# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#      for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#          print(issubclass(cls1, cls2), end="\t")
#      print()