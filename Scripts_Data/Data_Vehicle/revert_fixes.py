import sys

filepath = r'c:\Users\Jakub\Desktop\studia sem 5\syf\studia sem 5 (1)\studia sem4\model do matlaba\Scripts_Data\Data_Vehicle\Vehicle_data_dwishbone.m'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Revert architecture choices
content = content.replace(
    "Vehicle.Chassis.Body.BodyGeometry.class.Value = 'Parameterized';",
    "Vehicle.Chassis.Body.BodyGeometry.class.Value = 'CAD_FSAE_Achilles';"
)
content = content.replace(
    "Vehicle.Powertrain.Power.class.Value = 'Electric_L2_R2';",
    "Vehicle.Powertrain.Power.class.Value = 'Electric_L1_R1_L2_R2';"
)
content = content.replace(
    "Vehicle.Powertrain.Driveline.class.Value = 'L2_R2';",
    "Vehicle.Powertrain.Driveline.class.Value = 'L1_R1_L2_R2';"
)

# Zero out L1 and R1 motors to simulate RWD in a 4WD architecture
l1_trq = """Vehicle.Powertrain.Power.MotorL1.TorqueSpd.trq.Value = ...
  [300 300 300 300 286.4789 214.8592 171.8873 143.2394 122.7767 107.4296 ...
   95.493 85.9437 78.1306 71.6197];"""
l1_trq_zero = """Vehicle.Powertrain.Power.MotorL1.TorqueSpd.trq.Value = ...
  [0 0 0 0 0 0 0 0 0 0 0 0 0 0];"""

r1_trq = """Vehicle.Powertrain.Power.MotorR1.TorqueSpd.trq.Value = ...
  [300 300 300 300 286.4789 214.8592 171.8873 143.2394 122.7767 107.4296 ...
   95.493 85.9437 78.1306 71.6197];"""
r1_trq_zero = """Vehicle.Powertrain.Power.MotorR1.TorqueSpd.trq.Value = ...
  [0 0 0 0 0 0 0 0 0 0 0 0 0 0];"""

content = content.replace(l1_trq, l1_trq_zero)
content = content.replace(r1_trq, r1_trq_zero)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied revert fixes.')
