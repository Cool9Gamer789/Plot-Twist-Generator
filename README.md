# Plot Twist Generator

This is a Python script that uses the [OpenRouter API](https://openrouter.ai) and the DeepSeek model to generate surprising plot twists from a given story summary.

## Requirements

- Python 3.7 or higher
- [openai](https://pypi.org/project/openai/) Python library

## Installation

1. Install the `openai` library:
   ```bash
   pip install openai
   ```
2. Obtain a free API key from [OpenRouter API](https://openrouter.ai).
3. Replace the empty string in:
```python
api_key=""
```
with your own API key.

## Usage
1. Run the script
```bash
python main.py
```
2. When prompted:
* Enter a short story summary.
* Example:
```bash
A young archaeologist discovers a sealed chamber beneath an ancient temple, containing artifacts from a civilization no historian has ever documented.
```
3. The generated plot twist will be saved to a file named twist.txt.
