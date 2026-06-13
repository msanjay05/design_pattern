from proxy import ImageProxy


def main() -> None:
    image = ImageProxy("photo.png")
    print("Proxy created (image not loaded yet)")
    print(image.display())


if __name__ == "__main__":
    main()
