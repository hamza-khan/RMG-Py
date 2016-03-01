database(
    thermoLibraries = ['primaryThermoLibrary', 'GRI-Mech3.0']   
)

species(
    label='s1_3_6_ane',
    structure=SMILES("C1CCC2(CC1)CC2"),
)
species(
    label='s1_3_6_ene_1',
    structure=SMILES("C1=CC2(CCC1)CC2"),
)
species(
    label='s1_3_6_ene_2',
    structure=SMILES("C1=CCC2(CC1)CC2"),
)
species(
    label='s1_3_6_diene_1_4',
    structure=SMILES("C1=CC2(C=CC1)CC2"),
)
species(
    label='s1_3_6_diene_1_3',
    structure=SMILES("C1C=CC2(CC=1)CC2"),
)

quantumMechanics(
    software='mopac',
    method='pm7',
    onlyCyclics = True,
    maxRadicalNumber = 0,
)
