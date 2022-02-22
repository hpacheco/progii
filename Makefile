render:
	pandoc 2021/README.md -t html > 2021/index.html
	perl -i -pe's/.ipynb/.html/g' 2021/index.html
	pandoc projetos/Projeto0.md -t html --mathjax --standalone > projetos/Projeto0.html
	pandoc README.md -t html > index.html
	perl -i -pe's/.md/.html/g' index.html
