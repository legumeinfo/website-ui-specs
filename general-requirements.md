# General Requirements
  
- Searches should generate URLs containing query string search parameters for easy sharing. Likewise, URLs with query strings should populate form and execute search.
- The promise returned by the service function must be cancelable. This is to avoid race conditions when the service is being slow and/or the user makes another request before the previous one has been fulfilled. This can be done with the LisCancelPromiseController class.
- Search results should remain, not be cleared, when the form is updated by the user. The results persist until new search results are received.
