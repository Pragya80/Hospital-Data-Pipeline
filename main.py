from src.utils import ensure_directories, log
from src.bronze import run_bronze
from src.silver import run_silver
from src.gold import run_gold
from src.visualize import run_visualizations


def main():

    ensure_directories()

    log("Starting hospital data pipeline")

    run_bronze()

    run_silver()

    run_gold()

    run_visualizations()

    log("Pipeline completed successfully")


if __name__ == "__main__":
    main()