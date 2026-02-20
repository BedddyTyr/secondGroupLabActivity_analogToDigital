import multiprocessing
import time
from dataclasses import dataclass

# Object programming approach: Defining the Visitor class
@dataclass
class MallVisitor:
    id: int
    items: list      # Items to be inspected
    question: str    # Inquiry for the guard

def inspection_stage(input_queue, output_queue):
    """Stage 1: Guard inspecting bags/items."""
    while True:
        visitor = input_queue.get()
        if visitor is None: # Poison pill to stop the process
            output_queue.put(None)
            break

        print(f"[Stage 1] Guard inspecting Visitor {visitor.id}'s items: {visitor.items}...")
        time.sleep(1)  # Simulating inspection time

        # Pass the visitor and the time they entered the system to the next stage
        output_queue.put(visitor)

def inquiry_stage(input_queue):
    """Stage 2: Guard answering inquiries."""
    while True:
        visitor = input_queue.get()
        if visitor is None:
            break

        print(f"[Stage 2] Guard answering Visitor {visitor.id}'s question: '{visitor.question}'")
        time.sleep(1.5)  # Simulating inquiry time

if __name__ == "__main__":
    # 1. Initialize the Visitors
    visitors = [
        MallVisitor(1, ["Laptop", "Water bottle"], "Where is the department store?"),
        MallVisitor(2, ["Umbrella"], "Where is the nearest ATM?"),
        MallVisitor(3, ["Backpack"], "What time does the mall close?")
    ]

    # 2. Setup Communication Queues
    entry_queue = multiprocessing.Queue()
    mid_queue = multiprocessing.Queue()

    # 3. Create the Processes
    guard_a = multiprocessing.Process(target=inspection_stage, args=(entry_queue, mid_queue))
    guard_b = multiprocessing.Process(target=inquiry_stage, args=(mid_queue,))

    # --- START TOTAL TIMER HERE ---
    start_total_pipeline = time.time() 

    guard_a.start()
    guard_b.start()

    # 4. Feed visitors into the pipeline
    for v in visitors:
        entry_queue.put(v)

    # Add poison pill
    entry_queue.put(None)

    # 5. Wait for finish
    guard_a.join()
    guard_b.join()

    # --- END TOTAL TIMER HERE ---
    end_total_pipeline = time.time()
    total_duration = end_total_pipeline - start_total_pipeline

    print("\n" + "="*40)
    print(f"All visitors processed via Pipelining.")
    print(f"TOTAL PARALLEL EXECUTION TIME: {total_duration:.2f} seconds")
    print("="*40)