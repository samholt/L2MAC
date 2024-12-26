"""
This example demonstrates how to generate a codebase for a complex URL
 shortener application.
"""
from l2mac import generate_codebase

codebase: dict = generate_codebase(
    r"""
**Online URL Shortening Service**

**Overview**:
A service that allows users to submit long URLs and then receive a shortened
 version of that URL for ease of sharing.

**Functional Requirements to implement**:

1. **URL Shortening**:
   - [ ] 1.1. Users can input a URL to be shortened.
   - [ ] 1.2. The system validates that the URL is active and legitimate.
   - [ ] 1.3. The system generates a unique shortened URL.
   - [ ] 1.4. Users can choose custom short links (subject to availability).

2. **Redirection**:
   - [ ] 2.1. Accessing the shortened URL redirects to the original URL.

3. **Analytics**:
   - [ ] 3.1. Users can view statistics about their shortened URLs.
   - [ ] 3.2. View number of clicks.
   - [ ] 3.3. View date/time of each click.
   - [ ] 3.4. View geographical location of the clicker.

4. **User Accounts**:
   - [ ] 4.1. Users can create accounts.
   - [ ] 4.2. Account holders can view all their shortened URLs.
   - [ ] 4.3. Account holders can edit or delete their shortened URLs.
   - [ ] 4.4. Account holders can view analytics for all their shortened URLs.

5. **Admin Dashboard**:
   - [ ] 5.1. Administrators can view all shortened URLs.
   - [ ] 5.2. Administrators can delete any URL or user account.
   - [ ] 5.3. Administrators can monitor system performance and analytics.

6. **Expiration**:
   - [ ] 6.1. Users can set an expiration date/time for the shortened URL.
""",
    steps=10,
)

# it will print the codebase (repo) complete with all the files as a dictionary
print(
    codebase
)
