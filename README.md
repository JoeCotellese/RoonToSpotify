# RoonToSpotify

I'm a huge fan of the application Roon. The one problem is that I can't stream my albums outside of my network. I wrote this little utility to take all of the albums in my Roon library and save them into my Spotify account.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

This project uses `pipenv` to manage dependencies, and assumes Python 3.7
You can can install `pipenv` with `pip`. You may want to set the `PIPENV_VENV_IN_PROJECT` environment variable on your development machine
(see pipenv docs for details).

To bootstrap your python envinronment
    pipenv install

### Usage
To see usage:
    pipenv run python RoonToSpotify.py --help

Note that the ALBUMS file expects an Excel XLSX file. Roon exports older Excel workbooks. Converting it requires Excel and is left as an exercise for the user.

## Built With

* [Spotipy](https://spotipy.readthedocs.io/en/latest/) - A great Python wrapper for Spotify

## Contributing

Pull requests are welcome

## Authors

* **Joe Cotellese** - *Initial work* - https://github.com/PurpleBooth

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
