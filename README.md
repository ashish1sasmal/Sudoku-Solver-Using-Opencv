# Sudoku-Solver-Using-Opencv

#### "Solving wits and puzzles, in a way, helps to develop wit and ingenuity. "
    -- Shakuntala Devi
    
### A classic Sudoku Solver solves any sudoku puzzle using basic Image Processing, Python-Tesserect and backtracking algorithm.

#### Step-By-Step Procedure :
  1. Sudoku grid is pre-processed using image blurring (noise-removal), thresholding and erosion + dilation.
  2. Each cell of grid is seperated and stored using suitable contours.
  3. The contour based cells are sorted in left-to-right and top-to-bottom manner.
  4. The digits in cells are recognized using <b>Python-tesseract (Python-tesseract is an optical character 
  recognition (OCR) tool for python.</b> That is, it will recognize and “read” the text embedded in images.) </b>
  
  5. Final Step, the grid is stored in an 2d-array. The puzzle is solved using backtracking algorithm. 
  
#### Results :
<img src="https://github.com/ashish1sasmal/Sudoku-Solver-Using-Opencv/blob/master/Results/sudoku_solution.gif" width=320>
