"""Module for choosing an author from a predefined list."""


class Authors:
    """Class for choosing an author."""

    __authors = (
        "denys_skovoronok",
        "denys_sidorov",
        "hlib_shramko",
        "kekish",
        "kostiantyn_osypenko",
        "maxym_dvolinskyi",
        "tliubov",
        "valentyn_yehoian",
        "vitalinakliuieva",
        "anzhela_maliarevych",
    )

    @staticmethod
    def display_authors():
        """Display authors."""
        for index, author in enumerate(Authors.__authors, 1):
            print(f"{index}. {author}")

    @staticmethod
    def choose_author():
        """Choose author."""
        authors = Authors.__authors
        print("Choose an author:\n")
        Authors.display_authors()
        while True:
            try:
                choice = int(input("Enter corresponding number: "))
                if 1 <= choice <= len(authors):
                    return authors[choice - 1]
                print(f"Invalid choice. minimum is 1, maximum is {len(authors)}")
            except ValueError:
                print("Please enter a valid number.")
