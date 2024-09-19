up-with-logs:
	@docker compose up -d
	@docker compose logs -f python-producer python-consumer
