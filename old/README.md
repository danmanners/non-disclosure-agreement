# This is the deprecated first version using SQLite

Don't use it, but you know...it's here.

# Non-Disclosure Agreement

This project goal is to provide users a way to share files, strings, or URL's with each other by using a token. When creating the token, specifications for the lifetime of the object can be dictated. Once an object has reached the end of its life, it will behave as though it never existed.

## Usage

Run the application with `python main.py`.

### Adding new Data

Send a POST to it by running something like:

```shell
➜  curl -sL localhost:3000/new -XPOST -d 'https://google.com'
bf0f75323a5684c82f6cfc80190eb6589a96f511f80fb4573fe9235ad94a0fb6%
```

### Retrieving Data

Get a URL/String by running something like:

```shell
➜  curl localhost:3000/bf0f75323a5684c82f6cfc80190eb6589a96f511f80fb4573fe9235ad94a0fb6
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="https://google.com">https://google.com</a>.  If not click the link.%
```

Similarly, if you browse to http://localhost:3000/bf0f75323a5684c82f6cfc80190eb6589a96f511f80fb4573fe9235ad94a0fb6 in your browser, you will be redirected to https://google.com, as shown above from the curl response.

### Deleting Data

You can delete a string by adding the `DELETE` method to your curl, like this:

```shell
➜  curl -XDELETE localhost:3000/bf0f75323a5684c82f6cfc80190eb6589a96f511f80fb4573fe9235ad94a0fb6
token deleted, or it never existed.%
```

You can verify the token was deleted by attempting to hit it again

```shell
➜  curl localhost:3000/bf0f75323a5684c82f6cfc80190eb6589a96f511f80fb4573fe9235ad94a0fb6%
token deleted, or it never existed.%
```

## Notes

Right now, this application only uses a SQLITE3 database. This should be swapped for something else before any semblance of scale can be achieved.

I'm also not sure why you'd want to scale it. This is really just a shitty proof-of-concept.
