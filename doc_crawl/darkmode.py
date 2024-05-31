darkmode_css = """
@namespace epub "http://www.idpf.org/2007/ops";

/* Base Styles */
body {
    background-color: #1e1e1e;
    color: #d4d4d4;
    font-family: 'Georgia', serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

p {
    margin: 1em 0;
}

h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    font-weight: bold;
}

h1 {
    font-size: 2em;
}

h2 {
    font-size: 1.75em;
}

h3 {
    font-size: 1.5em;
}

h4 {
    font-size: 1.25em;
}

h5 {
    font-size: 1em;
}

h6 {
    font-size: 0.875em;
}

/* Links */
a {
    color: #569cd6;
    text-decoration: none;
}

a:hover, a:focus {
    text-decoration: underline;
}

/* Code */
code, pre {
    background-color: #2d2d2d;
    color: #dcdcdc;
    font-family: 'Courier New', monospace;
    padding: 0.2em;
    border-radius: 4px;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #555;
    padding-left: 1em;
    color: #999;
    margin: 1.5em 0;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
}

/* Lists */
ul, ol {
    margin: 1em 0;
    padding-left: 2em;
}

li {
    margin: 0.5em 0;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    background-color: #2d2d2d;
}

th, td {
    border: 1px solid #444;
    padding: 0.5em;
}

th {
    background-color: #333;
    color: #ffffff;
}

td {
    color: #d4d4d4;
}

/* Misc */
hr {
    border: 0;
    border-top: 1px solid #444;
    margin: 2em 0;
}

"""