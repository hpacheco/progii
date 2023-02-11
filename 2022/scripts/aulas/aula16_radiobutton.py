import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

xx = np.arange(0.0, 2.0, 0.01)
yy = np.sin(2*np.pi*xx)

ln, = plt.plot(xx,yy)

rect = plt.axes([0.7,0.9,0.1,0.08])
# um botão de seleção exclusiva
button = RadioButtons(rect,('2 Hz','4 Hz'))

def reage_ln(n):
    # altera a curva desenhada
    ln.set_ydata(np.sin(n*np.pi*xx))
    plt.draw()

# a função que reage ao evento recebe a opção
def reage(label):
    if label=='2 Hz': reage_ln(2)
    elif label=='4 Hz': reage_ln(4)

button.on_clicked(reage)
plt.show()