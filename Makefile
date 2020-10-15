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

#### Release ####

# Compress binaries with UPX.
.PHONY: compress
compress:
	upx --best --ultra-brute dist/qlock_*/qlock*

# Build and publish binaries as Github release artifacts.
.PHONY: release
release:
ifdef GITHUB_ACTIONS
	goreleaser release
else
	goreleaser --rm-dist --skip-publish --skip-validate --snapshot
endif
