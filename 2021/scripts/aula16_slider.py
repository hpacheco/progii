import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

xx = np.arange(0.0, 2.0, 0.01)
yy = np.sin(2*np.pi*xx)

line, = plt.plot(xx,yy)
rect = plt.axes([0.3,0.9,0.5,0.04])
# um botão de seleção exclusiva
slider = Slider(rect, 'Freq', 0.1, 30.0, valinit=2, valstep=0.5)

# a função que reage ao evento recebe o novo valor
def reage(freq):
    # altera a curva desenhada
    line.set_ydata(np.sin(freq*np.pi*xx))
    plt.draw()

slider.on_changed(reage)
plt.show()