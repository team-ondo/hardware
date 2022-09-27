
.PHONY: run-state run-socket help

.DEFAULT_GOAL := help

run-state: ## Run state machine
	poetry run python src/state_machine.py

run-socket: ## Run socket
	poetry run python src/socket/socket_client.py

help: ## Show help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'