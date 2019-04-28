# decode-django

Decode in Django

Components:
- Encoding/Decoding
- API wrapping decoding logic
- End-user web page

The components fit together as follows:

    [web page -> api -> decode logic]

## Encoding/Decoding

First lets dig into the encoding/decoding algorithm as it is lies at the core
of the app and is probably the most challenging. Consider that a simple
ASCII-like character encoding exists with the following mapping:

- 'A' = 1
- 'B' = 2
- ..
- 'Z' = 26

Let's quickly look at some sample encodings:

- "BBF" -> 226
- "AB" -> 12
- "L" -> 12

You probably already see an issue lurking here. Both "AB" and "L" are encoded
in the same way. This makes decoding the result quite the challenge.

The decoding of encoded strings assumes we're only dealing with numerical
digits with zero excluded (as per the encoding). The decoding algorithm takes
an encoded string and returns all the different ways the input could possibly
be decoded. For example, the input string, "226" can be decoded in 3 different
ways.

- (2, 2, 6) or "BBF"
- (2, 26) or "BZ"
- (22, 6) or "VF"

To get there I've used a tree-based approach. Perhaps there are other ways and
I'd be interested in hearing about them. Here goes!

We'll use "1234" as our input string. Let's see if we break the problem down a
bit, "divide and conquer". We know the encoding only goes up to 26 and so we
only need to consider single and double-digit combinations. So 12 is valid but
123 is definitely not a valid encoding. So looking at the first two digits we
can say it is encoded as either 1 (followed by 2 or 23) or 12 (followed by 3 or
34). We can apply the same logic to 2... it is followed by either 3 or 34.

<<Tree>>

Recursion

Each node has an optional left and right edge.

You'll notice that we always have a possible decoding by taking each digit
individually. This also gives an indication of the depth of the tree. So the
depth is equal to the length of the input string.

Each unique path from root to leaf is a possible decoding. Traversing the tree
could be done after it has been built but can also be done while building the
tree.

Nodes with values greater than 26 may be eliminated. As of now they are emitted
as an underscore.

## API

The decoding logic is exposed via a simple HTTP API. There is a single endpoint
which accepts the input string and returns all possible decodings.

Request:

    GET /api/decode/?input=226

Response:

    200 OK

    {
      "result": [
        "BBF",
        "BZ",
        "VF"
      ]
    }

If the input string contains invalid input a 400 status code is returned.

## End-user Web Page

An end-user may navigate their browser to a web page and provide an input
string for decoding. On submitting the input an API call is made to retrieve
all decodings which are then itemized on the page.

## Bugs and Limitations

For now the input string is capped to XX characters. Still need to re-evaluate
the maximum length of the input string. There are a number of factors to
consider here:

- The decoding algorithm, i.e. run time, recursion limit (call stack)
- Requests timing out
- The maximum size of an HTTP request
- The actual end-user use case

## ToDo
- API error handling, i.e. timeouts
- Get clarification if nodes > 27 (outside of encoding range) may be
  eliminated.
- Add property based testing for codec
