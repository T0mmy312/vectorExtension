# vector extension

## **vector2 class:**

The vector2 class takes in two arguments x and y.

You can add and subtract two vectors.

When you multiply two vectors it returns the scalar product of the two.

$\vec{a} * \vec{b} = a_{x} * b_{x} + a_{y} * b_{y}$

You can also call a funktion to get the lenght.
~~~
a = vector2(1, 2)
a.amout()
~~~
Or you can get the lenght by accessing the variable amout, a, betrag or b. (betrag and b are german)
~~~
a.amount
a.a
a.betrag
a.b
~~~
$a.amount = a.a = a.betrag = a.b = |\vec{a}| = \sqrt{a_{x}^2+a_{y}^2}$

You can also get the unit vector by calling the funktion or accessing the variable unitVec, u, einheitenVec or e. (again einheitenVec and e are german)

~~~
a.unitVec()
a.unitVec
a.u
a.einheitenVec
a.e
~~~
$a.u = \vec{a} * \frac{1}{|\vec{a}|}$

You can get the angle between two vectors by useing the angl funktion or useing the angle infix operator |v| both return the angle in degrees.

~~~
b = vector2(3, 4)

angl(a, b)
a |v| b
~~~
$\cos\gamma = \frac{\vec{a}*\vec{b}}{|\vec{a}|*|\vec{b}|}$

If you want to check if two vectors are paralell you can use the vecPar funktion (retuns true or false)

~~~
vecPar(a, b)
~~~

You can turn it into a tuple by calling the tuple funktion or accessing the tuple or t variable.
~~~
a.tuple()
a.tuple
a.t
~~~
All of the operators also work with tuples.

## **Vector3 class:**

The vector3 class takes in three arguments x, y and z.

You can add and subract two vectors.

When you multiply two vectors it returns the scalar product of the two.

$\vec{a} * \vec{b} = a_{x} * b_{x} + a_{y} * b_{y} + a_{z} * b_{z}$

You can get the lenght and unit vector just like in the vector two class.

The angl funktion and operator also work the same.

Tuples also work the same.

If you want the cross product of two vectors you can call the crossProd funktion or use the crossProd Infix operator |x|.
~~~
a = vector3(1, 2, 3)
b = vector3(4, 5, 6)

crossProd(a, b)
a |x| b
~~~
$\vec{a} \times \vec{b} = \begin{pmatrix} a_x \\\ a_y \\\ a_z \end{pmatrix} \times \begin{pmatrix}b_x \\\ b_y \\\ b_z\end{pmatrix}=\begin{pmatrix} a_yb_z - b_ya_z \\\ b_xa_z - a_xb_z \\\ a_xb_y - b_xa_y \end{pmatrix}$

## gP class

gP stand for the Parameter representation of a continuous line. The formular of this representation looks like this:

$g: \vec{X} = \vec{OP} + t *\vec{a}$

t is the paramiter and OP is a point on the line and a is the direction of the line.