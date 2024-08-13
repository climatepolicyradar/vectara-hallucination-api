.PHONY: build run deploy clean

build:
	docker build -t vectara-api .

run:
	docker run -p 80:80 vectara-api

deploy: build
	docker tag vectara-api:latest 845035659285.dkr.ecr.eu-west-1.amazonaws.com/vectara-api:latest
	docker push 845035659285.dkr.ecr.eu-west-1.amazonaws.com/vectara-api:latest

clean:
	docker rmi vectara-api
