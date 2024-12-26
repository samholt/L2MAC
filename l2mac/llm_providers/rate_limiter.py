"""
This module provides rate limiting functionality using the Token Bucket
algorithm.

Classes:
  TokenBucket: Implements the token bucket algorithm to control the rate of
  token consumption.
  RateLimiter: Manages rate limiting for requests and tokens using TokenBucket
  instances.
  ChatRateLimiter: A specialized RateLimiter for chat requests with predefined
  limits.

Functions:
  num_tokens_consumed_by_chat_request: Calculates the number of tokens consumed
  by a chat request.
"""
import time

from l2mac.llm_providers.openai import num_tokens_consumed_by_chat_request


class TokenBucket:
  """
  A token bucket rate limiter implementation.
  Attributes:
    rate (float): The rate at which tokens are added to the bucket (tokens per
      second).
    capacity (float): The maximum number of tokens the bucket can hold.
    tokens (float): The current number of tokens in the bucket.
    last_time (float): The last time tokens were added to the bucket.
  Methods:
    __init__(rate, capacity):
      Initializes the TokenBucket with a specified rate and capacity.
    consume(tokens=1):
      Attempts to consume a specified number of tokens from the bucket.
      Returns True if the tokens were successfully consumed, False otherwise.
  """
  def __init__(self, rate, capacity):
    self.rate = rate  # Tokens per second
    self.capacity = capacity
    self.tokens = self.capacity
    self.last_time = time.time()

  def consume(self, tokens=1):
    if tokens < 0:
      return False

    current_time = time.time()
    time_delta = current_time - self.last_time
    self.last_time = current_time

    # Add tokens based on the time passed
    self.tokens += time_delta * self.rate

    # Ensure the tokens do not exceed the capacity
    self.tokens = min(self.tokens, self.capacity)

    if self.tokens >= tokens:
      self.tokens -= tokens
      return True
    return False


class RateLimiter(object):
  """
  A class to enforce rate limiting on requests and tokens.
  Attributes:
    request_limit (int): The maximum number of requests allowed per minute.
    token_limit (int): The maximum number of tokens allowed per minute.
    token_counter (callable): A function that returns the number of tokens
      consumed by a request.
  Methods:
    consume(**kwargs):
      Consumes tokens and requests according to the rate limits.
      Blocks execution if the rate limit is exceeded until tokens and requests
        are available.
  """
  def __init__(self, request_limit_per_minute, token_limit_per_minute,
               token_counter):
    """
    Initializes the RateLimiter with the specified request and token limits.
    Blocks execution if the rate limit is exceeded until tokens and requests
    are available.
    Args:
      request_limit_per_minute (int): The maximum number of requests allowed
        per minute.
      token_limit_per_minute (int): The maximum number of tokens allowed per
        minute.
      token_counter (callable): A function that returns the number of tokens
        consumed by a request.
    """
    # Rate limits
    self.request_limit = request_limit_per_minute
    self.token_limit = token_limit_per_minute

    # Token counter
    self.token_counter = token_counter

    # Buckets
    self._request_bucket = TokenBucket(self.request_limit / 60.0,
                                       self.request_limit)
    self._token_bucket = TokenBucket(self.token_limit / 60.0, self.token_limit)

  def consume(self, **kwargs):
    num_tokens = self.token_counter(**kwargs)
    while not self._token_bucket.consume(num_tokens):
      if num_tokens > self.token_limit:
        num_tokens = self.token_limit // 2
      time.sleep(1 / self._token_bucket.rate)
    while not self._request_bucket.consume():
      time.sleep(1 / self._request_bucket.rate)


class ChatRateLimiter(RateLimiter):
  """
  A rate limiter specifically designed for chat-based requests.
  Inherits from the RateLimiter class and sets up limits for the number of
    requests
  and tokens that can be processed per minute.
  Attributes:
    request_limit (int): The maximum number of requests allowed per minute.
      Default is 3500.
    token_limit (int): The maximum number of tokens allowed per minute.
      Default is 90000.
  Methods:
    __init__(request_limit=3500, token_limit=90000):
      Initializes the ChatRateLimiter with specified request and token limits.
  """
  def __init__(self, request_limit=3500, token_limit=90000):
    super().__init__(
        request_limit_per_minute=request_limit,
        token_limit_per_minute=token_limit,
        token_counter=num_tokens_consumed_by_chat_request,
    )
