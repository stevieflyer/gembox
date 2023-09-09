# Steveflyer's Gembox 💎

This is a versatile, Python-based toolbox crafted with ❤️ by Steveflyer. It serves not only as a standalone repository of utilities but also as an essential package for other innovative projects under Steveflyer's belt.

Projects such as:
- **zephyrion**: A 🚀 pyppeteer-based headless web automation tool.
- **cetino**: A 🎈 lightweight and pythonic database manipulation tool.

## 🛠 Toolbox Contents

Gembox encapsulates a plethora of utilities streamlined for daily use, including:

### Core Utilities
- **date_utils**: 📅 Tools for effective date manipulations.
- **debug_utils**: 🐛 Essential debugging aids for developers.
- **re_utils**: 🧵 Regular expression utilities for efficient string processing.

### I/O Utilities
- **io**:
  - **pandas_io**: 🐼 I/O operations centered around Pandas.
  - **text_reader**: 📖 Efficient reading capabilities across multiple formats.
  - **_io**: Core I/O functionalities.

### Multiprocessing Utilities
### Multiprocessing Utilities 🚀

Gembox's multiprocessing utilities are tailored for efficient, parallel execution of both synchronous and asynchronous tasks. Leveraging the power of Python's multiprocessing and asyncio modules, it provides a seamless way to distribute and execute tasks across multiple CPU cores.

#### ParallelExecutor

The crown jewel of the multiprocessing utilities. `ParallelExecutor` facilitates the parallel execution of tasks. Whether you're dealing with synchronous or asynchronous tasks, this class got you covered.

Features:
- **Asynchronous Task Execution**: Seamlessly execute asynchronous functions in parallel across multiple processes.
- **Weighted Task Splitting**: Dynamically split tasks amongst worker processes based on their assigned weights, ensuring balanced work distribution.

Usage:
```python
tasks = [Task(function_name, params_dict), ...]
results = ParallelExecutor.run(tasks, n_workers=number_of_processes)
```

#### Task
A robust wrapper for any task (function) that you wish to execute, be it asynchronous or synchronous. The Task class ensures that each task is handled appropriately based on its nature.

Features:
- **Async Detection**: Automatically detects if a task is asynchronous and handles it accordingly during execution.
- **Weighted Execution**: Assign weights to tasks, which can then be used by the `ParallelExecutor` for balanced task distribution.

Usage:

With `gembox` 🚀, you can parallel your codes really easy
```python
# for example, you have a function:
def calc_something(input_df, threshold):
    # do something
    return output_df
```

Then, you can parallel it by:
```python
import asyncio
from gembox.multiprocessing import Task, ParallelExecutor

input_df_list = [df1, df2, df3, df4, df5]  # your input dataframes
tasks = [Task(calc_something, {'input_df': df, 'threshold': 0.5}) for df in input_df_list]

asyncio.run(ParallelExecutor.run(tasks, n_workers=5))
```

Super Easy, right? (✿◠‿◠)

This multiprocess utility ensures that your CPU cores are efficiently utilized, boosting the performance of your applications manifold.

### OpenAI Utilities
- **openai_util**: 🤖 Utilities tailored for OpenAI integrations.

### Pandas Utilities
- **pandas_util**: 🐼 Tools to supercharge your Pandas operations.

### Windows Utilities
- **win_utils**: 🪟 Specific tools for Windows operations, including word utilities.

### Scripts Utilities 🛠️

Gembox's script utilities offer a set of practical scripts that simplify frequent tasks, encapsulating complex operations into a single command. Currently, we've introduced a script that offers a fresh perspective on directory listing, aptly named `ls-py`.

#### ls-py

Move over traditional directory listing; `ls-py` is here to revolutionize the way you view your directory's contents!

Features:
- **Intuitive Listing**: Display directory contents in a structured tree format.
- **Recursive Listing**: Dive deep into directories with the recursive option.
- **Exclude Specific Items**: Have control over what you wish to see or skip.
- **Expand Hidden Directories**: Decide whether to peek into those hidden gems starting with "__" or ".".
- **Cross-Platform**: Whether you're on Windows, macOS, or Linux, `ls-py` has got you covered.

Usage:
```bash
ls-py [path] [options]
```

Examples:

1. **Simple Listing**: Just want to see what's in your current directory?
    ```bash
    ls-py
    ```
2. **Recursive Listing**: Want a deeper dive? No problem!
    ```bash
    ls-py -r ..
    ```
3. **Exclude Specific Items**: Want to skip those pesky .git and .idea folders? Easy easy!
    ```bash
    ls-py -r -x .git .idea __pycache__
    ```
4. **Expand Hidden Directories**: Want to peek into those hidden gems starting with "__" or "."? No problem!
    ```bash
    ls-py -r -e
    ```
Enhance your terminal experience with `ls-py` on any platform, a modern directory listing for the modern developer.

## 📦 Installation

To get started with Gembox, you can simply clone this repository or install it via pip (assuming it's available on PyPi).

```bash
pip install gembox
```

## Requirements

The required packages for Gembox are listed in requirements.txt. Ensure to install them for a smooth experience.

## 🤝 Contribution

Feel free to fork, enhance, create PRs and spread the word. Any contributions, big or small, are welcomed with open arms!

## ⭐ Star the Repo 
If you find this project useful, please consider giving it a star on [GitHub](https://github.com/stevieflyer/gembox).