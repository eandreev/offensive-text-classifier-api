# Offensive Message Text Classifier API

## API Description

This docker container exposes an API that allows to detect an offensive message.

API endpoint: `/classify` on port `80`.

The API call expects a POST call with a JSON body of the following form:

```
{ "text": "message text" }
```

(Don't forget to set the `Content-Type: application/json` HTTP request header.)

It returns JSON of the following form:

```
{ "class": 0 }
```

where `1` indicates that the message was classified as offensive.

## How to Test

### Using `docker run`

Run the container:

`$ docker run -p 80:80 eandreev/offensive-text-classifier-api`

In another terminal window, issue the following requests:

Neutral text:

```
$ curl \
    -d '{"text": "some neutral text"}' \
    -H "Content-Type: application/json" \
    localhost/classify

{"class":0}
```

Offensive text:

```
$ curl \
    -d '{"text": "some neutral text that nevertheless contains SCUM IDIOT"}' \
    -H "Content-Type: application/json" \
    localhost/classify

{"class":1}
```

A POST body that is missing the required field `text`:

```
$ curl \
    -d '{"other": [1,2]}' \
    -H "Content-Type: application/json" \
    localhost/classify

{"detail":"The \"text\" string field is required"}
```

A POST body where the `text` field is not a string:

```
$ curl \
    -d '{"text": [1,2]}' \
    -H "Content-Type: application/json" \
    localhost/classify

{"detail":"The \"text\" string field is required"}
```

### Using `docker-compose`

```
docker-compose up
```