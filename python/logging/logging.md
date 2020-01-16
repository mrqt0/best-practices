# Logging

## General logging best pratices

[Tip: Use a Human-Readable Logging Format](https://reflectoring.io/logging-format/):
The article uses Java, but the findings apply to any language.
- Logs should be human-readable. Use a format that allows quickly skimming
  through the logs.
- Information you should include:
  - Date and time: to correlate to other events
  - Logging level: to be able to filter
  - Name or source of log message
  - Message
  - Stack trace (in case of errors)
  - Message ID (optional): to quickly find certain events
  - Thread name (optional)
  - Contextual information (optional): Should not distract

[Tip: Provide Contextual Information in Log Messages](https://reflectoring.io/logging-context/)
- You should provide contextual information:
  - "not found" errors: which key, what type of item
  - exceptions: data constellation, root exception
  - validation error: use case, name of field, reason and value for which data
    validation failed
  - status change: id, type, previous and new state.

[3 Use Cases Where Structured Log Data Really Helps](https://reflectoring.io/structured-log-data/)
- Context information in the form of key/values pairs can really help:
  - To trace requests across services
  - To get info how a system ended up in a certain state, by printing its
    state variables
    
