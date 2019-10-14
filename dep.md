# Dep

## Dep Help

Dep is a tool for managing dependencies for Go projects

Usage: "dep [command]"

Commands:

- `init`     Set up a new Go project, or migrate an existing one
- `status`   Report the status of the project's dependencies
- `ensure`   Ensure a dependency is safely vendored in the project
- `version`  Show the dep version information
- `check`    Check if imports, Gopkg.toml, and Gopkg.lock are in sync

Examples:

- `dep init`                               set up a new project
- `dep ensure`                             install the project's dependencies
- `dep ensure -update`                     update the locked versions of all dependencies
- `dep ensure -add github.com/pkg/errors`  add a dependency to the project

Use "dep help [command]" for more information about a command.

## Version rules

Version rules can be used in either [[constraint]] or [[override]] stanzas. There are three types of version rules - version, branch, and revision. At most one of the three types can be specified.

## version

`version` is a property of `constraints` and `overrides`. It is used to specify version constraint of a specific dependency. It can be used to target an arbitrary VCS tag, or a semantic version, or a range of semantic versions.

Specifying semantic version ranges can be done using the following operators:

```ini
=       : equal
!=      : not equal
>       : greater than
<       : less than
>=      : greater than or equal to
<=      : less than or equal to
-       : literal range. E.g., 1.2 - 1.4.5 is equivalent to >= 1.2, <= 1.4.5
~       : minor range. E.g., ~1.2.3 is equivalent to >= 1.2.3, < 1.3.0
^       : major range. E.g., ^1.2.3 is equivalent to >= 1.2.3, < 2.0.0
[xX*]   : wildcard. E.g., 1.2.x is equivalent to >= 1.2.0, < 1.3.0
```

You might, for example, include a rule that specifies version = "=2.0.0" to pin a dependency to version 2.0.0, or constrain to minor releases with: version = "~2.1.0". Refer to the semver library documentation for more info.

Note: When you specify a version without an operator, dep automatically uses the ^ operator by default. dep ensure will interpret the given version as the min-boundary of a range, for example:

- `1.2.3` becomes the range `>=1.2.3, <2.0.0`
- `0.2.3` becomes the range `>=0.2.3, <0.3.0`
- `0.0.3` becomes the range `>=0.0.3, <0.1.0`

`~` and `=` operators can be used with the versions. When a version is specified without any operator, dep automatically adds a caret operator, `^`. The caret operator pins the left-most non-zero digit in the version. For example:

- `^1.2.3` means `1.2.3 <= X < 2.0.0`
- `^0.2.3` means `0.2.3 <= X < 0.3.0`
- `^0.0.3` means `0.0.3 <= X < 0.1.0`

To pin a version of direct dependency in manifest, prefix the version with `=`. For example:

```ini
[[constraint]]
  name = "github.com/pkg/errors"
  version = "=0.8.0"
```

## Example

A sample `Gopkg.toml` with most elements present:

```ini
required = ["github.com/user/thing/cmd/thing"]

ignored = [
  "github.com/user/project/pkgX",
  "bitbucket.org/user/project/pkgA/pkgY"
]

noverify = ["github.com/something/odd"]

[metadata]
codename = "foo"

[prune]
  non-go = true

  [[prune.project]]
    name = "github.com/project/name"
    go-tests = true
    non-go = false

[[constraint]]
  name = "github.com/user/project"
  version = "1.0.0"

  [metadata]
  property1 = "value1"
  property2 = 10

[[constraint]]
  name = "github.com/user/project2"
  branch = "dev"
  source = "github.com/myfork/project2"

[[override]]
  name = "github.com/x/y"
  version = "2.4.0"

  [metadata]
  propertyX = "valueX"
```
