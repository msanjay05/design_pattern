from singleton import DatabaseConnection


def main() -> None:
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(db1.connect("postgres://localhost/app"))
    print(db2.query("SELECT * FROM users"))
    print(f"Same instance: {db1 is db2}")


if __name__ == "__main__":
    main()
