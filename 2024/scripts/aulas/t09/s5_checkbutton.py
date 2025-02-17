import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

xx = np.arange(0.0, 2.0, 0.01)
yy1 = np.sin(2*np.pi*xx)
yy2 = np.sin(4*np.pi*xx)

ln1, = plt.plot(xx,yy1)
ln2, = plt.plot(xx,yy2)

rect = plt.axes([0.7,0.9,0.1,0.08])
# um botão de seleção
button = CheckButtons(rect,('2 Hz','4 Hz'),(True,True))

def reage_ln(ln):
    ln.set_visible(not ln.get_visible())
    plt.draw()

# a função que reage ao evento recebe a opção
def reage(label):
    if label=='2 Hz': reage_ln(ln1)
    elif label=='4 Hz': reage_ln(ln2)

button.on_clicked(reage)
plt.show()