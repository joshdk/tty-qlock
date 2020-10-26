#### General ####

# All target for when make is run on its own.
.PHONY: all
all: style

#### Linting ####

# Format code. Unformatted code will fail in CI.
.PHONY: style
style:
ifdef GITHUB_ACTIONS
	goimports -l .
else
	goimports -l -w .
endif

#### Linting ####

# Build binary.
.PHONY: build
build:
	@mkdir -p dist
	go build -ldflags='-s -w' -o dist/qlock main.go
	@echo 'Binary build! Run it like so:'
	@echo '  $$ ./dist/qlock'

#### Release ####

# Build and publish binaries as Github release artifacts.
.PHONY: release
release:
ifdef GITHUB_ACTIONS
	goreleaser release
else
	goreleaser --rm-dist --skip-publish --skip-validate --snapshot
endif
