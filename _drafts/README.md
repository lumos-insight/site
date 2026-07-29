# Drafts

Work-in-progress posts live here, one folder per post, same layout as `posts/`
(e.g. `_drafts/my-new-idea/index.qmd`).

- This folder is git-ignored (see `.gitignore`) except for this file, so drafts
  never get committed by accident.
- The `_` prefix also keeps Quarto from rendering it into the site — same
  convention as `_extensions/` and `_site/`.
- When a post is ready to publish: rename the folder to
  `YYYY-MM-DD-slug` and `mv` it into `posts/`.
