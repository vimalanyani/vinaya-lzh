# vinaya-lzh

An MVP project, with _super_ rough round the edges data prep and presentation.

## Data 

- for all round ease, as much as possible / makes sense, follow SC structure, aliases/ids etc.
    - Mahāsaṅghika Vinaya: https://suttacentral.net/pitaka/vinaya/lzh-mg-vi?lang=en

- add category number to file names.
- add leading zeros to file names where required.

### Prep

In it's current prototype form, `data_prep.py` needs to be run from its containing directory with relative input and output paths:

Example commands:

```sh
cd src/data
python3 data_prep.py --input_dir ./mg/vb/src --output_dir ./mg/vb/json --school "Mahāsaṅghika Vinaya" --book "Bhikkhunī Vibhaṅga" --has_rule_class

python3 data_prep.py --input_dir ./mg/pn/src --output_dir ./mg/pn/json --school "Mahāsaṅghika Vinaya" --book "Bhikkhunī Pakiṇṇaka"

python3 data_prep.py --input_dir ./mg/gd/src --output_dir ./mg/gd/json --school "Mahāsaṅghika Vinaya" --book "Garudhammas"

python3 data_prep.py --input_dir ./mg/pm/src --output_dir ./mg/pm/json --school "Mahāsaṅghika Vinaya" --book "Bhikkhunī Pātimokkha"
```

The rule data “schema“ appied in `data_prep.py` is defined in `src/data/types.ts` and consumed `src/utils/getAllBookRuleData.ts` and fed down through the app.

#### source `txt` files:

- the source translation `txt` use the following custom markup:

    ```html
    <lzh-fascicle-start> ... </lzh-fascicle-start>
    <!-- en-fascicle-start can be broken per line -->
    <en-fascicle-start> ... </en-fascicle-start> 
    <lzh-fascicle-end> ... </lzh-fascicle-end>
    <en-fascicle-end> ... </en-fascicle-end>
    <lzh-division-start> ... </lzh-division-start>
    <en-division-start> ... </en-division-start>
    <en-division-end> ... </en-division-end>
    <lzh> ... </lzh>
    <h2> ... </h2>
    <note> ... </note>
    <verse> ... </verse>
    ```
- source text files have have been renamed with leading zeros.


## Deployment

Deployed with GitHub Pages. Specifics to come!

## Things that could be done:

- update font-family for improved special character handling in all font sizes. 
- data validation
- define design system
- componentize rule page
- content sectioning
- 404 page
- actions
- loads more stuff!

## Astro Starter Kit: Basics

```sh
npm create astro@latest -- --template basics
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/astro/tree/latest/examples/basics)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/astro/tree/latest/examples/basics)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/withastro/astro?devcontainer_path=.devcontainer/basics/devcontainer.json)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

![just-the-basics](https://github.com/withastro/astro/assets/2244813/a0a5533c-a856-4198-8470-2d67b1d7c554)

### 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   └── Card.astro
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

### 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

### 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
