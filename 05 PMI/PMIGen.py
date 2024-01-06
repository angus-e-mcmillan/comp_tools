import glob
import csv
import os
from rdkit.Chem import SDMolSupplier
from rdkit.Chem.rdMolDescriptors import CalcPMI1, CalcPMI2, CalcPMI3, CalcPBF

PMI1 = CalcPMI1
PMI2 = CalcPMI2
PMI3 = CalcPMI3
PBF = CalcPBF

data = "/Users/wilsonwu/Library/Mobile Documents/com~apple~CloudDocs/Work/Documents/i-SNAP project/Final library/Final sdf files"
print(os.getcwd())
print(os.listdir())
globtest = glob.glob("*.sdf")
print(globtest)

for sdf in glob.glob('*.sdf'):
    suppl = SDMolSupplier(sdf)
    filename = sdf.strip('.sdf')
    with open(filename + 'pmi.csv', 'w') as csvfile:
        headers = ['PMI1', 'PMI2', 'PMI3', 'PBF']
        csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
        csvwriter.writeheader()
        for mol in suppl:
            csvwriter.writerow({'PMI1': PMI1(mol), 'PMI2': PMI2(mol), 'PMI3': PMI3(mol), 'PBF': PBF(mol)})
print("Woo!")
