# Paginated search

This is the requirements doc for paginaged searches to be implemented on the LIS Jekyll website.
Rather than describing a specific UI element, this doc describe's parts of the UI that all paginated search elements on the LIS Jekyll website should have in common.
As such, the UI specs for all paginated search elements should reference this spec, and updating this spec implicitly updates all paginated search element specs. 

Note that this UI spec describes the UI portions of the paginated search element.
The implementation API is documented in the Web Component docs.

## Specification version
Version: 1.0.0

<details>

An initial implementation of the paginated search functionality was completed in December of 2022 (see [Web Components issue #21](https://github.com/legumeinfo/web-components/issues/21)).
New features have been added since then as needed.
However, since these were added in an ad-hoc manner without a formal specification, version 1.0.0 of this spec reflects the state of the paginated search implementation when this spec was first written.

</details>

## Input

- search form
- Next and Previous buttons (for navigating pages of reults)

### Mockup

None

## Output

- A loading spinner should be shown if/when data for the search form is being loaded, e.g. site-specific genera
- An error alert if the search form data failed to load
- A loading spinner should be shown when a search form is submitted
- An error alert if the search failed
- A warning alert if the search didn't find anything
- Text saying how many results were found and the range being shown on the current page
- A table that displays results
- Text between the Next and Previous buttons saying what page of results you're currently viewing and (opptionally) how many pages of results there are

### Mockup

None

## Implementation notes

- Previous search results should only be cleared when there's new search results to replace them, i.e. if a new search fails then the previous results should remain.
- The inputs of the search form should be added to the URL querystring parameters when the form is submitted. If any of these querystring parameters are present when the page is loaded, then their values should be put in the search form. Similarly, the presence of (some) of these querystring parameters when the page is loaded should cause a search to happen automatically.
- The Web browser's forward and back buttons should navigate the search history and update the querystring parameters and search form accordingly.
- All of this functionality should be encapsulated in an abstract Web Component that other paginated search components can extend.
- The search form, what querystring parameters trigger an automatic search, and the results table should all be configurable by the conrete paginated search implementations.
