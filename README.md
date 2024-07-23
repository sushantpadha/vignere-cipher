<img src="./icon.png" height=128></img>

# vignere-cipher
Basic implementation of a Vigenere Cipher in Python.

## Installation

This project uses the [poetry](https://python-poetry.org/) build tool.

First, `git clone` the project and `cd` into the project root folder

Then, install the project with all dependencies in a virtual environment using `poetry install`

Enter a new shell using `poetry shell` (optionally set environment variable `VIRTUAL_ENV_DISABLE_PROMPT=1` to disable the prompt prefix).


## Usage

Follow the steps outlined in the [Installation](#installation) section.

Run the script using `poetry run vignere_cipher` followed by command line arguments.

### Command line usage

```text
usage: vignere_cipher.cmd [-h] -k KEY [-e | -d] [--extended] text

encrypt and decipher messages with vignere cipher

positional arguments:
  text        text message to decrypt or encrypt standard mode: non-alphabetic characters and cases of alphabetic characters will be
              preserved extended mode: all characters will be en/decrypted according to extended alphabet, non-ascii characters will be
              preserved

options:
  -h, --help  show this help message and exit
  -k KEY      key to use to en/decrypt text case is preserved (if applicable) and non-alphabet characters are preserved
  -e          encrypt text using key
  -d          decrypt text using key
  --extended  use extended alphabet consisting of all ascii characters from 33 to 126. prefer using raw strings

“Sometimes it’s the people no one imagines anything of who do the things that no one can imagine.” (Alan Turing)
```

### Examples

1. To encrypt the text `attackatdawn` with the key `lemon`:

  ```bash
  $ poetry run vignere_cipher "attackatdawn" -k "lemon" -e
  lxfopvefrnhr
  ```

2. To decrypt the text `lxfopvefrnhr` with the key `lemon`:

  ```bash
  $ poetry run vignere_cipher "lxfopvefrnhr" -k "lemon" -d
  attackatdawn
  ```

3. To encrypt the text `godsavethequeen` with the key `pickle`, using the extended alphabet (ASCII chars 33-126):
   ```bash
   $ poetry run vignere_cipher "godsavethequeen" -k "pickle" -e --extended
   XYH_N\V^LQ^[VOR
   ```

## Developing

1. Download the source code.
2. Open up a terminal.
3. `cd` into the project root †.
4. Install the project using steps outlined in [Installation](#installation)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Notes

Learn more about vignere cipher:
- https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
- https://crypto.interactive-maths.com/vigenegravere-cipher.html
- https://www.geeksforgeeks.org/vigenere-cipher/

:exclamation: CAUTION: :exclamation:
This script should not be used for serious security or cryptographic purposes.
It is only a fun project to use encrypted messages for basic demonstrations or amusement.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

† Project root is the folder named "vignere-cipher" at the top level, i.e., it is shalloww

†† Source root is the folder named "vignere_cipher" inside another folder named "vignere-cipher", i.e., it is deep (nested)

