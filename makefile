PWD = $(shell pwd)
WHOAMI = $(shell whoami)


all:
	@echo "make create-image"
	@echo "make run"

create-image:
	docker build -t csv-generator .

run:
	docker run --rm -v $(PWD):/app --user $(WHOAMI) --env USER=$(WHOAMI)  csv-generator
