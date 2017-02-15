all: run

run: main.py
	python main.py

clean:
	rm *.png
	rm *.ppm
	rm *.pyc
