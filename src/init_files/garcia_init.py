# -*- coding: utf-8 -*-

import numpy as np
from src.functions.material import Material
from src.functions.mesh import Mesh

class GarciaInit:
    def __init__(self, N=2**12, Nx=20, generator="sobol"):
        self.N = N
        self.Nx = Nx
        self.generator = generator
        self.totalDim = 3
        self.RB = 5
        self.LB = 0
        self.G = 1
        self.c = 1.0
        self.right = False
        self.left = True
        self.moment_match = False
        self.phi_left = 1.0
        self.source = np.zeros((self.Nx,self.G))
        self.material_code = "garcia_data"
        self.geometry = "slab"
        self.true_flux = np.array((False)) # no analytic solution for scalar flux
        self.avg_scalar_flux = True
        self.edge_scalar_flux = False
        self.avg_angular_flux = False
        self.avg_current = False
        self.edge_current = False
        self.shannon_entropy = False
        self.save_data = True
        self.mesh = Mesh(self.LB, self.RB, self.Nx)
        self.material = Material(self.material_code, self.geometry, self.mesh)
        
        