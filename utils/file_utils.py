from pathlib import Path
from typing import Optional


def get_main_path():
    main_path: Optional[Path] = None

    if (Path('.') / 'data').exists():
        main_path = Path('.')
    else:
        parent_dirs = Path('.').absolute().parents
        for parent in parent_dirs:
            if (parent / 'data').exists():
                main_path = parent

        if main_path is None:
            print('Could not find the dataset path. Please run from the correct path')
            exit(-1)

    return main_path
