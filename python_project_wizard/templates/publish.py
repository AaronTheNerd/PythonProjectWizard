from scripts.utils import build, clean, upgrade_twine, publish

def main() -> None:
    clean()
    build()
    upgrade_twine()
    publish()
    clean()

if __name__ == "__main__":
    main()