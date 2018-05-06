all: read clean

# compile with table of contents
# add "\tableofcontents" in doc
all-tbc:
	pdflatex *.tex
	pdflatex *.tex
	open *.pdf
	rm *.out *.aux *.log

edit: *.tex
	open *.tex

compile: 
	pdflatex *.tex

read: compile
	open *.pdf

clean:
	rm *.out *.aux *.log
