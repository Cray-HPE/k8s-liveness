# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.4.4] - 2024-10-10
### Added
- Added type hints and `py.typed`

## [1.4.3] - 2024-08-21
### Changed
- Change how RPM release value is set

## [1.4.2] - 2024-08-21
### Added
- Publish RPM to install package to system Python

### Changed
- Spelling corrections.
- Disabled concurrent Jenkins builds on same branch/commit
- Added build timeout to avoid hung builds
- Added `MANIFEST.in` file to make Python source distribution installable
- Build Python package in Docker container

### Removed
- Removed defunct files leftover from previous versioning system

### Dependencies
- Bump `tj-actions/changed-files` from 37 to 44 ([#18](https://github.com/Cray-HPE/k8s-liveness/pull/18), [#20](https://github.com/Cray-HPE/k8s-liveness/pull/20), [#22](https://github.com/Cray-HPE/k8s-liveness/pull/22), [#23](https://github.com/Cray-HPE/k8s-liveness/pull/23), [#25](https://github.com/Cray-HPE/k8s-liveness/pull/25), [#26](https://github.com/Cray-HPE/k8s-liveness/pull/26), [#27](https://github.com/Cray-HPE/k8s-liveness/pull/27))
- Bump `actions/checkout` from 3 to 4 ([#19](https://github.com/Cray-HPE/k8s-liveness/pull/19))
- Bump `stefanzweifel/git-auto-commit-action` from 4 to 5 ([#21](https://github.com/Cray-HPE/k8s-liveness/pull/21))

## [1.4.1] - 2022-12-20
### Added
- Add Artifactory authentication to Jenkinsfile

## [1.4.0] - 2022-08-10
### Changed
- Convert to gitflow/gitversion.