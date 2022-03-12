render:
	pandoc 2021/README.md -t html --standalone --metadata title="20/21" > 2021/index.html
	perl -i -pe's/.ipynb/.html/g' 2021/index.html
	
	pandoc projetos/Projeto0.md -t html --mathjax --standalone --metadata title="Projeto 0" > projetos/Projeto0.html
	pandoc projetos/Projeto1.md -t html --mathjax --standalone --metadata title="Projeto 1" > projetos/Projeto1.html
	pandoc projetos/Projeto2.md -t html --mathjax --standalone --metadata title="Projeto 2" > projetos/Projeto2.html
	pandoc README.md -t html --standalone --metadata title="21/22" > index.html
	perl -i -pe's/.md/.html/g' index.html
	
	cd scripts/projeto0; tree -H '.' --noreport --charset utf-8 -P "*.py" -o index.html
	cd scripts/projeto1; tree -H '.' --noreport --charset utf-8 -I "*_sols.py" -I "__pycache__" -I "*.html" -o index.html
	cd scripts/projeto2; tree -H '.' --noreport --charset utf-8 -I "*_sols.py" -I "__pycache__" -I "*.html" -o index.html
