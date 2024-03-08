# URL Shortening Service API

## Endpoints

### POST /shorten

Request:

```
{
  "original_url": "https://www.example.com"
}
```

Response:

```
{
  "short_url": "a1B2c3"
}
```

### GET /{short_url}

Request:

```
GET /a1B2c3
```

Response:

```
{
  "original_url": "https://www.example.com"
}
```

## Error Handling

- 400 Bad Request: Invalid request or invalid URL
- 404 Not Found: Short URL not found