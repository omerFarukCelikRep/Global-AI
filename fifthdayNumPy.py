#Numpy
#Basic library used in scientific calculations
#Linear algebra, machine learning, data science
#Multi-dimensional arrays
#Fast access to multi-dimensional arrays
#The difference from the lists is having a fixed size

import numpy as np
from numpy.core.fromnumeric import size
from numpy.core.records import array
from numpy.lib.index_tricks import AxisConcatenator

a = np.array([1,2,3,4,5]);  #1st degree array, vector

print(type(a));
print(a.shape);

print(a.ndim);  #return the dimension of an array

b = np.array([[1,2,3,4],[5,6,7,8]]);  # 2nd degree array

print(b);
print(b.shape);

print(b[0,0]);

c = np.array([[1,2,3],[4,5,6],[7,8,9]]);

print(c);
print(c.shape);

print(c.ndim);


d = np.array([[[1,2,3],[4,5,6],[7,8,9]]]);

print(d);

print(d.shape);
print(d.ndim);

new_array = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]);
print(new_array);

print(new_array.shape);
print(new_array.ndim);


#Arrays with Special Values

#Zero Array

s = np.zeros((2,2));

print(s);

s2 = np.ones((2,3)).astype("int64").dtype;

print(s2);

s3 = np.full((3,3),8);

print(s3.dtype);

s4 = np.empty((4,5));   #It creates a series of randomly determined elements according to the state of the memory

print(s4);


#Diagonal Array

s5 = np.eye(4);

print(s5);

s6 = np.eye(4,4);

print(s6);

s7 = np.arange(0,10,1);

print(s7);

s8 = np.linspace(2,3,5);

print(s8);

s9 = np.random.random((5,5));

print(s9);

array_random = np.random.randint(5,10, size=10);

print(array_random.shape);


#Reshape
s10 = np.random.randint(5,10, size=(5,3));

print(s10);

print(s10.shape);

print(s10.reshape(3,5));   #The original matrix and the new one must have the same number of items


s11 = np.random.randint(5,10,size=(5,3));
print(s11);

s11 =s11.ravel();

print(s11);

print(s11.astype("int64").dtype)

s11 = s11.reshape(3,5);

print(s11.max());
print(s11.max());
print(s11[::-1]);

s12 = np.random.randint(1,100,(10,3));
print(s12);

print(type(s12));

print(s12.argmax());   #return index number
print(s12.argmax());
print(s12.mean());


#Stacking

array1  = np.array([[1,2,3],[4,5,6]]);

array2 = np.array([[6,5,4],[3,2,1]]);


print(np.vstack((array1,array2)));  #vertical stacking
print(np.hstack((array1,array2)));  #horizontal stacking

#Concatenation

myArray = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(5,2);

print(myArray);

print(np.concatenate([myArray,myArray], axis=0))  #vertical
print(np.concatenate([myArray,myArray], axis=1))  #horizontal


#Slicing

array3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]);

array4 = array3[:2, 1:3];

print(array4);

print(array3[0,1]);

array4[0,0] = 77;

print(array3[0,1]);

print(array3);

array5 = np.array([[1,2],[3,4],[5,6]]);

print(array5[[0,1,2],[0,1,0]]);
print(array5[0,0],array5[1,1],array5[2,0]);

print(np.array([array5[0,0],array5[1,1],array5[2,0]]));

array6 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]);

array7 = np.array([0,2,0,1]);

print(array6[np.arange(4), array7]);    #([0,1,2,3],[0,2,0,1])


#Aritmetic Operations

x = np.array([[1,2],[3,4]], dtype=np.float64);
y = np.array([[5,6],[7,8]], dtype=np.float64);

print(x + y);

print(np.add(x,y));

print(x-y);
print(np.subtract(x,y));

print(x * y);
print(np.dot(x,y));

print(x/y);
print(np.divide(x,y));

s = np.array([[4,9],[16,81]], dtype=np.float64);

print(np.sqrt(s));


t = np.array([[4,9],[16,81]], dtype=np.float64);

print(np.square(t));


#Calculate the exponential of all elements in the input array

r = np.array([[4,9],[16,81]],dtype=np.float64);

print(np.exp(r));

v = np.array([10,100,1000,10000,100000,1000000]);

print(np.log(v));


p = np.array([np.pi/6, np.pi/2,np.pi/3]);

print(np.sin(p));


k = np.array([[1,2],[3,4]]);

print(np.sum(k));

print(np.sum(k, axis=0));
print(np.sum(k, axis=1));


#Transpose

m = np.array([[1,2],[3,4]]);

print(m.T);

n = np.array([[1,2,3]]);

print(n.T);

z = np.array([[1,2,3],[4,5,6]]);

print(z.T);

print(n);
print(n.shape);
print(n.T);
print(n.T.shape);

 
#Data Type Conversion

newArray = np.array([1,2,2.5]);

print(newArray);
print(newArray.astype(int));


#Dimension Expansion

arrayX = np.array([1,2]);

print(arrayX.shape);

arrayX = np.expand_dims(arrayX,axis=0);
print(arrayX.shape);

arrayX = np.expand_dims(arrayX,axis=0);
print(arrayX.shape);

arrayX = np.expand_dims(arrayX,axis=0);
print(arrayX.shape);
print(type(arrayX));
print(arrayX.ndim);
print(arrayX.reshape(2,1,1,1));


arrayY = np.array([1,2]);

print(arrayY.shape);

arrayY = np.expand_dims(arrayY,axis=1);
print(arrayY.shape);

arrayY = np.expand_dims(arrayY,axis=1);
print(arrayY.shape);

arrayY = np.expand_dims(arrayY,axis=1);
print(arrayY.shape);
print(type(arrayY));
print(arrayY.ndim);
print(arrayY.reshape(2,1,1,1));


