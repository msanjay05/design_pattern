from handlers import AuthHandler, BusinessHandler, RateLimitHandler


def main() -> None:
    chain = AuthHandler()
    chain.set_next(RateLimitHandler()).set_next(BusinessHandler())

    requests = [
        "GET /api/users",
        "GET /api/users token=abc",
        "GET /api/users token=abc burst",
        "GET /api/users token=abc",
    ]

    for request in requests:
        result = chain.handle(request)
        print(f"{request!r} -> {result}")


if __name__ == "__main__":
    main()
