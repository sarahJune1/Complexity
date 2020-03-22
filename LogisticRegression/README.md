# Logistic Mapping & Population Dynamics


### Reading Material :

_On the importance of nonlinear modeling in computer performance prediction_

https://arxiv.org/abs/1305.4924

_Newton's Clock: Chaos in the Solar System_

https://aapt.scitation.org/doi/abs/10.1119/1.18429?journalCode=ajp

_Henri Poincaré - Sensitive Dependence on Initial Conditions_

http://www.chaos.umd.edu/misc/poincare.html

Henri Poincaré - Science and Method

https://archive.org/details/sciencemethod00poinuoft/page/14/mode/2up

#### Copied from Mathematica Notebook in Folder

TextSentences[
  WikipediaData["PageID" -> "18137", "ArticlePlaintext"]][[;; 2]]

  {"The logistic map is a polynomial mapping (equivalently, recurrence \
relation) of degree 2, often cited as an archetypal example of how \
complex, chaotic behaviour can arise from very simple non-linear \
dynamical equations.", "The map was popularized in a 1976 paper by \
the biologist Robert May, in part as a discrete-time demographic \
model analogous to the logistic equation first created by Pierre \
François Verhulst."}

Formula:

def logisticMap(x ,r):
    cap = r * (x - x**2)
    return cap
