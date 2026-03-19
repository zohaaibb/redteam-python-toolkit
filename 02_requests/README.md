# Day 02: requests Library

## Scripts
- `website_checker.py` - Checks if sites are up, shows server info, title, response time

## What I Learned
- **Status codes**: 200 = OK, 404 = Not Found, 403 = Forbidden, 301/302 = Redirects
- **Headers**: Servers reveal info like Server, Content-Type, Cookies
- **Timeouts**: Without them, script hangs forever on dead sites
- **Error handling**: Different exceptions for different failures
- **None handling**: Functions can return None, always check before using

## What I Broke
| Change | Result | Lesson |
|--------|--------|--------|
| Removed timeout | Script hung on dead site | Timeouts are essential |
| Removed try/except | Script crashed on error | Error handling = robustness |
| Used fake URL | ConnectionError caught it | Different errors = different handling |
| Forgot title check | Script crashed on .upper() | Always check for None |

## Feature I Added
- Response time measurement: `response.elapsed.total_seconds()`
- Safe title extraction with None check

## Questions I Can Answer Now
- [x] What's the difference between 404 and 403?
- [x] Why use try/except?
- [x] What happens when .find() doesn't find anything?
- [x] How to handle functions that return None?
- [x] How to measure response time?

## Next
Day 03: subprocess - running system commands from Python
