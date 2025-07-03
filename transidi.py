# idiom_search_app.py — main program
from idioms_bd import idioms


def search_idioms(query):
    query = query.lower()
    matches = {k: v for k, v in idioms.items() if query in k}
    return matches


def main():
    print("🎯 English Idiom Search (Type 'exit' to quit)")

    while True:
        user_input = input("\n🔍 Enter a keyword or idiom: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        results = search_idioms(user_input)

        if results:
            print(f"\n📘 Found {len(results)} idiom(s):\n")
            for idiom, meaning in results.items():
                print(f"👉 {idiom}\n   📝 {meaning}\n")
        else:
            print("❌ No idioms found matching your input.")


if __name__ == "__main__":
    main()
