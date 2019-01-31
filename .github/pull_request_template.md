Please make sure you do the following when updating the layer index:

* [ ] Add or update the JSON file for your layer, in the appropriate subdirectory (`layers` or `interfaces`)
* [ ] Add an explicit `docs` URL field to your JSON, if appropriate.  If omitted, it will default to the `README.md` at the root of your repo, but you may want to provide a more specific URL.  If you're using the `subdir` field, then you definitely want to point to the README of the layer rather than the repo.
* [ ] Run `update_readme.py` to update the user-friendly index in the README
