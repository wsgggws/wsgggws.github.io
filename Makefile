.PHONY: all dev build clean

# Python executable
PYTHON = .venv/bin/python
# Image optimization script
SCRIPT = optimize_images.py

all: dev

# Create virtual environment if not exists
.venv:
	python3 -m venv .venv
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install Pillow

# Generate and optimize cover images
images: .venv
	$(PYTHON) $(SCRIPT)

# Run local development server
dev: images
	hugo server --disableFastRender

# Build for production
build: images
	hugo --gc --minify

# Clean build artifacts
clean:
	rm -rf public resources
