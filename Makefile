# Makefile for scaling-palm-tree
# Legal Advocacy & Authorized Rep Services Repository

.PHONY: help init clean test build install lint format docs

# Default target
.DEFAULT_GOAL := help

help: ## Display this help message
	@echo "scaling-palm-tree - Legal Advocacy & Authorized Rep Services"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

init: ## Initialize the project (install dependencies, setup environment)
	@echo "Initializing project..."
	@mkdir -p docs
	@mkdir -p src
	@mkdir -p tests
	@echo "Project directories created."
	@echo "Please install required dependencies for your specific implementation."

clean: ## Clean up generated files and caches
	@echo "Cleaning up..."
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete
	@find . -type d -name '*.egg-info' -delete
	@find . -type f -name '.DS_Store' -delete
	@rm -rf dist/ build/ .pytest_cache/ .coverage htmlcov/
	@echo "Cleanup complete."

test: ## Run tests
	@echo "Running tests..."
	@if [ -d "tests" ]; then \
		echo "Test directory found. Please configure your test runner."; \
	else \
		echo "No tests directory found. Run 'make init' first."; \
	fi

build: ## Build the project
	@echo "Building project..."
	@echo "Configure build steps for your specific implementation."

install: ## Install project dependencies
	@echo "Installing dependencies..."
	@echo "Please configure dependency installation for your specific stack."

lint: ## Run linting checks
	@echo "Running linting checks..."
	@echo "Configure linting tools for your specific implementation."

format: ## Format code
	@echo "Formatting code..."
	@echo "Configure code formatting tools for your specific implementation."

docs: ## Generate documentation
	@echo "Generating documentation..."
	@mkdir -p docs
	@echo "Configure documentation generation for your specific implementation."

.PHONY: status
status: ## Show git status
	@git status

.PHONY: pull
pull: ## Pull latest changes from remote
	@git pull

.PHONY: push
push: ## Push changes to remote
	@git push
