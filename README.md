# byond2json

byond2json is a tool for converting BYOND hub and player data to JSON strings or Python dictionaries.

## Methods

* `hub2dict(game : str) -> dict:`
* `hub2json(game : str, indent) -> str:`
* `player2dict(player : str) -> dict:`
* `player2json(player : str, indent) -> str:`

The `indent` parameter is used for pretty-printing the JSON string; defaults to `4`.

## Example Usage

```python
from byond2json import hub2json

# print the current hub listing as JSON
print(hub2json("Exadv1/SpaceStation13"))
```

## Known Issues

* The hub tends to omit the last few (typically 3/4) hub entries from the output.
