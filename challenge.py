from tools import get_available_computers


def run_challenge():

    print("=" * 60)
    print("CHALLENGE: COMPUTER LAB ASSISTANT")
    print("=" * 60)

    print("\nChallenge Question:")
    print("Which available computers have at least 16 GB RAM,")
    print("and what is the total RAM of those computers?")

    # Get all available computers
    available = get_available_computers()

    # Store computers with at least 16 GB RAM
    selected = []

    for computer in available:

        if computer["ram"] >= 16:
            selected.append(computer)

    # Calculate total RAM
    total_ram = 0

    for computer in selected:
        total_ram += computer["ram"]

    print("\nAvailable computers with at least 16 GB RAM:")

    for computer in selected:

        print(
            f"{computer['computer_id']} - "
            f"{computer['ram']} GB RAM - "
            f"{computer['storage']} - "
            f"{computer['os']}"
        )

    print(f"\nTotal RAM: {total_ram} GB")


if __name__ == "__main__":
    run_challenge()