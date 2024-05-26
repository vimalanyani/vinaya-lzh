# vinaya-lzh

An MVP project, with _super_ rough round the edges data prep and presentation.

## Data 

- for all round ease, as much as possible / makes sense, follow SC structure, aliases/ids etc.
    - Mahāsaṅghika Vinaya: https://suttacentral.net/pitaka/vinaya/lzh-mg-vi?lang=en

- add category number to file names.
- add leading zeros to file names where required.

### Prep

The `data_prep.py` is a quick and dirty tool to the raw source `txt` files into data the frontend can consume. Run with:

```sh
python3 scripts/data_prep.py
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

Deployed with GitHub Pages to vimalanyani.github.io/vinaya-lzh/.

SEE [DEPLOYMENT PICTURE GUIDE](src/docs/deploy/index.md)

## Things that could be done:

- 404 page
- page achnors
- index accordions
- data refinement
- clean up `data_prep.py` mess
- data validation
- linting
- define design system
- loads more stuff!

