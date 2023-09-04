# HOW SOLVE pdf-with-js ERROR on LINUX


## Explanation:

For anyone who fall into same problem:
I have forked plugin repo and modified mkdocs_with_pdf/drivers /headless_chrome.py file to render diagrams to png before generating pdf. I decided to do it because even if I managed to generate diagrams from javascript in pdf text labels were missing because of underlying print engine + svg files.

Diagrams in static page are still rendered by javascript lib, pngs are only for pdf generation.


[see this `https://gist.github.com/krukowskid/c47fc76056d1fb7b991ef628db96c96f`](https://gist.github.com/krukowskid/c47fc76056d1fb7b991ef628db96c96f)


its using mmdc so you need to install mermaid-cli




