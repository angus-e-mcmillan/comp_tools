import glob
import csv
import os
from rdkit.Chem import SDMolSupplier
from rdkit.Chem.Lipinski import FractionCSP3, NumAromaticRings, NumHAcceptors, NumHDonors, NumRotatableBonds
from rdkit.Chem.Descriptors import MolWt
from rdkit.Chem.Crippen import MolLogP
from rdkit.Chem.rdMolDescriptors import CalcPBF
from rdkit.Chem.GraphDescriptors import BertzCT

fsp3 = FractionCSP3
nar = NumAromaticRings
NumA = NumHAcceptors
NumD = NumHDonors
NumR = NumRotatableBonds
Wt = MolWt
LogP = MolLogP
PBF = CalcPBF
BC = BertzCT

data = "/Users/wilsonwu/Dropbox/Libraries/Combined/Combined R enantiomer"
print(os.getcwd())
print(os.listdir())
globtest = glob.glob("*.sdf")
print(globtest)

for sdf in glob.glob('*.sdf'):
    suppl = SDMolSupplier(sdf)
    filename = sdf.strip('.sdf')
    with open(filename + '-fsp3-nar.csv', 'w') as csvfile:
        headers = ['Fsp3', '#Aromatic_rings', '#HAcceptors', '#HDonors', '#Rotatable_Bonds', 'MolWt', 'LogP', 'PBF', 'BC']
        csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
        csvwriter.writeheader()
        for mol in suppl:
            csvwriter.writerow({'Fsp3': fsp3(mol), '#Aromatic_rings': nar(mol), '#HAcceptors': NumA(mol), '#HDonors': NumD(mol), '#Rotatable_Bonds': NumR(mol), 'MolWt': Wt(mol), 'LogP': LogP(mol), 'PBF': PBF(mol), 'BC': BertzCT(mol, cutoff=100, dMat=None, forceDMat=1)})
print("sucess")
