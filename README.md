# comp-tools
Useful Comp Tools Session

If you want to skip building your own workflow (shown below) just import "Reactions_with_RDKit_Hub_after4.3" and update the data paths.

Today we are going to look into using KNIME to enumerate reaction products and then calculate some properties for those products. First we need to install KNIME, I'm using version 5.1.1. You can download it here...

https://www.knime.com/downloads

We will use the copper catalysed azide and alkyne click reaction. The first thing we need to do is import our starting materials. For This we provided a csv file which contains the starting materials as smiles. See:

alkynes.csv
azides.csv

To import the csv file we can use the CSV Reader node which you will find in Repository on the left hand side.
![Screenshot 2023-10-16 at 17 31 09](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/d459a0fd-508c-43b3-b635-ae4e9ad016df)


Drag it into your workspace and configure the directory to the CSV file you with to open
![Screenshot 2023-10-16 at 17 34 52](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/e2c9cb7d-fa0b-4f42-a0e4-29a4f060e182)


Next we can convert the String column which contains smiles into a "smiles" coolumn using the Molecule Type Cast Node. 

We will use the RDKit extension which you may need to install.

RDKit from Molecule Node can change our smiles representation into an RDKit molecule and the RDKIt canon SMILES will write canonical smiles for that RDKit molecule. This seems a bit stepy but it ensures we don't have any issues with our molecules later.

You can repeat this for your next building block (the alkynes) and then we are ready to enumerate.
![Screenshot 2023-10-16 at 17 40 35](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/bd5a9061-649f-4389-bffd-1a013a095773)


To ennumerate the reaction products we use Molecular Sketcher Node to draw the reaction. This outputs a smarts string which we plug into the RDKit two component reaction, along with our two sets of starting materials. 
![Screenshot 2023-10-16 at 17 41 51](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/20f08a5f-f478-4309-a4d5-1b056a648507)
![Screenshot 2023-10-16 at 17 42 10](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/150e9d64-183d-408c-ac02-d8c9a492670b)


Now we can enumerate our reaction products. By plugging the output into the Molecular Properties node we can also calculate some properties, like MW and sum formula.
![Screenshot 2023-10-16 at 17 44 54](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/f90e3acb-88b8-4ac6-8320-fe1482b29d22)



Finally to save our output we can use CSV writer.
![Screenshot 2023-10-16 at 17 45 10](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/7eba67fa-e690-4a41-9b68-797b1f1dd38f)


Now try making a three component library by including the materials from the amines.csv to perform a reductive amination.
