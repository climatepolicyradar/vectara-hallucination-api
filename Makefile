deploy:
	docker build -t vectara-api .
	docker tag vectara-api:latest 845035659285.dkr.ecr.eu-west-1.amazonaws.com/vectara-api:latest
	docker push 845035659285.dkr.ecr.eu-west-1.amazonaws.com/vectara-api:latest