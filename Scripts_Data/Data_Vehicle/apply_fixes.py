import re
import sys

filepath = r'c:\Users\Jakub\Desktop\studia sem 5\syf\studia sem 5 (1)\studia sem4\model do matlaba\Scripts_Data\Data_Vehicle\Vehicle_data_dwishbone.m'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Body Geometry
content = content.replace(
    "Vehicle.Chassis.Body.BodyGeometry.class.Value = 'CAD_FSAE_Achilles';",
    "Vehicle.Chassis.Body.BodyGeometry.class.Value = 'Parameterized';"
)

# 2. Powertrain classes
content = content.replace(
    "Vehicle.Powertrain.Power.class.Value = 'Electric_L1_R1_L2_R2';",
    "Vehicle.Powertrain.Power.class.Value = 'Electric_L2_R2';"
)
content = content.replace(
    "Vehicle.Powertrain.Driveline.class.Value = 'L1_R1_L2_R2';",
    "Vehicle.Powertrain.Driveline.class.Value = 'L2_R2';"
)

# 3. Dampers
content = content.replace(
    "Vehicle.Chassis.Damper.Axle1.Damping.d.Value = 250000;",
    "Vehicle.Chassis.Damper.Axle1.Damping.d.Value = 2500;"
)
content = content.replace(
    "Vehicle.Chassis.Damper.Axle2.Damping.d.Value = 250000;",
    "Vehicle.Chassis.Damper.Axle2.Damping.d.Value = 2000;"
)

# 4. Brake Axle 1
content = content.replace(
    "Vehicle.Brakes.Axle1.DiscAndPad.lMeanRadius.Value = 0.15;",
    "Vehicle.Brakes.Axle1.DiscAndPad.lMeanRadius.Value = 0.0825;"
)
content = content.replace(
    "Vehicle.Brakes.Axle1.DiscAndPad.rMuStatic.Value = 0.7;",
    "Vehicle.Brakes.Axle1.DiscAndPad.rMuStatic.Value = 0.4;"
)
content = content.replace(
    "Vehicle.Brakes.Axle1.DiscAndPad.rMuKinetic.Value = 0.5;",
    "Vehicle.Brakes.Axle1.DiscAndPad.rMuKinetic.Value = 0.35;"
)
content = content.replace(
    "Vehicle.Brakes.Axle1.Caliper.lCylinderDiameter.Value = 0.0125;",
    "Vehicle.Brakes.Axle1.Caliper.lCylinderDiameter.Value = 0.021;"
)

# 5. Brake Axle 2
content = content.replace(
    "Vehicle.Brakes.Axle2.DiscAndPad.lMeanRadius.Value = 0.1;",
    "Vehicle.Brakes.Axle2.DiscAndPad.lMeanRadius.Value = 0.0825;"
)
content = content.replace(
    "Vehicle.Brakes.Axle2.DiscAndPad.rMuStatic.Value = 0.7;",
    "Vehicle.Brakes.Axle2.DiscAndPad.rMuStatic.Value = 0.4;"
)
content = content.replace(
    "Vehicle.Brakes.Axle2.DiscAndPad.rMuKinetic.Value = 0.5;",
    "Vehicle.Brakes.Axle2.DiscAndPad.rMuKinetic.Value = 0.35;"
)
content = content.replace(
    "Vehicle.Brakes.Axle2.Caliper.lCylinderDiameter.Value = 0.0125;",
    "Vehicle.Brakes.Axle2.Caliper.lCylinderDiameter.Value = 0.021;"
)

# 6. Motor L2 & R2
old_motor_w = """[0 1666.6667 3333.3333 4774.6371 5000 6666.6667 8333.3333 10000 11666.6667 ...
   13333.3333 15000 16666.6667 18333.3333 20000]"""
new_motor_w = """[0 1666.7 3333.3 5000 6666.7 8333.3 10000 11666.7 13333.3 ...
   15000 16666.7 18333.3 19166.7 20000]"""

old_motor_trq = """[200 200 200 200 190.9859 143.2394 114.5916 95.493 81.8511 71.6197 63.662 ...
   57.2958 52.0871 47.7465]"""
new_motor_trq = """[29.1 29.1 29.1 29.1 29.1 29.1 29.1 29.1 26.5 21.0 15.8 ...
   12.0 10.9 10.0]"""

old_loss_trq = "[0 20 40 60 80 100 120 140 160 180 200]"
new_loss_trq = "[0 2.91 5.82 8.73 11.64 14.55 17.46 20.37 23.28 26.19 29.1]"

content = content.replace(old_motor_w, new_motor_w)
content = content.replace(old_motor_trq, new_motor_trq)
content = content.replace(old_loss_trq, new_loss_trq)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied structural fixes.')
