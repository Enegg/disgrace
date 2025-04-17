"""Library's exception hierarchy.

`Exception` > `DiscordException` > ...
- `ClientException` +
  - `InvalidData`
  - `LoginFailure`
  - `SessionStartLimitReached` +
  - `ConnectionClosed`
  - `PrivilegedIntentsRequired`
  - `InteractionException`
    - `InteractionTimedOut` +
    - `InteractionResponded` +
    - `InteractionNotResponded` +
- `GatewayNotFound`
- `HttpException` +
  - `Forbidden` +
  - `NotFound` +
  - `DiscordServerError`
- `WebhookTokenMissing` ?
- `LocalizationKeyError` ?
"""
# + - likely a good idea
# ? - may not be needed


class DiscordException(Exception): ...


class ClientException(DiscordException): ...


class GatewayNotFound(DiscordException): ...


class HttpException(DiscordException): ...


class Forbidden(HttpException): ...


class NotFound(HttpException): ...


class DiscordServerError(HttpException): ...
