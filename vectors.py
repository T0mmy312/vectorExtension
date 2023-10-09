from math import *
from typing import Any

class Infix:

  def __init__(self, function):
    self.function = function

  def __ror__(self, other):
    return Infix(lambda x, self=self, other=other: self.function(other, x))

  def __or__(self, other):
    return self.function(other)

  def __rlshift__(self, other):
    return Infix(lambda x, self=self, other=other: self.function(other, x))

  def __rshift__(self, other):
    return self.function(other)

  def __call__(self, value1, value2):
    return self.function(value1, value2)

def crossProd(a, b): #returns the cross product of two vector3's
  if isinstance(a, vector3) and isinstance(b, vector3):
    return vector3(a.y * b.z - b.y * a.z, b.x * a.z - a.x * b.z, a.x * b.y - b.x * a.y)
  else:
    ValueError(f"x only works on vector3 and vector3 and not with {type(a)} and {type(b)}!")

x = Infix(crossProd) #makes you able to call crossProd(a, b) like this: a |x| b

def angl(a, b): #returns the angle between two vectors
  if isinstance(a, vector3) and isinstance(b, vector3) or isinstance(
      a, vector2) and isinstance(b, vector2):
    return degrees(acos((a * b) / (a.a * b.a)))
  else:
    return ValueError(f"angl only works on vector3 and vector3 or vector2 and vector2 and not with {type(a)} and {type(b)}!")

v = Infix(angl) #makes you able to call angl(a, b) like this: a |v| b

def vecPar(a, b): #checks if two vectors are paralell or not
  if isinstance(a, vector2) and isinstance(b, vector2):
    return a.x/a.y == b.x/b.y
  elif isinstance(a, vector3) and isinstance(b, vector3):
    return a.x/b.x == a.y/b.y and a.y/b.y == a.z/b.z
  elif isinstance(a, gP) and isinstance(b, gP):
    if isinstance(a.a, vector2) and isinstance(b.a, vector2):
      return a.a.x/a.a.y == b.a.x/b.a.y
    if isinstance(a, vector3) and isinstance(b, vector3):
      return a.a.x/b.a.x == a.a.y/b.a.y and a.a.y/b.a.y == a.a.z/b.a.z

def intersect(g1, g2): #returns the intersection of g1 and g2
  if isinstance(g1, gP) and isinstance(g2, gP):
    if vecPar(g1.a, g2.a):
      return g1 if g2.element(g1.op) else None
    else:
      if isinstance(g1.a, vector2) and isinstance(g2.a, vector2):
        t = (g2.op.x * g2.a.y + g1.op.y * g2.a.x - g2.op.y * g2.a.x - g1.op.x * g2.a.y)/(g1.a.x * g2.a.y - g1.a.y * g2.a.y)
        #s = (g1.op.y + t * g1.a.y - g2.op.y)/g2.a.y
        return g1.calc(t)
      elif isinstance(g1.a, vector3) and isinstance(g2.a, vector3):
        t = (g2.op.x * g2.a.y + g1.op.y * g2.a.x - g2.op.y * g2.a.x - g1.op.x * g2.a.y)/(g1.a.x * g2.a.y - g1.a.y * g2.a.x)
        #s = (g1.op.y + t * g1.a.y - g2.op.y)/g2.a.y
        return g1.calc(t)

n = Infix(intersect) #makes you able to call intersect(g1, g2) like this: g1 |n| g2
p = Infix(vecPar) #makes you able to call vecPar(a, b) like this: a |p| b

def reflect(f, l): #reflects a line over a face and retruns the reflections
  if isinstance(f, plane) and isinstance(l, gP):
    pass

class vector3:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def unitVec(self):
    return self.u

  def amount(self):
    return self.a

  def tuple(self):
    return self.t

  def __add__(self, other):
    if isinstance(other, vector3):
      return vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 3:
        return vector3(self.x + other[0], self.y + other[1], self.z + other[2])
  
  def __radd__(self, other):
    if isinstance(other, vector3):
      return vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 3:
        return vector3(self.x + other[0], self.y + other[1], self.z + other[2])

  def __sub__(self, other):
    if isinstance(other, vector3):
      return vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 3:
        return vector3(self.x - other[0], self.y - other[1], self.z - other[2])

  def __mul__(self, other):
    if isinstance(other, vector3):
      return self.x * other.x + self.y * other.y + self.z * other.z
    elif isinstance(other, float) or isinstance(other, int):
      return vector3(self.x * other, self.y * other, self.z * other)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 3:
        return self.x * other[0] + self.y * other[1] + self.z * other[2]
  
  def __rmul__(self, other):
    if isinstance(other, vector3):
      return self.x * other.x + self.y * other.y + self.z * other.z
    elif isinstance(other, float) or isinstance(other, int):
      return vector3(self.x * other, self.y * other, self.z * other)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 3:
        return self.x * other[0] + self.y * other[1] + self.z * other[2]

  def __truediv__(self, other):
    if isinstance(other, float) or isinstance(other, int) and other != 0:
      return vector3(self.x / other, self.y / other, self.z / other)

  def __eq__(self, other):
    if isinstance(other, vector3):
      return (self.x == other.x) and (self.y == other.y) and (self.z== other.z)
    elif isinstance(other, tuple) or isinstance(other, list):
      return (self.x == other[0]) and (self.y == other[1]) and (self.z== other[2])
    else:
      return False

  def __gt__(self, other):
    if isinstance(other, vector3):
      return self.a > other.a
    elif isinstance(other, tuple) or isinstance(other, list):
      return self.a > sqrt(other[0]**2 + other[1]**2 + other[2]**2)

  def __lt__(self, other):
    if isinstance(other, vector3):
      return self.a < other.a
    elif isinstance(other, tuple) or isinstance(other, list):
      return self.a < sqrt(other[0]**2 + other[1]**2 + other[2]**2)

  def __ge__(self, other):
    if isinstance(other, vector3):
      return self.a >= other.a
    elif isinstance(other, tuple) or isinstance(other, list):
      return self.a >= sqrt(other[0]**2 + other[1]**2 + other[2]**2)

  def __le__(self, other):
    if isinstance(other, vector3):
      return self.a <= other.a
    elif isinstance(other, tuple) or isinstance(other, list):
      return self.a <= sqrt(other[0]**2 + other[1]**2 + other[2]**2)

  def __str__(self):
    return f"{self.x}, {self.y}, {self.z}"

  def __len__(self):
    return 3

  def __getattribute__(self, __name: str):
    var = ["x", "y", "z"]
    if __name in var:
      return super().__getattribute__(__name)
    elif __name == "amount" or __name == "a" or __name == "betrag" or __name == "b":
      return sqrt(self.x**2 + self.y**2 + self.z**2)
    elif __name == "unitVec" or __name == "u" or __name == "einheitenVec" or __name == "e":
      return self / self.a
    elif __name == "tuple" or __name == "t":
      return (self.x, self.y, self.z)
    else:
      return AttributeError(
          f"'{__name}' Attribute does not exist in class 'vector3'")

class vector2:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def unitVec(self):
    return self.u

  def amount(self):
    return self.a

  def tuple(self):
    return self.t

  def __add__(self, other):
    if isinstance(other, vector2):
      return vector2(self.x + other.x, self.y + other.y)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 2:
        return vector2(self.x + other[0], self.y + other[1])
  
  def __radd__(self, other):
    if isinstance(other, vector2):
      return vector2(self.x + other.x, self.y + other.y)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 2:
        return vector2(self.x + other[0], self.y + other[1])

  def __sub__(self, other):
    if isinstance(other, vector2):
      return vector2(self.x - other.x, self.y - other.y)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 2:
        return vector2(self.x - other[0], self.y - other[1])

  def __mul__(self, other):
    if isinstance(other, vector2):
      return self.x * other.x + self.y * other.y
    elif isinstance(other, float) or isinstance(other, int):
      return vector2(self.x * other, self.y * other)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 2:
        return self.x * other[0] + self.y * other[1]
  
  def __rmul__(self, other):
    if isinstance(other, vector2):
      return self.x * other.x + self.y * other.y
    elif isinstance(other, float) or isinstance(other, int):
      return vector2(self.x * other, self.y * other)
    elif isinstance(other, tuple) or isinstance(other, list):
      if len(other) >= 2:
        return self.x * other[0] + self.y * other[1]

  def __truediv__(self, other):
    if isinstance(other, float) or isinstance(other, int) and other != 0:
      return vector2(self.x / other, self.y / other)

  def __eq__(self, other):
    if isinstance(other, vector2):
      return (self.x == other.x) and (self.y == other.y)
    elif isinstance(other, tuple) or isinstance(other, list) and len(other) == 2:
      return (self.x == other[0]) and (self.y == other[1])
    else:
      return False

  def __gt__(self, other):
    if isinstance(other, vector2):
      return self.a > other.a
    elif isinstance(other, tuple) or isinstance(other, list) and len(other) == 2:
      return self.a > sqrt(other[0]**2 + other[1]**2)

  def __lt__(self, other):
    if isinstance(other, vector2):
      return self.a < other.a
    elif isinstance(other, tuple) or isinstance(other, list) and len(other) == 2:
      return self.a < sqrt(other[0]**2 + other[1]**2)

  def __ge__(self, other):
    if isinstance(other, vector2):
      return self.a >= other.a
    elif isinstance(other, tuple) or isinstance(other, list) and len(other) == 2:
      return self.a >= sqrt(other[0]**2 + other[1]**2)

  def __le__(self, other):
    if isinstance(other, vector2):
      return self.a <= other.a
    elif isinstance(other, tuple) or isinstance(other, list) and len(other) == 2:
      return self.a <= sqrt(other[0]**2 + other[1]**2)

  def __str__(self):
    return f"{self.x}, {self.y}"

  def __len__(self):
    return 3

  def __getattribute__(self, __name: str):
    var = ["x", "y"]
    if __name in var:
      return super().__getattribute__(__name)
    elif __name == "amount" or __name == "a" or __name == "betrag" or __name == "b":
      return sqrt(self.x**2 + self.y**2)
    elif __name == "unitVec" or __name == "u" or __name == "einheitenVec" or __name == "e":
      return self / self.a
    elif __name == "tuple" or __name == "t":
      return (self.x, self.y)
    else:
      return AttributeError(f"'{__name}' Attribute does not exist in class 'vector2'")

class plane:

  def __init__(self, p: vector3,x: vector3, y: vector3):
    self.p = p
    self.x = x
    self.y = y
  
  def n(self):
    return self.x |x| self.y
  
  def onPlane(a: vector3):
    pass
  
  def __getattribute__(self, __name: str):
    var = ["x", "y", "p"]
    if __name in var:
      return super().__getattribute__(__name)
    elif __name == "n":
      return self.n()

class g:

  def __init__(self, k, d):
    self.k = k
    self.d = d
  
  def calc(self, x):
    return self.k * x + self.d
  
  def element(self, p):
    return p.y == self.calc(p.x)
  
  def __str__(self):
    return f"y = {self.k} * x + {self.d}"
  
  def __setattr__(self, __name: str, __value: Any) -> None:
    var = ["k", "d"]
    if __name in var:
      super().__setattr__(__name, __value)
    elif __name == "x" and isinstance(__value, int) or isinstance(__value, float):
      return self.calc(__value)
    elif __name == "p" and isinstance(__value, vector2) or isinstance(__value, vector3):
      return self.element(__value)

class gP:

  def __init__(self, op: vector2 or vector3, a: vector2 or vector3):
    if isinstance(op, vector3) and isinstance(a, vector3) or isinstance(op, vector2) and isinstance(a, vector2):
      self.op = op
      self.a = a
    else:
      return ValueError(f"args can only be vector2 or vector3 not {type(op)} and {type(a)}")
    
  def calc(self, t):
    return self.op + t * self.a

  def element(self, p):
    if isinstance(self.op, vector2) and isinstance(p, vector2):
      if self.a.x != 0:
        t1 = (p.x - self.op.x)/self.a.x
      else:
        t1 = p.x == self.op.x
      if self.a.y != 0:
        t2 = (p.y - self.op.y)/self.a.y
      else:
        t2 = p.y == self.op.y
      if isinstance(t1, bool) or isinstance(t2, bool):
        return t1 * t2 != 0
      else:
        return t1 == t2
    elif isinstance(self.op, vector3) and isinstance(p, vector3):
      if self.a.x != 0:
        t1 = (p.x - self.op.x)/self.a.x
      else:
        t1 = p.x == self.op.x
      if self.a.y != 0:
        t2 = (p.y - self.op.y)/self.a.y
      else:
        t2 = p.y == self.op.y
      if self.a.z != 0:
        t3 = (p.z - self.op.z)/self.a.z
      else:
        t3 = p.z == self.op.z
      if isinstance(t1, bool) or isinstance(t2, bool) or isinstance(t3, bool):
        return t1 * t2 * t3 != 0
      else:
        return t1 == t2 and t2 == t3
  
  def __str__(self):
    return f"X = ({self.op}) + t * ({self.a})"
      
  def __setattr__(self, __name: str, __value: Any):
    var = ["op", "a"]
    if __name in var:
      super().__setattr__(__name, __value)
    elif __name == "t" and isinstance(__value, int) or isinstance(__value, float):
      return self.calc(__value)
    elif __name == "p" and isinstance(__value, vector2) or isinstance(__value, vector3):
      return self.element(__value)