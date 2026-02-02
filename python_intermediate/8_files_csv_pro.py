import csv
import time
import logging
from contextlib import contextmanager, suppress

# Basic logging configuration
# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Context manager for messuring time
# Gestor de contexto para medir el tiempo
@contextmanager
def mesuring_time(name_process):
    beginning = time.perf_counter()
    try:
        yield
    finally:
        duration = time.perf_counter() - beginning
        logging.info(f"{name_process} tomó {duration:.4f} segundos")


total = 0

with mesuring_time("Sales calculation"), \
     suppress(FileNotFoundError), \
     open("data/sales.csv", newline="") as f:

    reader = csv.DictReader(f)

    for row in reader:
        try:
            price = float(row["price"])
            quantity = int(row["quantity"])
            total += price * quantity
        except (ValueError, KeyError) as e:
            logging.warning(f"Invalid row skipped: {row} ({e})")

print("Total sales:", total)