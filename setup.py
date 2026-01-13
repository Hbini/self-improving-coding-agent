from setuptools import setup, find_packages
setup(
    name='self-improving-coding-agent',
    version='0.1.0',
    author='Hernane Bini',
    description='Self-Improving Coding Agent powered by LLM',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'openai>=1.3.0', 'langchain>=0.1.0', 'transformers>=4.35.0',
        'fastapi>=0.104.0', 'pytest>=7.4.0', 'black>=23.12.0'
    ]
)
