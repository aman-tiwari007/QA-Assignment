The target application is hosted on claude.ai and is protected by an
anti-bot challenge redirect mechanism.

During automation execution, the page is redirected to
`/api/challenge_redirect`, and the actual UI content is rendered dynamically
inside a protected iframe.

Due to this behavior, Playwright is unable to reliably locate or interact
with certain UI elements such as tabs and buttons in a headless or automated
environment.

This limitation was identified during debugging and has been documented
as part of the assignment.
