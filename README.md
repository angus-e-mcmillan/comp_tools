# comp-tools
Useful Comp Tools Session

If you want to skip building your own workflow (shown below) just import "Reactions_with_RDKit_Hub_after4.3" and update the data paths.

Today we are going to look into using KNIME to enumerate reaction products and then calculate some properties for those products. First we need to install KNIME, I'm using version 5.1.1. You can download it here...

https://www.knime.com/downloads

We will use the copper catalysed azide and alkyne click reaction. The first thing we need to do is import our starting materials. For This we provided a csv file which contains the starting materials as smiles. See:

alkynes.csv
azides.csv

To import the csv file we can use the CSV Reader node which you will find in Repository on the left hand side.
![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/591ab4cc-393f-4afa-97c4-1dc8d204c033)

Drag it into your workspace and configure the directory to the CSV file you with to open
![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/e315f3bd-2801-47fc-beb1-c4f1f1484754)

Next we can convert the String column which contains smiles into a "smiles" coolumn using the Molecule Type Cast Node. 

We will use the RDKit extension which you may need to install.

RDKit from Molecule Node can change our smiles representation into an RDKit molecule and the RDKIt canon SMILES will write canonical smiles for that RDKit molecule. This seems a bit stepy but it ensures we don't have any issues with our molecules later.

You can repeat this for your next building block (the alkynes) and then we are ready to enumerate.
![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/ce26118a-f1d8-4016-b411-7be89425dc61)

To ennumerate the reaction products we use Molecular Sketcher Node to draw the reaction. This outputs a smarts string which we plug into the RDKit two component reaction, along with our two sets of starting materials. 
![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/435f1a9f-1a59-4522-8984-35acdf1771d0)
![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/d7d6e981-4327-44df-bb00-7c0243e204c4)

Now we can enumerate our reaction products. By plugging the output into the Molecular Properties node we can also calculate some properties, like MW and sum formula.
![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/9553db90-41ff-4f8b-86a0-c3984aca08cd)


Finally to save our output we can use CSV writer.
![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/782b6352-4d66-4e0e-ae6c-baad6ce01b9f)

Now try making a three component library by including the materials from the amines.csv to perform a reductive amination.
