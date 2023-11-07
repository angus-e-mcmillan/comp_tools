![example](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/8e2ab7f6-778e-47d2-8976-6866fd4997af)

First download blender from:
https://www.blender.org/download/

Next install Molecular Nodes add on
https://bradyajohnston.github.io/MolecularNodes/installation.html

In the window on the right you will find the "scene" settings, look for render properties. 
Change the Render engine: "cycles"
Change Device: "GPU Compute"

![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/71f34c13-e202-44ff-8383-de495e8de0fa)

Now lets import a protein to play with. In the scence menu, find scene proerties, here you will see the Molecular Nodes tab (if you installed it). You can use the PDB ID to download a protein directly.

Common short cuts for blender opoerations can be found here (https://docs.blender.org/manual/en/latest/interface/keymap/introduction.html)

![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/66454616-ecac-49a3-aa0d-b622b8ff6fe0)

Press the "z" key and select "rendered" (or hot key 8). Now you should see your protein as an atom point cloud.

![image](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/8bbbfc54-361f-4dcc-9738-ff40c36a56db)

Select "Geometry Nodes" at the top of the screne and select your protein to see the Nodes applied to that object.
![Screenshot 2023-10-30 at 09 11 54](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/f5ed628f-b7bd-445d-a06c-e5293d2f778a)


Press Shift + A to add more nodes. Use the search feature to find Join Geometry. In the same dropdown we find the Molecular nodes, nodes. We can try out some of the styles to change the look of your protein. Try connecting the atoms from 2 Named Attributes nodes into "stick ball and stick" "style_cartoon" and "style surface" nodes. Then use the Join Geometry node to combine them. Play with the settings and find something that you like.

![Screenshot 2023-10-30 at 09 11 42](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/a844a9c1-e7da-45f4-8402-886773207e57)

Once you have something you like, move the camera by selecting it and pressing "g" followed by x, y or z  to translate it or "r" followed x, y, z to rotate it until you have your protein framed.

![Screenshot 2023-10-30 at 09 16 41](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/c68a7b92-61c1-409c-a716-d1265e550610)

Now you can render an image by pressing F12 or selecting render image from the render dropdown.

![Screenshot 2023-10-30 at 09 16 21](https://github.com/angus-e-mcmillan/comp-tools/assets/57298625/75c6e911-203f-4dd1-8207-cad0117e05a8)

You can improve the scene further by experimenting with lights, or importing different assets. 
