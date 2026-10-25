import tokenize
from io import BytesIO
with open("source.py", "rb") as f:
    data = f.read()
tokens = tokenize.tokenize(BytesIO(data).readline)
result = []
for token in tokens:
    if token.type != tokenize.COMMENT:
        result.append(token)
with open("without_comments.py", "w", encoding="utf-8") as f:
    f.write(tokenize.untokenize(result).decode("utf-8"))
