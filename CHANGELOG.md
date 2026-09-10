# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog.

## [Unreleased]

## [2026-04-17]

### Added

- Labs 07 to 12 with dedicated `starter/*` and `solution/*` branches.
- `CHANGELOG.md` to track notable changes.
- `CONTRIBUTING.md` with contribution, review, and security workflow.

### Changed

- Repository license changed from MIT to Creative Commons Attribution 4.0 International.
- README updated to document the attribution requirement and contribution workflow.
- GitLab project security posture strengthened:
  - protected branches for `main`, `starter/*`, and `solution/*`
  - protected tags for `v*`
  - merge blocked unless pipeline succeeds
  - merge blocked until discussions are resolved
  - committers cannot approve merge requests
  - merge request approval rule overrides disabled
