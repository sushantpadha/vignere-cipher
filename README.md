# vignere-cipher
encrypt and decipher messages with vignere cipher

## Installation

Run the following command

```bash
python -m pip install git+https://Sushant-Padha/vignere-cipher.git
```


## Usage

Follow the steps outlined in the [Installation](#installation) section.

Use the script with the command

```bash
python -m vignere_cipher
# or
python vignere_cipher
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

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

† Project root is the folder named "vignere-cipher" at the top level, i.e., it is shalloww

†† Source root is the folder named "vignere_cipher" inside another folder named "vignere-cipher", i.e., it is deep (nested)

