# Exercice PYTHON NUMPY machine learning (10/30) ------------------------------
import numpy as np
def initialisation(m, n):
    t = np.random.rand(m, n) # randn: generates samples from the normal distribution
    one = np.ones((m, 1))
    return np.hstack((t, one)) # np.concatenate(..., axe=1)

print(initialisation(10, 5))

# Exercice PYTHON NUMPY Indexing Slicing Masking (11/30) ----------------------
from scipy import misc 
import matplotlib.pyplot as plt

face = misc.face(gray=True)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()

h = face.shape[0]
w = face.shape[1]
zoom_face = face[h//4: -h//4, w//4: -w//4]
zoom_face[zoom_face > 150] = 255
plt.imshow(zoom_face, cmap=plt.cm.gray)
plt.show()

# Exercice PYTHON NUMPY STATISTIQUES et MATHÉMATIQUES (12/30) -----------------
np.random.seed(0)
a = np.random.randint(0, 100, [10, 5])
d = (a - a.mean(axis=0))/ a.std(axis=0)