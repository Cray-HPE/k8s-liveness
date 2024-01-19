# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- Spelling corrections.
- Disabled concurrent Jenkins builds on same branch/commit
- Added build timeout to avoid hung builds

### Removed
- Removed defunct files leftover from previous versioning system

### Dependencies
- Bump `tj-actions/changed-files` from 37 to 42 ([#18](https://github.com/Cray-HPE/k8s-liveness/pull/18), [#20](https://github.com/Cray-HPE/k8s-liveness/pull/20), [#22](https://github.com/Cray-HPE/k8s-liveness/pull/22), [#23](https://github.com/Cray-HPE/k8s-liveness/pull/23), [#25](https://github.com/Cray-HPE/k8s-liveness/pull/25))
- Bump `actions/checkout` from 3 to 4 ([#19](https://github.com/Cray-HPE/k8s-liveness/pull/19))
- Bump `stefanzweifel/git-auto-commit-action` from 4 to 5 ([#21](https://github.com/Cray-HPE/k8s-liveness/pull/21))

## [1.4.1] - 2022-12-20
### Added
- Add Artifactory authentication to Jenkinsfile

## [1.4.0] - 2022-08-10
### Changed
- Convert to gitflow/gitversion.