import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# calcula um seno
xx = np.arange(0.0, 2.0, 0.01)
yy = np.sin(2*np.pi*xx)

_,ax = plt.subplots()

# desenha o gráfico, ax é o objeto
ln, = ax.plot(xx,yy)

# um retângulo perto do canto superior direito
rect = plt.axes([0.7, 0.9, 0.25, 0.07])
# um botão
button = Button(rect,'Mostrar / Esconder')

# a função que reage ao evento
def reage(info):
    # lê e altera a visibilidade do gráfico
    ax.set_visible(not ax.get_visible())
    plt.draw()

# liga o evento à função
button.on_clicked(reage)
plt.show()