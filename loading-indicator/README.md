# Loading indicator

This is the requirements doc for loading indicators to be implemented on the LIS Jekyll website.
It's a very simple spec intended to force consistency across the site.

## Specification version
Version: 1.0.0

<details>

An initial implementation of the loading indicator functionality was completed in May of 2023 (see [Web Components PR #113](https://github.com/legumeinfo/web-components/pull/113)).

</details>

## Input

- something is being loaded

### Mockup

None

## Output

- The part of the page data is being for is covered by a semi-opaque element
- The [UIkit spinner](https://getuikit.com/docs/spinner) is placed at the vertical and horizontal center of the covering element
- An alert element can be used to indicate loading status, e.g. load failed, load success, something else

### Mockup

None

## Implementation notes

None
