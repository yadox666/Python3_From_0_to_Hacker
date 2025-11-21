import argparse

def main():
    # Create the parser and add arguments
    parser = argparse.ArgumentParser(description="A script to process a file with specified options.")

    # Required positional arguments
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")

    # Optional argument with default value and choices
    parser.add_argument(
        "--format",
        choices=["json", "csv", "txt"],
        default="json",
        help="Output format (default: json)"
    )

    # Optional argument that is required (e.g., requires a user name)
    parser.add_argument(
        "--user",
        required=True,
        help="Username required for processing"
    )

    # Optional argument with type validation
    parser.add_argument(
        "--threshold",
        type=int,
        help="A threshold value (integer) for processing"
    )

    # Boolean flag (store_true means it’s a flag and sets to True if provided)
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    # Parse arguments
    args = parser.parse_args()

    # Use the arguments
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
    print(f"Output format: {args.format}")
    print(f"User: {args.user}")

    if args.threshold is not None:
        print(f"Threshold: {args.threshold}")
    
    if args.verbose:
        print("Verbose mode is enabled")

if __name__ == "__main__":
    main()
