PWD = $(shell pwd)


all:
	@echo "make create-image"
	@echo "make run"

create-image:
	docker build -t csv-generator .

run:
	docker run --rm -v $(PWD):/app csv-generator
