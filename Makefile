render:
	pandoc 2021/README.md -t html --standalone --metadata title="20/21" > 2021/index.html
	perl -i -pe's/.ipynb/.html/g' 2021/index.html
	
	pandoc projetos/Projeto0.md -t html --mathjax --standalone --metadata title="Projeto 0" > projetos/Projeto0.html
	pandoc projetos/Projeto1.md -t html --mathjax --standalone --metadata title="Projeto 1" > projetos/Projeto1.html
	pandoc README.md -t html --standalone --metadata title="21/22" > index.html
	perl -i -pe's/.md/.html/g' index.html
