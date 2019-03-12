
## Checker

```go
// Commentf returns an infomational value to use with Assert or Check calls.
// If the checker test fails, the provided arguments will be passed to
// fmt.Sprintf, and will be presented next to the logged failure.
//
// For example:
//
//     c.Assert(v, Equals, 42, Commentf("Iteration #%d failed.", i))
//
// Note that if the comment is constant, a better option is to
// simply use a normal comment right above or next to the line, as
// it will also get printed with any errors:
//
//     c.Assert(l, Equals, 8192) // Ensure buffer size is correct (bug #123)
//
```
Commentf

```go
// The Not checker inverts the logic of the provided checker.  The
// resulting checker will succeed where the original one failed, and
// vice-versa.
//
// For example:
//
//     c.Assert(a, Not(Equals), b)
//
```
Not

```go
// The IsNil checker tests whether the obtained value is nil.
//
// For example:
//
//    c.Assert(err, IsNil)
//
```
IsNil

```go
// The NotNil checker verifies that the obtained value is not nil.
//
// For example:
//
//     c.Assert(iface, NotNil)
//
// This is an alias for Not(IsNil), made available since it's a
// fairly common check.
//
```
NotNil

```go
// The Equals checker verifies that the obtained value is equal to
// the expected value, according to usual Go semantics for ==.
//
// For example:
//
//     c.Assert(value, Equals, 42)
//
```
Equals

```go
// The DeepEquals checker verifies that the obtained value is deep-equal to
// the expected value.  The check will work correctly even when facing
// slices, interfaces, and values of different types (which always fail
// the test).
//
// For example:
//
//     c.Assert(value, DeepEquals, 42)
//     c.Assert(array, DeepEquals, []string{"hi", "there"})
//
```
DeepEquals

```go
// The HasLen checker verifies that the obtained value has the
// provided length. In many cases this is superior to using Equals
// in conjunction with the len function because in case the check
// fails the value itself will be printed, instead of its length,
// providing more details for figuring the problem.
//
// For example:
//
//     c.Assert(list, HasLen, 5)
//
```
HasLen

```go
// The ErrorMatches checker verifies that the error value
// is non nil and matches the regular expression provided.
//
// For example:
//
//     c.Assert(err, ErrorMatches, "perm.*denied")
//
```
ErrorMatches

```go
// The Matches checker verifies that the string provided as the obtained
// value (or the string resulting from obtained.String()) matches the
// regular expression provided.
//
// For example:
//
//     c.Assert(err, Matches, "perm.*denied")
//
```
Matches

```go
// The Panics checker verifies that calling the provided zero-argument
// function will cause a panic which is deep-equal to the provided value.
//
// For example:
//
//     c.Assert(func() { f(1, 2) }, Panics, &SomeErrorType{"BOOM"}).
//
//
```
Panics

```go
// The PanicMatches checker verifies that calling the provided zero-argument
// function will cause a panic with an error value matching
// the regular expression provided.
//
// For example:
//
//     c.Assert(func() { f(1, 2) }, PanicMatches, `open.*: no such file or directory`).
//
//
```
PanicMatches

```go
// The FitsTypeOf checker verifies that the obtained value is
// assignable to a variable with the same type as the provided
// sample value.
//
// For example:
//
//     c.Assert(value, FitsTypeOf, int64(0))
//     c.Assert(value, FitsTypeOf, os.Error(nil))
//
```
FitsTypeOf

```go
// The Implements checker verifies that the obtained value
// implements the interface specified via a pointer to an interface
// variable.
//
// For example:
//
//     var e os.Error
//     c.Assert(err, Implements, &e)
//
```
Implements


