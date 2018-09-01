from vpython import *
from random import random
#GlowScript 2.7 VPython

# Bruce Sherwood

N = 3 # N by N by N array of atoms
# Surrounding the N**3 atoms is another layer of invisible fixed-position atoms
# that provide stability to the lattice.
k = 1
m = 1
spacing = 1.05
atom_radius = 0.3*spacing
L0 = spacing-1.8*atom_radius
V0 = pi*(0.5*atom_radius)**2*L0 # initial volume of spring
scene.center = 0.5*(N-1)*vector(1,1,1)
dt = 0.04*(2*pi*sqrt(m/k))
axes = [vector(1,0,0), vector(0,1,0), vector(0,0,1)]

scene.caption= """A model of a solid represented as atoms connected by interatomic bonds.

Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

class crystal:
        
    def __init__(self,  N, atom_radius, spacing, momentumRange ):
        self.atoms = []
        self.springs = []
        
        # Create (N+2)^3 atoms in a grid; the outermost atoms are fixed and invisible
        for z in range(-1,N+1,1):
            for y in range(-1,N+1,1):
                for x in range(-1,N+1,1):
                    atom = box()
                    atom.pos = vector(x*1,y*1,z*1)*spacing
                    atom.radius = atom_radius
                    atom.color = vector(random(),random(),random())
                    if 0 <= x < N and 0 <= y < N and 0 <= z < N:
                        p = vec.random()
                        atom.momentum = momentumRange*p
                    else:
                        atom.visible = False
                        atom.momentum = vec(0,0,0)
                    atom.index = len(self.atoms)
                    self.atoms.append( atom )

    
    # Create a grid of springs linking each atom to the adjacent atoms
    # in each dimension, or to invisible motionless atoms


c = crystal(N, atom_radius, spacing, 0.1*spacing*sqrt(k/m))

