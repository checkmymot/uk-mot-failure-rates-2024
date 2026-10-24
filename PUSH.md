# Publishing the data repo

Same one-time GitHub setup as the widget (see `../garage-widget/PUSH.md`):
account → `checkmymot` org → public repo named `uk-mot-failure-rates-2024`.

Then:

```bash
cd ~/workspace/checkmymot/github/uk-mot-failure-rates-2024
git remote add origin git@github.com:checkmymot/uk-mot-failure-rates-2024.git
git push -u origin main
```

No Pages needed for this one (it's a data/code repo, not a site) —
though enabling Pages costs nothing.

## After publishing — make it earn links

- Add the repo link to the article
  (https://checkmymot.com/mot-failure-rates-by-town/) under the data table
  ("Download the full dataset on GitHub").
- Mention it in journalist follow-ups: data desks love a GitHub repo with
  methodology — it makes the story citable.
- Topics on the repo (GitHub → About → Topics):
  `mot`, `dvsa`, `uk`, `open-data`, `data-journalism`, `automotive`
