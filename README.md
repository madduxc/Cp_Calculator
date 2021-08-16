[readme.txt](https://github.com/madduxc/Cp_Calculator/files/6995881/readme.txt)
# Cp_Calculator

Rocketry Center of Pressure project

Overall Objectives:
1. Collaborate over Git and Discord on a working, useful software project.
2. Practice using GUIs to visualize results.
3. Implement package for a model rocketry program.

Take as inputs the geometry measurements of a model rocket in sections and deliver as outputs the rocket 
center of pressure.  Bonus points for sketching the gemetry and overalying the Cp.

Goals:
Cp_Calculator should be a class, with named rockets as class objects.
Break down tasks into small, reusable functions whenever possible
Inputs should be checked for validity (i.e., no negative distances, no overlapping points, etc.)
Individual sections to be calculated separately by class or function:
    Nose cone
    Airframe
    Shoulder
    Fins
    Boattail
Increase complexity of individual function without having to rewrite the parent class.
Summation performed by Cp_Calculator or handed to a function
Results should be written to a file - JSON or csv.
Unit testing performed for each function and class written
