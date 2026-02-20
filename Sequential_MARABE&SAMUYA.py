import time
from dataclasses import dataclass

@dataclass
class MallVisitor:
    id: int
    items: list
    question: str


def sequential_version(visitors):
    print("Running Sequential Version...\n")
    start_time = time.time()

    for visitor in visitors:
        visitor_start = time.time()

        # Stage 1: Inspection
        print(f"[Sequential - Stage 1] Inspecting Visitor {visitor.id}'s items: {visitor.items}...")
        time.sleep(1)

        # Stage 2: Inquiry
        print(f"[Sequential - Stage 2] Answering Visitor {visitor.id}'s question: '{visitor.question}'")
        time.sleep(1.5)

        total_time = time.time() - visitor_start
        print(f"--- Finished Visitor {visitor.id}. Total processing time: {total_time:.2f}s ---\n")

    total_execution = time.time() - start_time
    print(f"Total Sequential Execution Time: {total_execution:.2f}s")
    return total_execution


if __name__ == "__main__":
    visitors = [
        MallVisitor(1, ["Laptop", "Water bottle"], "Where is the department store?"),
        MallVisitor(2, ["Umbrella"], "Where is the nearest ATM?"),
        MallVisitor(3, ["Backpack"], "What time does the mall close?")
    ]

    sequential_version(visitors)