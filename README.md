<img src="./icon.png" height=128></img>

# vignere-cipher
encrypt and decipher messages with vignere cipher

## Installation

Run the following command

```bash
python -m pip install git+https://github.com/Sushant-Padha/vignere-cipher.git
```


## Usage

Follow the steps outlined in the [Installation](#installation) section.

Use the script with the command

```bash
python -m vignere_cipher [options]
```

### Command line usage

```text
usage: vignere_cipher [-h] -k KEY [-e | -d] text

encrypt and decipher messages with vignere cipher

inspired by the movie Imitation Game, 2014 (no, this is not the Enigma cipher)

positional arguments:
  text        text message to decrypt or encrypt (all non-alphabetic characters will be removed)

optional arguments:
  -h, --help  show this help message and exit
  -k KEY      key to use to en/decrypt text (all non-alphabetic characters will be removed)
  -e          encrypt text using key
  -d          decrypt text using key

“Sometimes it’s the people no one imagines anything of who do the things that no one can imagine.” (Imitation Game, 2014)
```

### Examples

1. To encrypt the text `attackatdawn` with the key `lemon`, use the following command

  ```bash
  python -m vignere_cipher "attackatdawn" -k "lemon" -e
  ```

2. To decrypt the text `lxfopvefrnhr` with the key `lemon`, use the following command

  ```bash
  python -m vignere_cipher "lxfopvefrnhr" -k "lemon" -d
  ```

## Developing

1. Download the source code.
2. Open up a terminal.
3. `cd` into the project root†.
4. Run the command (mind the period at the end of the command)
   ```bash
   python -m pip install -e .
   ```

To develop you will need to install [Python3](https://python.org) for your specific OS and architecture

Other than that, you will also need some dependencies.

They can be installed from the `requirements.txt` file provided in the source.

Just run

```bash
python -m pip install -r requirements.txt
```

To run tests, simply `cd` into the source root†† and execute the following command

```bash
python -m pytest .
```

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

