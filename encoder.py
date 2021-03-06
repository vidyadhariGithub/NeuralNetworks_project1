# encoder.py
# COMP9444, CSE, UNSW

import torch
#16x8
star16 = torch.Tensor(
    [[1,1,0,0,0,0,0,0],
     [0,1,1,0,0,0,0,0],
     [0,0,1,1,0,0,0,0],
     [0,0,0,1,1,0,0,0],
     [0,0,0,0,1,1,0,0],
     [0,0,0,0,0,1,1,0],
     [0,0,0,0,0,0,1,1],
     [1,0,0,0,0,0,0,1],
     [1,1,0,0,0,0,0,1],
     [1,1,1,0,0,0,0,0],
     [0,1,1,1,0,0,0,0],
     [0,0,1,1,1,0,0,0],
     [0,0,0,1,1,1,0,0],
     [0,0,0,0,1,1,1,0],
     [0,0,0,0,0,1,1,1],
     [1,0,0,0,0,0,1,1]])

# REPLACE heart18 WITH AN 18-by-14 TENSOR
# TO REPRODUCE IMAGE SHOWN IN SPEC
heart18 = torch.Tensor(
    [[0,0,0,0,0,0,0,0,1,1,1,1,1,1],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,1,1,1,1,1,1,1,0,0,0,0,0,0],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [0,0,1,1,1,1,1,1,0,0,0,0,1,1],
     [0,1,1,1,1,1,1,1,0,0,0,1,1,1],
     [0,1,1,1,1,1,1,1,0,0,1,1,1,1],
     [0,0,1,1,1,1,1,1,0,1,1,1,1,1],
     [0,0,0,1,1,1,1,1,0,1,1,1,1,1],
     [0,0,0,0,1,1,1,1,0,0,1,1,1,1],
     [0,0,0,0,0,1,1,1,0,1,1,1,1,1],
     [0,0,0,0,0,0,1,1,0,1,1,1,1,1],
     [0,0,0,0,0,0,0,1,0,0,1,1,1,1],
     [0,0,0,0,0,0,0,1,0,0,0,1,1,1],
     [0,0,0,0,0,0,1,1,0,0,0,0,1,1],
     [0,0,0,0,0,1,1,1,0,0,0,0,0,1],
     [0,0,0,0,1,1,1,1,0,0,0,0,0,0],
     [0,0,0,1,1,1,1,1,0,0,0,0,0,1]])

# REPLACE target1 WITH DATA TO PRODUCE
# A NEW IMAGE OF a '+' sign, 13x8 tensor
target1 = torch.Tensor(
     [[1,1,1,1,0,0,1,1],
      [0,1,1,1,0,0,1,1],
      [0,0,1,1,0,0,1,1],
      [0,0,0,1,0,0,1,1],
      [0,0,0,0,0,0,1,1],
      [0,0,1,1,1,1,1,1],
      [0,0,1,1,0,1,1,1],
      [0,0,1,1,0,0,0,1],
      [0,0,1,1,0,0,0,0],
      [1,1,1,1,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,1,1,1,1],
      [1,1,1,1,1,1,1,1]])

# REPLACE target2 WITH DATA TO PRODUCE
# A NEW IMAGE OF a smiley, 14x14 tensor
target2 = torch.Tensor(
    [[1,1,1,1,1,1,1,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [0,0,0,1,1,1,1,1,0,1,1,1,1,1],
     [0,0,0,0,0,1,1,1,0,1,1,1,1,1],
     [0,0,0,0,1,1,1,1,0,0,1,1,1,1],
     [0,1,1,1,1,1,1,1,0,0,1,1,1,1],
     [0,0,1,1,1,1,1,1,0,0,0,1,1,1],
     [0,0,0,1,1,1,1,1,0,0,0,0,1,1],
     [0,0,0,0,1,1,1,1,0,0,0,0,1,1],
     [0,0,0,0,0,1,1,1,0,0,0,0,1,1],
     [0,0,0,0,0,0,1,1,0,0,0,1,1,1],
     [0,0,0,0,0,0,0,1,0,0,1,1,1,1]])
