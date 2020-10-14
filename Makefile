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
