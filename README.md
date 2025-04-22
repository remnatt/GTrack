# GTrack
> [!IMPORTANT]
>
> **This is NOT to be used maliciously. Please refrain from using it in any possible way of harm. All though I can not force you to I hope you comply.**


### `GTrack.py` Arg Commands

```json
[
  {
    "argument": "--api",
    "type": "flag",
    "description": "Enables GitHub API usage mode."
  },
  {
    "argument": "--botAs",
    "type": "string",
    "description": "Specifies the GitHub bot username used for commits."
  },
  {
    "argument": "--botPfp",
    "type": "string (URL)",
    "description": "Sets a profile picture for the bot (must be a direct .png link)."
  },
  {
    "argument": "--incommit",
    "type": "flag",
    "description": "Triggers initial commit logic if set."
  },
  {
    "argument": "--readme",
    "type": "string ('true' or 'false')",
    "description": "Determines whether to create a README.md file."
  },
  {
    "argument": "--bold",
    "type": "flag",
    "description": "If true, formats README content in bold."
  },
  {
    "argument": "--licsensetype",
    "type": "integer (1-5)",
    "description": "Selects a license type to add to the repo. Options: 1=MIT, 2=Apache 2.0, 3=Apache 2.0, 4=Unlicense, 5=GPLv3."
  },
  {
    "argument": "--gitignore",
    "type": "string ('true' or 'false')",
    "description": "Adds a .gitignore file with default content if 'true'."
  },
  {
    "argument": "--extrafile",
    "type": "string",
    "description": "Specifies the base name of an extra file to add (e.g., 'header')."
  },
  {
    "argument": "--extrafiletype",
    "type": "string",
    "description": "File extension/type for the extra file (e.g., 'py', 'md')."
  },
  {
    "argument": "--content",
    "type": "string",
    "description": "Content to write into the extra file or SECURITY.md if applicable."
  },
  {
    "argument": "--customcommitmessage",
    "type": "string",
    "description": "Custom commit message to use for all file operations."
  },
  {
    "argument": "--vmode",
    "type": "flag",
    "description": "Versioned mode: replaces existing files instead of skipping them."
  },
  {
    "argument": "--addtimestamp",
    "type": "string ('true' or 'false')",
    "description": "If 'true', includes timestamps in the logger output."
  },
  {
    "argument": "--SecurityFile",
    "type": "string ('true' or 'false')",
    "description": "Adds a SECURITY.md file with default or custom content."
  }
]

```
