def main():
    fname = "example.text"
    with open(fname, "r", encoding="utf-8") as file:
        line_count = sum(1 for line in file)
        print(f"Total number of lines in {fname}: {line_count}")

if __name__ == "__main__":
    main()