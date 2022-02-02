A curve of pursuit is a curve constructed by analogy to having a point or points representing pursuers and pursuees; the curve of pursuit is the curve traced by the pursuers.
The pursuit curve can be modelled analytically. A good derivation of the model of the pursuit curve can be found here:https://mathworld.wolfram.com/PursuitCurve.html
The pursuit curve can be hard to model analytically if the path/direction taken by the runner varies with time.
The simulation simulates the pursuit curve for a simple case but can easily be modified to simulate more complicated cases.
###  Variable Definitions ###
#initial_x --> initial position of the merchant ship (the runner)
#initial_y --> initial position of the pirate ship (the chaser)
#vm --> direction vector of the runner
#run --> speed of the runner
#chase --> speed of the chaser
We can model the path of the runner by modifying the vm and run variable.
