# Decode

## Decoding

- Only the digits 1-9 are allowed in the input string.

## API

The decoding capability is exposed via a simple HTTP API. There is a single
endpoint.

Request:

    GET /api/decode/?input=226

Response:

OK: 200

    {
      "result": [
        "BBF",
        "BZ",
        "VF"
      ]
    }

Invalid Input:

NOK: 400

## Limitations
Re-evaluate the maximum length of the input string. There are a number of
factors to consider:

- The decoding algorithm/requests timing out
- The maximum size of an HTTP request
- The actual end-user use case

For now the input string is capped to 16 characters.

## ToDo
- API error handling, i.e. timeouts
