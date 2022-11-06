import os.path


def filename():
    from pathlib import Path
    return (
        Path(os.path.abspath(__file__))
        .parent
        .parent
        .parent
        .joinpath('resources')
        # .joinpath('koren.txt')
        .absolute()
        .__str__()
    )


