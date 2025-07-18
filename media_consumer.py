import os
import time

def consume_media():
    """
    This function will consume media from the predefined directories.
    """
    directories = [
        "~/0.SelfImprovement",
        "~/1.AIML",
        "~/2.Programming",
        "~/3.Investment",
        "~/4.SkillPolish",
        "~/5.Entertainment"
    ]

    for directory in directories:
        directory = os.path.expanduser(directory)
        if os.path.exists(directory):
            print(f"Consuming media from: {directory}")
            for root, _, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    print(f"  - Consuming: {filepath}")
                    # Simulate media consumption
                    time.sleep(1)
            print("-" * 20)

if __name__ == "__main__":
    consume_media()
