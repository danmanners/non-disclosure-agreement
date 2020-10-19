# Non-Disclosure Agreement

This project goal is to provide users a way to share files, strings, or URL's with each other by using a hash code. When creating the hash, specifications for the lifetime of the object can be dictated. Once an object has reached the end of its life, it will behave as though it never existed.

## Usage

Run the application with `python main.py`.

### Adding new URLs

Send a POST to it by running something like:

```shell
➜  curl -sL localhost:3000/new -XPOST -d '{"data":"https://stackoverflow.com/questions/12244057/any-way-to-add-a-new-line-from-a-string-with-the-n-character-in-flask"}'
4788b32ebdf95a4ebd8c9acb3105cbc5ea14bdeff5fd266e1408a1d5a996a742%
```

### Get Data

Get a URL/String by running something like:

```shell
➜  curl localhost:3000/a50c704411aadef1a54b940045bf81da3a3e4759e1a1dd8bb803965283832fde
https://stackoverflow.com/questions/12244057/any-way-to-add-a-new-line-from-a-string-with-the-n-character-in-flask
```

Similarly, if you browse to http://localhost:3000/a50c704411aadef1a54b940045bf81da3a3e4759e1a1dd8bb803965283832fde in your browser, you will be redirected to https://stackoverflow.com/questions/12244057/any-way-to-add-a-new-line-from-a-string-with-the-n-character-in-flask, as shown above from the curl response.

## Notes

Right now, this application only uses a SQLITE3 database. This should be swapped for something else before any semblance of scale can be achieved.

