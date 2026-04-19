import sys
import warnings
from ai_care_coordintor.crew import CareCoordinatorCrew

warnings.filterwarnings("ignore", category=SyntaxWarning)

def run() -> None:
    """
    Run the Care Coordinator crew.
    """
    # Example: Load patient data or other required inputs here
    # For demonstration, using placeholder values
    inputs = {
        'discharge_text': 'Sample discharge plan text.',
        'symptom_report': 'Sample symptom report.',
        'biometric_data': 'Sample biometric data.',
        'care_plan': 'Sample care plan.',
    }
    crew = CareCoordinatorCrew().crew()
    crew.kickoff(inputs=inputs)
    print(crew.usage_metrics)



def train() -> None:
    print("train")


def replay() -> None:
    print("replay")
    run()

def test() -> None:
    print("test")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [run|train|replay|test]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        print("Usage: python main.py [run|train|replay|test]")
        sys.exit(1)
