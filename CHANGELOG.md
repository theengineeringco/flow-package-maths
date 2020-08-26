# [1.1.0-develop.3](https://github.com/theengineeringco/flow-py-library-general_maths/compare/v1.1.0-develop.2...v1.1.0-develop.3) (2020-08-25)


### Bug Fixes

* Updated namespace (previous commits) ([374fcd2](https://github.com/theengineeringco/flow-py-library-general_maths/commit/374fcd21282891b41c5677c517c186651c5a0319))

# [1.1.0-develop.2](https://github.com/theengineeringco/flow-py-library-general_maths/compare/v1.1.0-develop.1...v1.1.0-develop.2) (2020-08-24)


### Bug Fixes

* Was using has_data incorrectly. Now improved. ([9687f4c](https://github.com/theengineeringco/flow-py-library-general_maths/commit/9687f4c4d17857ed363a1fb92ada2b2a74e0a3f4))


### Performance Improvements

* Have number (unions) in Linspace. ([634343c](https://github.com/theengineeringco/flow-py-library-general_maths/commit/634343cd808018c0dcb4f11aff4d88ad471c198c))

# [1.1.0-develop.1](https://github.com/theengineeringco/flow-py-library-general_maths/compare/v1.0.0...v1.1.0-develop.1) (2020-08-20)


### Features

* updated all relevant components to allow unions ([83b41a0](https://github.com/theengineeringco/flow-py-library-general_maths/commit/83b41a0ab20f050ec0b3a48b3e02c7e8729a5783))
* Updated to new Python Abs 2.0 changes. ([469baae](https://github.com/theengineeringco/flow-py-library-general_maths/commit/469baae3285c4dee4decb6582a3be1982c8dc9d5))

# 1.0.0 (2020-08-04)


### Bug Fixes

* All components' debug messages only in Debug mode. ([e28b61e](https://github.com/theengineeringco/flow-py-library-general_maths/commit/e28b61eece4bfe93e58a5b8c8be42ffb6b7883ec))
* Inports of some trig functions were incorrectly typed. ([9fa1b19](https://github.com/theengineeringco/flow-py-library-general_maths/commit/9fa1b19aa4e4292c6ced069692c6d7ede8e0210b))

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v0.1.0 - 2020-07-2

### Added

- Assemble arrays and perform basic maths on them
- Logging (instead of `print` statements)

### Changed

- Moved to new Python Abstraction Runtime: https://github.com/theengineeringco/flow-py/pull/92
- Overhaul of component definitions (removed Runs and modified testing procedures)
- Components no longer have a sub-function and a process, all maths is done directly in the process!

## v0.0.1 - 2020-07-02

### Added

- Initial Commit

[0.0.1]: https://github.com/theengineeringco/flow-py-library-general_maths
