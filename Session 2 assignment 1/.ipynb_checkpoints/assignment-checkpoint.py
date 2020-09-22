import pytest
_ = 123456789  # just  wrong number, please ignore

# Black box model
# 1. Calculate the specific yield coefficients (C-mol) for all products.

# Initial- and end values  
glucose_init = 20 #g/L
biomass_init = 0.2 #g DW yeast/ L
ethanol_end = 10 #g/L
biomass_end = 2.74 #g DW yeast/L
glycerol_end = 1.54 #g/L

# Molecular weights 
glucose_mw = 180.156 #g/mol
ethanol_mw = 46.07 #g/mol
glycerol_mw = 92.09382 #g/mol 

# Mw in C-mol
glucose_mw_Cmol = glucose_mw/6 # g/Cmol
ethanol_mw_Cmol = ethanol_mw/2 # g/Cmol
glycerol_mw_Cmol = glycerol_mw/3 # g/Cmol
biomass_mw_Cmol = 12.0107 + 1.8*1.00784 + 0.5*15.999 + 0.2*14.0067  #g/Cmol, from CH_(1.8)O_(0.5)N_(0.2) 

# C-mol concentrations of glucose and end products:
glucose_init_Cmol = glucose_init / glucose_mw_Cmol # Cmol/L
ethanol_end_Cmol = ethanol_end / ethanol_mw_Cmol # Cmol/L
glycerol_end_Cmol = glycerol_end / glycerol_mw_Cmol # Cmol/L
biomass_end_Cmol = biomass_end / biomass_mw_Cmol # Cmol/L

# Assign your solutions to the following variables (replace _ with your solutions)
Y_sx = biomass_end_Cmol/glucose_init_Cmol
Y_se = ethanol_end_Cmol/glucose_init_Cmol
Y_sg = glycerol_end_Cmol/glucose_init_Cmol


def test_Y_sx():
    assert Y_sx == pytest.approx(0.166, .01)

def test_Y_se():
    assert Y_se == pytest.approx(0.652, .01)

def test_Y_sg():
    assert Y_sg == pytest.approx(0.075, .01)
  

# 2. Calculate the carbon balance.

# 1 = Y_sx + Y_se + Y_sg
# Carbon balance: 1 - Y_sx - Y_se - Y_sg

# Assign your solution to the following variable (replace _ with your solution)
carbon_balance = 1 - Y_sx - Y_se - Y_sg # c-mol product / c-mol-Glc

def test_carbon_balance():
    assert carbon_balance == pytest.approx(0.106, 0.01)
    

# 3. Assuming that CO2 is the only missing product, calculate how much CO2 was produced in the fermentation.

# Yield coefficient for CO2:
Y_sc = carbon_balance # cmol CO2/ Cmol glucose

# Produced CO2 in Cmol/L:
co2_produced_Cmol = Y_sc * glucose_init_Cmol # Cmol/L

# Molecular weight of CO2:
co2_mw_Cmol = 44.01 #g/Cmol

# Produced Co2 in g/L
# Assign your solution to the following variable (replace _ with your solution)
co2_produced = co2_produced_Cmol * co2_mw_Cmol # g/L

def test_co2_produced():
    assert co2_produced == pytest.approx(3.129, 0.01)
    
