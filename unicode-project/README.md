# Unicode Reader Mini Function

## Objective
To read Unicode characters off a HTML GOOGLE DOC file and present results as readable text.

## Requirements
- Allows user to enter the arguments for URL pointing to the required source.

## Components
- Comprises of a function to fetch table data in HTML from URL.
- Logic to read and extract table and convert table data into a dataframe.

## Methodology
1. **Data Extraction:** Use Pandas to read URL, extract table, and format table data.
2. **Matrix Creation:** Form a 2D matrix using max values of both `x` and `y` as extracted from source DOC.
3. **Looping:** Loop the range of rows in matrix, and loop the elements in list to extract `x`, `y`, and `Character` values using index.
4. **Placement:** Replace an element of the matrix using `x`, `y` as index positions and `Character` as the value.
5. **Final Polish:** Format to show output in correct sequence, and to remove list separators.

## Special Considerations
- Use `pandas` to easily manage extraction of max values, and to read HTML DOC from url.
- To work in rows, and to handle `x`, `y` as paired elements for easy checking.
- Avoid requirement to sort for looping (e.g., while `y=1`, do all `x`).
- **Axis Orientation:** y-axis descending top [max] to bottom [0].
- **Zero-Indexing:** Consideration for `x=0`, `y=0` (i.e. max +1 to keep within range).
- **Notation:** 2D matrix notation is swapped from `x,y` to `y,x` after creation.

## Library
- Pandas

## Output Explained
I elected to use the Pandas library to easily read the HTML DOC from the URL, and to extract the HTML table using `pd.read_html` and clean table data.

Using a 2D matrix of single char blanks formed by max values of both x-coordinate and y-coordinate, the resulting image is formed by looping through the range of rows and elements in the matrix and replacing blank values with the Unicode value of Character for each coordinate pair. 

The final image is formatted by removing list separators, and by reversing the y-axis loop into descending order from top [`y=max`] to bottom [`y=0`].

> **Note on Orientation:** An image is also generated when looping from `y=0` to `y=max`, showing 'M' instead of 'W'. However, calibration from the sample shows the correct orientation is y-descending.
