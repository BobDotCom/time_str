# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) since
v1.0.0.

## [Unreleased]

### Added

- `parse_interval` shortcut function.
- Type hints
- `max_unit` kwarg to `IntervalConverter` constructor and `parse_interval` function.
- New precise methods to `IntervalConverter` for precise conversions:
  `timedelta_precise()` and `datetime_precise()`.
- New `IntervalConverter.datetime_relative()` shortcut method.

### Changed

- Renamed `Converter` to `IntervalConverter`.
- `input_string` attribute of `IntervalConverter` is now a read-only property.
- `IntervalConverter.convert()` is now `IntervalConverter.timedelta_relative()`.

### Removed

- `time_str.convert` shortcut function.
- `converted_string`, `split_string`, `pattern`, `raw_output` and `output` attributes of
  `IntervalConverter` have been removed or are now private.

## [0.1.1] - 2022-05-18

No notable changes.

## [0.1.0-post.2] - 2021-08-26

### Added

- Support for decades and centuries

## [0.0.3-post.1] - 2021-02-01

No notable changes.

## [0.0.3] - 2021-01-31

No notable changes.

## [0.0.3-dev.2] - 2021-01-31

No notable changes.

## [0.0.3-dev.1] - 2021-01-31

No notable changes.

## [0.0.2-post.1] - 2021-01-31

### Fixed

- Month calculation issues

## [0.0.2] - 2020-12-30

No notable changes.

## [0.0.2-dev.3] - 2020-12-30

No notable changes.

## [0.0.2-dev.2] - 2020-12-30

### Added

- `convert` shortcut function

## [0.0.2-dev.1] - 2020-12-30

No notable changes.

## [0.0.1] - 2020-12-30

### Added

- Converter class

[unreleased]: https://github.com/BobDotCom/time_str/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/BobDotCom/time_str/compare/v0.1.0-post.2...v0.1.1
[0.1.0-post.2]:
  https://github.com/BobDotCom/time_str/compare/v0.0.3-post.1...v0.1.0-post.2
[0.0.3-post.1]: https://github.com/BobDotCom/time_str/compare/v0.0.3...v0.0.3-post.1
[0.0.3]: https://github.com/BobDotCom/time_str/compare/v0.0.3-dev.2...v0.0.3
[0.0.3-dev.2]: https://github.com/BobDotCom/time_str/compare/v0.0.3-dev.1...v0.0.3-dev.2
[0.0.3-dev.1]:
  https://github.com/BobDotCom/time_str/compare/v0.0.2-post.1...v0.0.3-dev.1
[0.0.2-post.1]: https://github.com/BobDotCom/time_str/compare/v0.0.2...v0.0.2-post.1
[0.0.2]: https://github.com/BobDotCom/time_str/compare/v0.0.2-dev.3...v0.0.2
[0.0.2-dev.3]: https://github.com/BobDotCom/time_str/compare/v0.0.2-dev.2...v0.0.2-dev.3
[0.0.2-dev.2]: https://github.com/BobDotCom/time_str/compare/v0.0.2-dev.1...v0.0.2-dev.2
[0.0.2-dev.1]: https://github.com/BobDotCom/time_str/compare/v0.0.1...v0.0.2-dev.1
[0.0.1]: https://github.com/BobDotCom/time_str/commits/v0.0.1
