import os
from typing import List

from setuptools import setup, find_packages


def _read_requirements(path: str) -> List[str]:
    with open(path, encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]


setup(
    name="alpha_clip",
    py_modules=["alpha_clip"],
    version="1.0",
    description="",
    author="OpenAI&ZeyiSun",
    packages=find_packages(exclude=["tests*"]),
    install_requires=_read_requirements(
        os.path.join(os.path.dirname(__file__), "requirements.txt")
    ),
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
