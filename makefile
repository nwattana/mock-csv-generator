PWD = $(shell pwd)
GROUPID = $(shell id -g)
USERID = $(shell id -u)


all:
	@echo "make create-image"
	@echo "make run"

create-image:
	docker build -t csv-generator .

run-basic:
	docker run --rm -v $(PWD):/app csv-generator

run:
	mkdir -p $(PWD)/output
	docker run --rm -v $(PWD)/output:/app/output --user $(USERID):$(GROUPID) csv-generator
	# sudo chown $(USER):$(USER) -R $(PWD)/output