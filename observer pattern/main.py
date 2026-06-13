from observer import EmailSubscriber, NewsPublisher, SmsSubscriber


def main() -> None:
    publisher = NewsPublisher()
    publisher.subscribe(EmailSubscriber("user@example.com"))
    publisher.subscribe(SmsSubscriber("+1-555-0100"))

    for notification in publisher.publish("Market hits record high"):
        print(notification)


if __name__ == "__main__":
    main()
