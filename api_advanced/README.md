# alu-scripting

Python scripts that use the Reddit API (via the `requests` module) to query
subreddit information.

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- `requests` module
- PEP 8 style, all files executable
- A custom `User-Agent` is set and redirects are never followed

## Tasks (directory `api_advanced`)

| File | Description |
|------|-------------|
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the subscriber count, 0 if invalid |
| `1-top_ten.py` | `top_ten(subreddit)` prints the first 10 hot post titles, `None` if invalid |
| `2-recurse.py` | `recurse(subreddit)` recursively returns all hot post titles, `None` if invalid |
| `3-count.py` | `count_words(subreddit, word_list)` recursively prints sorted keyword counts |

## Usage

```
$ python3 0-main.py programming
$ python3 1-main.py programming
$ python3 2-main.py programming
$ python3 3-main.py programming 'python java javascript'
```
