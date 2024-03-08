import time
from llm_utils import num_tokens_consumed_by_chat_request

class TokenBucket:
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
    def __init__(self, request_limit_per_minute, token_limit_per_minute, token_counter):
        # Rate limits
        self.request_limit = request_limit_per_minute
        self.token_limit = token_limit_per_minute

        # Token counter
        self.token_counter = token_counter

        # Buckets
        self._request_bucket = TokenBucket(self.request_limit / 60.0, self.request_limit)
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
    def __init__(self, request_limit=3500, token_limit=90000):
        super().__init__(
            request_limit_per_minute=request_limit,
            token_limit_per_minute=token_limit,
            token_counter=num_tokens_consumed_by_chat_request
        )