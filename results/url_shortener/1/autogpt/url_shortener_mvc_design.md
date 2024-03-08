# MVC Architecture Design

## Model
- URL
  - id
  - long_url
  - short_url
  - custom_alias
  - click_count
  - expiration_date

## View
- Home page
  - Input for long URL
  - Input for custom alias (optional)
  - Button to generate short URL
  - Display short URL
  - Display click stats

## Controller
- Generate short URL
  - Create unique alias
  - Save URL to the model
  - Return short URL
- Redirect short URL
  - Retrieve long URL from the model
  - Increment click count
  - Redirect to long URL
- Delete expired URLs
  - Check expiration date
  - Remove expired URLs from the model
